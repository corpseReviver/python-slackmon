import slack
import time
import os
import sys
from pathvalidate import sanitize_filepath


class Monitor:
    def __init__(self, token, outfile, frequency, verbose):
        self.cwd = os.path.abspath(os.getcwd())
        self.token = token
        self.outfile = outfile
        self.frequency = frequency
        self.verbose = verbose
        self.client = None
        self.data = {}

    def vprint(self, msg: str) -> None:
        """Print message to console if verbose flag is set.
        
        Arguments:
            msg {str} -- A string to print
        """

        if self.verbose:
            print(msg)

    def start_monitor(self) -> None:
        """Gets the slack client, tests for connectivity to Slack
        and validates arguments. 
        
        """

        self.init_slack_client()
        self.test_slack_connection()
        self.validate_input()

    def init_slack_client(self) -> None:
        """Creates a Slack client from API token.

        """

        self.client = slack.WebClient(token=self.token)
        self.vprint('--> Slack client initalized.')

    def test_slack_connection(self) -> None:
        """Tests connection to Slack API. 


        Uses the Slack web API api_test method to test.
        If the test is successfull the response will return 
        True in the "ok" key. 

        """

        try:
            response = self.client.api_test()
        except Exception as e:
            print('--> Slack Web API connection failed. Exception --> {}'.format(e))
            sys.exit()

        if response.get('ok') is False:
            raise Exception('Unable to connect to the Slack Web API.')

    def validate_input(self) -> None:
        """Validates arguments

        Test case 1: Frequency must be an int and between 3600 and 604800
        Test case 2: Sanitized file path for outfile argument
        Test case 3: Confirm outfile is a JSON file, if not convert it. 

        """

        # Frequency validation
        if not self.frequency:
            self.frequency = 3600
            self.vprint(
                '--> No frequency set so setting to default value of 3600 seconds.')

        if not type(self.frequency) == int:
            raise Exception(
                'Frequency must be an integer, must be in seconds, and between 3600 (1 day) and 604800 (1 week)')

        if self.frequency < 3600 or self.frequency > 604800:
            raise Exception(
                'Frequency must be in seconds, and between 3600 (1 day) and 604800 (1 week)')

        self.vprint('--> Frequency has been set to {}'.format(self.frequency))

        # Outfile validation
        if self.outfile:
            # Sanatizes output file. Removed script characters and blank spaces
            self.outfile = sanitize_filepath(self.outfile)
            self.vprint('--> Santized outfile to {}'.format(self.outfile))

            # Confirm outfile is a JSON file, if not convert to JSON
            basename = os.path.basename(self.outfile)
            basepath = self.outfile.split(basename)[0]
            base = basename.split('.')[0]
            ext = '.'.join(basename.split('.')[1:]) 
            self.vprint('--> Outfile details. Basename: {}, Basepath: {}, Base: {}, Ext: {}'.format(basename, basepath, base, ext))

            if not ext.lower() == 'json' or not ext:
                self.outfile = os.path.join(basepath, '{}.json'.format(base))
                self.vprint('--> Converted outfile to JSON. New File {}'.format(self.outfile))
                

    def get_formatted_outfile(self) -> str:
        """Returns the output file sanatized and formatted for JSON. 
        
        Returns:
            str -- Fromatted output file
        """
        return self.outfile


    def get_conversation_list(self, types: str) -> dict:
        """Returns a list of all conversations by channel type.

           Uses Slack web API method conversations_list to
           lists all channels in a Slack team.

        Arguments:
            types str -- Slack channel type. Available
                       types are im, private_channel,
                       public_channel, and mpim. 

        Returns:
            dict -- Conversation list 
        """
        response = self.client.conversations_list(types=types)
        self.vprint('--> Returned the coversations list for {}'.format(types))

        return response

    def translate_user_id(self, user_id:str) -> dict:
        """Converts a Slack user ID to a real name and email address

        Using the Slack API method users.info, we return the users
        real name, which was entered on account creation, and email from
        the users ID. 

        Arguments:
            client {slack object} -- A Slack websocket client
            user_id {str} -- A Slack user ID

        Returns:
            {dict} -- Response that contains a status of the response
                      query and the paylod.  
                ### Return format ###
                {
                    "status": "{str} error | complete",
                    "data": "{list} coversation_list response"
                }
        """

        response = self.client.users_info(user=user_id)

        try:
            real_name = response.get('user').get('profile').get('real_name')
        except:
            real_name = 'Not found'

        try:
            email = response.get('user').get('profile').get('email')
        except:
            email = 'Not found'

        return {"real_name": real_name, "email": email}

    def get_history(self, response: dict, types:str='im') -> dict:
        """Returns messages of a Slack channel. 
        
        Uses Slack web API method conversations_history to fetch 
        history of messages and events from direct message channels.
        
        Arguments:
            response {dict} -- Slack Web API response from conversation_list.
        
        Keyword Arguments:
            types {str} -- Slack channel type. Available
                           types are im, private_channel,
                           public_channel, and mpim.  (default: {'im'})
        
        Returns:
            {dict} -- Response that contains a status of the response
                      query and the paylod. 
                ### Return format ###
                {
                    "status": "{str} error | complete",
                    "data": "{list} coversation_history response"
                }
        """

        data = {}
        now = time.time()
        oldest = int(now - self.frequency) + (now % self.frequency > 0)

        while True:
            next_cursor = response.get('response_metadata').get('next_cursor')

            # Generate all channel ID's returned in response.
            channel_ids = [x.get('id') for x in response.get('channels')]
            self.vprint('--> Generated a list of channel ids {}'.format(channel_ids))

            for channel_id in channel_ids:
                # Grab IM message details for a channel ID. Only
                # return message details from now until the oldest frequency number.
                response = self.client.conversations_history(
                    channel=channel_id, oldest=str(oldest))

                # If any messages are returned, add them to the
                # response dictionary.
                messages = response.get('messages')
                if messages:
                    for message in messages:
                        self.vprint('--> Message found for channel ID {}'.format(channel_id))

                        user_id = message.get('user')

                        # adds users real_name and email into message log
                        message.update(
                            {'user_info': self.translate_user_id(user_id)})

                    data[channel_id] = {"data": messages}

            # If more data is available, request the next page.
            # Otherwise break the loop.
            if next_cursor:
                response = self.client.conversations_list(
                    types=types, cursor=next_cursor)
            else:
                break

        return data

    def get_im_messages(self) -> dict:
        """Returns all IM messages within a given time period. 
        
        Time period is determined by the frequency argument. 
        
        Returns:
            {dict} -- Response that contains a status of the response
                  query and the paylod. 
            ### Return format ###
            {
                "status": "{str} error | complete",
                "data": "{list} coversation_history response"
            }
        """

        response = self.get_conversation_list(types='im')
        response = self.get_history(response=response, types='im')

        return response

    def get_mpim_messages(self) -> dict:
        """Returns all MPIM messages within a given time period. 
        
        Time period is determined by the frequency argument. 
        
        Returns:
            {dict} -- Response that contains a status of the response
                  query and the paylod. 
            ### Return format ###
            {
                "status": "{str} error | complete",
                "data": "{list} coversation_history response"
            }
        """

        response = self.get_conversation_list(types='mpim')
        response = self.get_history(response=response, types='mpim')

        return response

    def get_public_channel_messages(self) -> dict:
        """Returns all public channel messages within a given time period. 
        
        Time period is determined by the frequency argument. 
        
        Returns:
            {dict} -- Response that contains a status of the response
                  query and the paylod. 
            ### Return format ###
            {
                "status": "{str} error | complete",
                "data": "{list} coversation_history response"
            }
        """

        response = self.get_conversation_list(types='public_channel')
        response = self.get_history(response=response, types='public_channel')

        return response

    def get_private_channel_messages(self) -> dict:
        """Returns all private channel messages within a given time period. 
        
        Time period is determined by the frequency argument. 
        
        Returns:
            {dict} -- Response that contains a status of the response
                  query and the paylod. 
            ### Return format ###
            {
                "status": "{str} error | complete",
                "data": "{list} coversation_history response"
            }
        """
        response = self.get_conversation_list(types='private_channel')
        response = self.get_history(response=response, types='private_channel')

        return response
