import argparse
import json
from slackmon.monitor import Monitor


def main():
    # Create parameters from argparse arguments.
    args = create_argparser()

    # Create slackmon monitor
    slackmon_monitor = Monitor(
        args.token, args.outfile, args.frequency, args.verbose)

    # Start slackmon monitor which creates Slack clients.
    slackmon_monitor.start_monitor()

    # Create dictionary of messages per channel
    im_messages, mpim_messages, private_channel_messages, public_channel_messages = get_messages(
        slackmon_monitor)

    outfile = slackmon_monitor.get_formatted_outfile()

    # Creates message report in JSON format. Will print to console or to a file depending on argument specification.
    generate_report(im_messages, mpim_messages,
                    private_channel_messages, public_channel_messages, args, outfile)


def create_argparser() -> object:
    """Create parameters from argparse arguments. 

    See --help function or help strings below to view argument descriptions. 

    Returns:
        [argparge object] -- To obtain value use args.[key]. IE print(args.token)
    """
    parser = argparse.ArgumentParser(
        description="A Slack channel and private message retriever. Usage: Specifiy your Slack API \
        token and what message channels you want to return. For example if you want to return im and \
        mpim messages, use the --im --mpim flags. If you want to return all messages, do not specifiy \
        any channel flags.")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument(
        "--im", help="Return private IM messages", action="store_true")
    parser.add_argument(
        "--mpim", help="Return private group messages", action="store_true")
    parser.add_argument(
        "--private-channels", help="Return private channel messages", action="store_true")
    parser.add_argument(
        "--public-channels", help="Return public channel messages", action="store_true")
    parser.add_argument("-t", "--token", type=str,
                        help="Slack API token", required=True)
    parser.add_argument("-o", "--outfile", type=str,
                        help="Output response to this file location")
    parser.add_argument("-f", "--frequency", type=int,
                        help="Grab Slack messages from now until this set time in seconds. (Min 3600 - Max 604800) (IE - 3600 \
                        will grab the last hours worth of messages)")
    args = parser.parse_args()

    return args


def get_messages(slackmon_monitor: object) -> tuple:
    """Create dictionary of messages per channel 

    Arguments:
        slackmon_monitor {object} -- A slackmon monitor object used to get messages. 

    Returns:
        tuple -- dictionary of im, mpim, private, and public channel messages in this order. 
    """
    im_messages = slackmon_monitor.get_im_messages()
    mpim_messages = slackmon_monitor.get_mpim_messages()
    private_channel_messages = slackmon_monitor.get_private_channel_messages()
    public_channel_messages = slackmon_monitor.get_public_channel_messages()

    return im_messages, mpim_messages, private_channel_messages, public_channel_messages


def generate_report(im_messages: dict, mpim_messages: dict, private_channel_messages: dict, 
        public_channel_messages: dict, args:object, outfile:str) -> None:
    """Creates message report in JSON format.

     Will print to console or to a file depending on argument specification. This function also
     counts the number of messages returned per channel. Client specifies to return all messages
     by not specifying --im, --mpim, --private-channels, --public-channels flags, or specific
     flags to return those messages. 

    Arguments:
        im_messages {dict} -- Dictionary of IM messages
        mpim_messages {dict} -- Dictionary of MPIM messages
        private_channel_messages {dict} -- Dictionary of private channel messages
        public_channel_messages {dict} -- Dictionary of public channel messages
        outfile {str} - Formatted output file for report.
        args {object} -- To obtain value use args.[key]. IE print(args.token)
    """

    # Init empty dictionary to use for return data.
    data = {}

    if args.im:
        data["im_messages"] = im_messages

    if args.mpim:
        data["mpim_messages"] = mpim_messages

    if args.private_channels:
        data["private_channel_messages"] = private_channel_messages

    if args.public_channels:
        data["public_channel_messages"] = public_channel_messages

    if not data:
        data["im_messages"] = im_messages
        data["mpim_messages"] = mpim_messages
        data["private_channel_messages"] = private_channel_messages
        data["public_channel_messages"] = public_channel_messages

    if outfile:
        with open(outfile, "w") as f:
            f.write(json.dumps(data))
        print('--> Wrote data to {}'.format(outfile))
    else:
        print(json.dumps(data))


if __name__ == "__main__":
    main()

