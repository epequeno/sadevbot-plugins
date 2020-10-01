from errbot import BotPlugin, botcmd
import logging

log = logging.getLogger(__name__)

try:
    from slack import RTMClient
    from slack import WebClient
    from slack.errors import BotUserAccessError
except ImportError:
    log.exception("Could not start the SlackRTM backend")
    log.fatal(
        "You need to install slackclient in order to use the Slack backend.\n"
        "You can do `pip install errbot[slack-rtm]` to install it."
    )
    sys.exit(1)

class Welcome(BotPlugin):
    """
    """
    def __init__(self):
        pass

    
    @RTMClient.run_on(event="member_joined_channel")
    def hello(**kwargs):
        for i in range(10):
            log.info("hello from welcome bot")
