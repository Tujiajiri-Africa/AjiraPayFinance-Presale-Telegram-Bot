import logging
from py_singleton import singleton
import requests
import json
import traceback
from utils.consts import SLACK_CONSTS

logger = logging.getLogger('Ajira_Pay_Presale_Logs')
logger.setLevel(logging.DEBUG)
        
@singleton
class SLACK_LOGGER(object):
    @staticmethod
    def log_message_to_slack(message):
        message = str(message)
        try:
            requests.post(url=SLACK_CONSTS.slack_webhook_url, data=json.dumps({'text': message.replace('@everyone', '<!channel>') + ' '}),
                          headers={'Content-type': 'application/json'})
        except Exception as e:
            logger.error('Error sending message to slack \n ' + traceback.format_exc())