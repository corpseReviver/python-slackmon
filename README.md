# Slackmon
Slackmon is a Slack channel message retriever. It obtains Slack messages for all channels (public, private, direct, and group) for a specified amount of time for any Workspace.

# Installation
$ pip install slackmon

or from src

$ git clone git@github.com:corpseReviver/python-slackmon.git
$ python python-slackmon/setup.py install

### How to use Slackmon
1) Via the command line

usage: slackmon [-h] [-v] [--im] [--mpim] [--private-channels]
                [--public-channels] -t TOKEN [-o OUTFILE] [-f FREQUENCY]

A Slack channel and private message retriever. Usage: Specifiy your Slack API
token and what message channels you want to return. For example if you want to
return im and mpim messages, use the --im --mpim flags. If you want to return
all messages, do not specifiy any channel flags.

required arguments:
  -t TOKEN, --token TOKEN
                        Slack API token
                        
optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose
  --im                  Return private IM messages
  --mpim                Return private group messages
  --private-channels    Return private channel messages
  --public-channels     Return public channel messages
  -o OUTFILE, --outfile OUTFILE
                        Output response to this file location
  -f FREQUENCY, --frequency FREQUENCY
                        Grab Slack messages from now until this set time in
                        seconds. (Min 3600 - Max 604800) (IE - 3600 will grab
                        the last hours worth of messages)


2) Via the Python module

slackmon.generate_report(slackmon_monitor, data, outfile)

   Writes message data to file or console for consumption.

   Grabs the formatted outfile name (if used) from the slackmon
   object. If an outfile is present, write message data, which is
   passed into this method, to the outfile. If no outfile is present,
   return the JSON data to the caller.

   Arguments:
      slackmon_monitor {object} -- A slackmon monitor object. This is
      used to retrieve messages from channels, private and group IM's.
      data {dict} -- Slack messages formatted in a dictionary.
      outfile {str} -- A path to export your response to. Must be
      JSON. (default: {None})

   Returns:
      dict -- If an outfile is present, response with confirmation of
      file write. If an outfile is not present, respond with a JSON
      data dump of messages.

slackmon.get_all_messages(token, outfile=None, frequency=None, verbose=False)

   [Returns all Slack messages within a given timeframe.

   Retreives all Slack im, mpim, public, and private channel message
   for a  workspace. Workspace messages are tied to your Slack web API
   token. By  entering the frequency in seconds, you can return all
   messages within a  given timeframe. For example if you enter 3600
   as your frequency (1 hour),  you will return all messages within
   the last hour of calling this method.  If left blank the default
   value  is 1 hour. You can also output response to  the console or
   to an outfile (JSON is only supported as of now). If you don't
   specify an outfile, a response will be returned to your console.

   Example: >> data = get_all_messages(token='jKdl123Akd=DA',
         outfile='path/data.json',  frequency=3600 )

      >> print(data) >> {"status": "complete", "data": "Wrote data to
      path/data.json"}

   Arguments:
      token {str} -- Slack web API token

   Keyword Arguments:
      outfile {str} -- A path to export your response to. Must be
      JSON. (default: {None}) frequency {int} -- Number of seconds to
      capture messages from starting now. (default: {None}) verbose
      {bool} -- Prints verbose logging data to screen if set to True
      (default: {False})

   Returns:
      JSON -- All queried messages formatted in a JSON string.

slackmon.get_im_messages(token, outfile=None, frequency=None, verbose=False)

   Returns all Slack IM messages within a given timeframe.

   Retreives all Slack IM message for a workspace. Workspace messages
   are tied to your Slack web API token. By entering the frequency in
   seconds, you can return all messages within a given timeframe. For
   example if you enter 3600 as your frequency (1 hour), you will
   return all messages within the last hour of calling this method. If
   left blank the default value  is 1 hour. You can also output
   response to the console or to an outfile (JSON is only  supported
   as of now). If you don't specify an outfile, a response will be
   returned to your console.

   Example: >> data = get_im_messages(token='jKdl123Akd=DA',
         outfile='path/data.json',  frequency=3600 )

      >> print(data) >> {"status": "complete", "data": "Wrote data to
      path/data.json"}

   Arguments:
      token {str} -- Slack web API token

   Keyword Arguments:
      outfile {str} -- A path to export your response to. Must be
      JSON. (default: {None}) frequency {int} -- Number of seconds to
      capture messages from starting now. (default: {None}) verbose
      {bool} -- Prints verbose logging data to screen if set to True
      (default: {False})

   Returns:
      JSON -- All queried messages formatted in a JSON string.

slackmon.get_mpim_messages(token, outfile=None, frequency=None, verbose=False)

   Returns all Slack MPIM messages within a given timeframe.

   Retreives all Slack IM message for a workspace. Workspace messages
   are tied to your Slack web API token. By entering the frequency in
   seconds, you can return all messages within a given timeframe. For
   example if you enter 3600 as your frequency (1 hour), you will
   return all messages within the last hour of calling this method. If
   left blank the default value  is 1 hour. You can also output
   response to the console or to an outfile (JSON is only  supported
   as of now). If you don't specify an outfile, a response will be
   returned to your console.

   Example: >> data = get_mpim_messages(token='jKdl123Akd=DA',
         outfile='path/data.json',  frequency=3600 )

      >> print(data) >> {"status": "complete", "data": "Wrote data to
      path/data.json"}

   Arguments:
      token {str} -- Slack web API token

   Keyword Arguments:
      outfile {str} -- A path to export your response to. Must be
      JSON. (default: {None}) frequency {int} -- Number of seconds to
      capture messages from starting now. (default: {None}) verbose
      {bool} -- Prints verbose logging data to screen if set to True
      (default: {False})

   Returns:
      JSON -- All queried messages formatted in a JSON string.

slackmon.get_private_channel_messages(token, outfile=None, frequency=None, verbose=False)

   Returns all Slack private channel messages within a given
   timeframe.

   Retreives all Slack private channel message for a workspace.
   Workspace messages are tied to your Slack web API token. By
   entering the frequency in seconds, you can return all messages
   within a given timeframe. For example if you enter 3600 as your
   frequency (1 hour), you will return all messages within the last
   hour of calling this method. If left blank the default value  is 1
   hour. You can also output response to the console or to an outfile
   (JSON is only  supported as of now). If you don't specify an
   outfile, a response will be  returned to your console.

   Example: >> data =
   get_private_channel_messages(token='jKdl123Akd=DA',
         outfile='path/data.json',  frequency=3600 )

      >> print(data) >> {"status": "complete", "data": "Wrote data to
      path/data.json"}

   Arguments:
      token {str} -- Slack web API token

   Keyword Arguments:
      outfile {str} -- A path to export your response to. Must be
      JSON. (default: {None}) frequency {int} -- Number of seconds to
      capture messages from starting now. (default: {None}) verbose
      {bool} -- Prints verbose logging data to screen if set to True
      (default: {False})

   Returns:
      JSON -- All queried messages formatted in a JSON string.

slackmon.get_public_channel_messages(token, outfile=None, frequency=None, verbose=False)

   Returns all Slack public channel messages within a given timeframe.

   Retreives all Slack public channel message for a workspace.
   Workspace messages are tied to your Slack web API token. By
   entering the frequency in seconds, you can return all messages
   within a given timeframe. For example if you enter 3600 as your
   frequency (1 hour), you will return all messages within the last
   hour of calling this method. If left blank the default value  is 1
   hour. You can also output response to the console or to an outfile
   (JSON is only  supported as of now). If you don't specify an
   outfile, a response will be  returned to your console.

   Example: >> data =
   get_public_channel_messages(token='jKdl123Akd=DA',
         outfile='path/data.json',  frequency=3600 )

      >> print(data) >> {"status": "complete", "data": "Wrote data to
      path/data.json"}

   Arguments:
      token {str} -- Slack web API token

   Keyword Arguments:
      outfile {str} -- A path to export your response to. Must be
      JSON. (default: {None}) frequency {int} -- Number of seconds to
      capture messages from starting now. (default: {None}) verbose
      {bool} -- Prints verbose logging data to screen if set to True
      (default: {False})

   Returns:
      JSON -- All queried messages formatted in a JSON string.

### Development
Want to contribute? Do it!

