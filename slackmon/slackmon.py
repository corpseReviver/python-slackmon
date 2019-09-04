"""A Slack channel message retriever.

This script obtains Slack messages for all channels
(public, private, direct, and group) for a specified amount
of time for a Workspace.
"""

from slackmon.monitor import Monitor
import json


def get_im_messages(token, outfile=None, frequency=None, verbose=False):
    """Returns all Slack IM messages within a given timeframe.

    Retreives all Slack IM message for a workspace. Workspace messages
    are tied to your Slack web API token. By entering the frequency in
    seconds, you can return all messages within a given timeframe. For example
    if you enter 3600 as your frequency (1 hour), you will return all messages
    within the last hour of calling this method. If left blank the default value 
    is 1 hour. You can also output response to the console or to an outfile (JSON is only 
    supported as of now). If you don't specify an outfile, a response will be 
    returned to your console.

    Example: >> data = get_im_messages(token='jKdl123Akd=DA', 
                             outfile='path/data.json', 
                             frequency=3600
                             )
            >> print(data)
            >> {"status": "complete", "data": "Wrote data to path/data.json"}

    Arguments:
        token {str} -- Slack web API token

    Keyword Arguments:
        outfile {str} -- A path to export your response to. Must be JSON. (default: {None})
        frequency {int} -- Number of seconds to capture messages from starting now. (default: {None})
        verbose {bool} -- Prints verbose logging data to screen if set to True (default: {False})

    Returns:
        JSON -- All queried messages formatted in a JSON string.

    """

    # Create monitor and validate arguments
    slackmon_monitor = setup_monitor(token, outfile, frequency, verbose)

    # Create dictionaries of messages per channel
    data = slackmon_monitor.get_im_messages()

    return generate_report(slackmon_monitor, data, outfile)


def get_mpim_messages(token, outfile=None, frequency=None, verbose=False):
    """Returns all Slack MPIM messages within a given timeframe.

    Retreives all Slack IM message for a workspace. Workspace messages
    are tied to your Slack web API token. By entering the frequency in
    seconds, you can return all messages within a given timeframe. For example
    if you enter 3600 as your frequency (1 hour), you will return all messages
    within the last hour of calling this method. If left blank the default value 
    is 1 hour. You can also output response to the console or to an outfile (JSON is only 
    supported as of now). If you don't specify an outfile, a response will be 
    returned to your console.

    Example: >> data = get_mpim_messages(token='jKdl123Akd=DA', 
                             outfile='path/data.json', 
                             frequency=3600
                             )
            >> print(data)
            >> {"status": "complete", "data": "Wrote data to path/data.json"}

    Arguments:
        token {str} -- Slack web API token

    Keyword Arguments:
        outfile {str} -- A path to export your response to. Must be JSON. (default: {None})
        frequency {int} -- Number of seconds to capture messages from starting now. (default: {None})
        verbose {bool} -- Prints verbose logging data to screen if set to True (default: {False})

    Returns:
        JSON -- All queried messages formatted in a JSON string.

    """

    # Create monitor and validate arguments
    slackmon_monitor = setup_monitor(token, outfile, frequency, verbose)

    # Create a dictionary of messages per channel
    data = slackmon_monitor.get_mpim_messages()

    return generate_report(slackmon_monitor, data, outfile)


def get_public_channel_messages(token, outfile=None, frequency=None, verbose=False):
    """Returns all Slack public channel messages within a given timeframe.

    Retreives all Slack public channel message for a workspace. Workspace messages
    are tied to your Slack web API token. By entering the frequency in
    seconds, you can return all messages within a given timeframe. For example
    if you enter 3600 as your frequency (1 hour), you will return all messages
    within the last hour of calling this method. If left blank the default value 
    is 1 hour. You can also output response to the console or to an outfile (JSON is only 
    supported as of now). If you don't specify an outfile, a response will be 
    returned to your console.

    Example: >> data = get_public_channel_messages(token='jKdl123Akd=DA', 
                             outfile='path/data.json', 
                             frequency=3600
                             )
            >> print(data)
            >> {"status": "complete", "data": "Wrote data to path/data.json"}

    Arguments:
        token {str} -- Slack web API token

    Keyword Arguments:
        outfile {str} -- A path to export your response to. Must be JSON. (default: {None})
        frequency {int} -- Number of seconds to capture messages from starting now. (default: {None})
        verbose {bool} -- Prints verbose logging data to screen if set to True (default: {False})

    Returns:
        JSON -- All queried messages formatted in a JSON string.

    """

    # Create monitor and validate arguments
    slackmon_monitor = setup_monitor(token, outfile, frequency, verbose)

    # Create a dictionary of messages per channel
    data = slackmon_monitor.get_public_channel_messages()

    return generate_report(slackmon_monitor, data, outfile)


def get_private_channel_messages(token, outfile=None, frequency=None, verbose=False):
    """Returns all Slack private channel messages within a given timeframe.

    Retreives all Slack private channel message for a workspace. Workspace messages
    are tied to your Slack web API token. By entering the frequency in
    seconds, you can return all messages within a given timeframe. For example
    if you enter 3600 as your frequency (1 hour), you will return all messages
    within the last hour of calling this method. If left blank the default value 
    is 1 hour. You can also output response to the console or to an outfile (JSON is only 
    supported as of now). If you don't specify an outfile, a response will be 
    returned to your console.

    Example: >> data = get_private_channel_messages(token='jKdl123Akd=DA', 
                             outfile='path/data.json', 
                             frequency=3600
                             )
            >> print(data)
            >> {"status": "complete", "data": "Wrote data to path/data.json"}

    Arguments:
        token {str} -- Slack web API token

    Keyword Arguments:
        outfile {str} -- A path to export your response to. Must be JSON. (default: {None})
        frequency {int} -- Number of seconds to capture messages from starting now. (default: {None})
        verbose {bool} -- Prints verbose logging data to screen if set to True (default: {False})

    Returns:
        JSON -- All queried messages formatted in a JSON string.

    """

    # Create monitor and validate arguments
    slackmon_monitor = setup_monitor(token, outfile, frequency, verbose)

    # Create a dictionary of messages per channel
    data = slackmon_monitor.get_public_channel_messages()

    return generate_report(slackmon_monitor, data, outfile)


def get_all_messages(token, outfile=None, frequency=None, verbose=False):
    """[Returns all Slack messages within a given timeframe.

    Retreives all Slack im, mpim, public, and private channel message for a 
    workspace. Workspace messages are tied to your Slack web API token. By 
    entering the frequency in seconds, you can return all messages within a 
    given timeframe. For example if you enter 3600 as your frequency (1 hour), 
    you will return all messages within the last hour of calling this method. 
    If left blank the default value  is 1 hour. You can also output response to 
    the console or to an outfile (JSON is only supported as of now). If you don't 
    specify an outfile, a response will be returned to your console.

    Example: >> data = get_all_messages(token='jKdl123Akd=DA', 
                             outfile='path/data.json', 
                             frequency=3600
                             )
            >> print(data)
            >> {"status": "complete", "data": "Wrote data to path/data.json"}

    Arguments:
        token {str} -- Slack web API token

    Keyword Arguments:
        outfile {str} -- A path to export your response to. Must be JSON. (default: {None})
        frequency {int} -- Number of seconds to capture messages from starting now. (default: {None})
        verbose {bool} -- Prints verbose logging data to screen if set to True (default: {False})

    Returns:
        JSON -- All queried messages formatted in a JSON string.

    """

    # Create monitor and validate arguments
    slackmon_monitor = setup_monitor(token, outfile, frequency, verbose)

    # Create a concatinated dictionary of messages per channel
    data = {}
    public_channel_messages = slackmon_monitor.get_public_channel_messages()
    private_channel_messages = slackmon_monitor.get_private_channel_messages()
    im_messages = slackmon_monitor.get_im_messages()
    mpim_messages = slackmon_monitor.get_mpim_messages()
    data["im_messages"] = im_messages
    data["mpim_messages"] = mpim_messages
    data["private_channel_messages"] = private_channel_messages
    data["public_channel_messages"] = public_channel_messages

    return generate_report(slackmon_monitor, data, outfile)


def setup_monitor(token, outfile, frequency, verbose):
    """Creates and starts slackmon monitor. 

    Checks to see if a Slack web API token has been passed as an 
    argument and raised an Exception if not. Creates a slackmon
    monitor and performs validation checks on argument data.

    Arguments:
        token {str} -- Slack web API token
        outfile {str} -- A path to export your response to. Must be JSON. (default: {None})
        frequency {int} -- Number of seconds to capture messages from starting now. (default: {None})
        verbose {bool} -- Prints verbose logging data to screen if set to True (default: {False})

    Returns:
        [object] -- A slackmon monitor object. This is used to retrieve messages
        from channels, private and group IM's. 

    Raises:
        Exception -- Raised if no Slack web API token is passed into method. 

    """

    if not token:
        raise Exception('A Slack API token is required.')

    # Create slackmon monitor
    slackmon_monitor = Monitor(token, outfile, frequency, verbose)

    # Gets the slack client, tests for connectivity to
    # Slack and validates arguments.
    slackmon_monitor.start_monitor()

    return slackmon_monitor


def generate_report(slackmon_monitor, data, outfile):
    """Writes message data to file or console for consumption. 

    Grabs the formatted outfile name (if used) from the slackmon object.
    If an outfile is present, write message data, which is passed
    into this method, to the outfile. If no outfile is present, return
    the JSON data to the caller.

    Arguments:
        slackmon_monitor {object} -- A slackmon monitor object. This is used to retrieve messages
        from channels, private and group IM's. 
        data {dict} -- Slack messages formatted in a dictionary. 
        outfile {str} -- A path to export your response to. Must be JSON. (default: {None})

    Returns:
        dict -- If an outfile is present, response with confirmation of file write. If an outfile
        is not present, respond with a JSON data dump of messages. 
        
    """

    if outfile:
        outfile = slackmon_monitor.get_formatted_outfile()
        try:
            with open(outfile, "w") as f:
                f.write(json.dumps(data))
            return {"status": "complete", "data": "Wrote data to {}".format(outfile)}
        except Exception as e:
            return {"status": "error:: unable to write data to file, dumping instead.", "data": json.dumps(data)}
    else:
        return json.dumps(data)
