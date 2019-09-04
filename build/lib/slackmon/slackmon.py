"""A Slack channel message retriever.

This script obtains Slack messages for all channels
(public, private, direct, and group) for a specified amount
of time for a Workspace.
"""

from slackmon.monitor import Monitor


def create_monitor(token:str=None, outfile:str=None, frequency:int=None, 
        verbose:bool=False) -> object:
    """Create a slackmon monitor object.

    Use this function when importing this module from another program. 

    Keyword Arguments:
        token {str} -- Slack API token (default: {None})
        outfile {str} -- Output response to this file location (default: {None})
        frequency {int} -- Grab Slack messages from now until this set time in
                        seconds. (default: {None})
        verbose {bool} -- Prints verbose text if set to True (default: {False})

    Returns:
        object -- A slackmon monitor object used to get messages.

    Raises:
        Exception -- Raises this exception if a Slack API token is not set. 
    """

    if not token:
        raise Exception('A Slack API token is required to create a monitor.')

    return Monitor(token, outfile=outfile, frequency=frequency, verbose=verbose)

