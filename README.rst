# Slackmon
Slackmon is a Slack channel message retriever. It obtains Slack messages for all channels (public, private, direct, and group) for a specified amount of time for any Workspace.

# Installation
$ pip install slackmon
or
$ git clone git@github.com:corpseReviver/python-slackmon.git
$ python python-slackmon/setup.py install

### How to use it
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
  '', --im                  Return private IM messages
  '', --mpim                Return private group messages
  '', --private-channels    Return private channel messages
  '',m --public-channels     Return public channel messages
  -o OUTFILE, --outfile OUTFILE
                        Output response to this file location
  -f FREQUENCY, --frequency FREQUENCY
                        Grab Slack messages from now until this set time in
                        seconds. (Min 3600 - Max 604800) (IE - 3600 will grab
                        the last hours worth of messages)


### Development
Want to contribute? Do it!

