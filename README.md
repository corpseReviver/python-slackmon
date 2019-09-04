# Slackmon
Slackmon is a Slack channel message retriever. It obtains Slack messages for all channels (public, private, direct, and group) for a specified amount of time for any Workspace.

# Installation
$ pip install slackmon

****or from src****

$ git clone git@github.com:corpseReviver/python-slackmon.git

$ python python-slackmon/setup.py install

# Usage from CLI

$ slackmon [-h] [-v] [--token] [--im] [--mpim] [--private-channels] [--public-channels] [-o OUTFILE] [-f FREQUENCY]

**required arguments:**

 ** --token:** Slack API token
 
                        
**optional arguments:**

**--help: **show this help message and exit

**--verbose: **Verbose logging of script output

**  --im**: Return private IM messages

**  --mpim  ** :Return private group messages

**  --private-channels ** : Return private channel messages

**  --public-channels  ** : Return public channel messages

**--outfile **: Output response to this file location

** --frequency **: Grab Slack messages from now until this set time in
                        seconds. (Min 3600 - Max 604800) (IE - 3600 will grab
                        the last hours worth of messages)


# Usage from Python module

`slackmon.get_all_messages(token, outfile=None, frequency=None, verbose=False)`

`slackmon.get_im_messages(token, outfile=None, frequency=None, verbose=False)`

`slackmon.get_mpim_messages(token, outfile=None, frequency=None, verbose=False)`

`slackmon.get_private_channel_messages(token, outfile=None, frequency=None, verbose=False)`

`slackmon.get_public_channel_messages(token, outfile=None, frequency=None, verbose=False)`

These methods return messages from specified channels, im's or mpim's (group messages). 

Workspace messages are tied to your Slack web API token. By entering the frequency in seconds, you can return all messages within a given timeframe. For example if you enter 3600 as your frequency (1 hour), you will return all messages within the last hour of calling this method. If left blank the default value  is 1 hour. You can also output response to the console or to an outfile (JSON is only  supported as of now). If you don't specify an outfile, a response will be  returned to your console.

Arguments:
      token {str} -- Slack web API token

   Keyword Arguments:
      outfile {str} -- A path to export your response to. Must be JSON. (default: {None}) 
      
      frequency {int} -- Number of seconds to capture messages from starting now. (default: {None}) 
      
      verbose {bool} -- Prints verbose logging data to screen if set to True (default: {False})

   Returns:
      JSON -- All queried messages formatted in a JSON string.

 **Example:**

>> data = get_all_messages(token='jKdl123Akd=DA', outfile='path/data.json', frequency=3600 )`

>> print(data)

>> {"status": "complete", "data": "Wrote data to path/data.json"}


### Development
Want to contribute? Do it!

