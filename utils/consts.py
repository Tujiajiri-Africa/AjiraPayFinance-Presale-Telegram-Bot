from py_singleton import singleton

@singleton
class WEB3_CONSTS(object):
    aclhemy_url = 'https://polygon-mumbai.g.alchemy.com/v2/XXGBKxwudOEfk0lt_F0hICAzFO5b_zt4'
    presale_contract_address = '0x70ab9C214818560f6Fd63d9AF9C38cF4D37Fe5A0'

class SLACK_CONSTS(object):
    slack_webhook_url = 'https://hooks.slack.com/services/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'

class TG_CONSTS(object):
    bot_chat_id = '-1001795206544'
    bot_api_key = '5945276453:AAGww6gRNaOEsTz_aJOt2ru-vuaieQSKF4w'