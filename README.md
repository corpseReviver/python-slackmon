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

### Development
Want to contribute? Do it!

