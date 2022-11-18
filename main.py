import traceback
import asyncio
import json
import time
import logging
from web3 import Web3
import requests
from artifacts.abi.presale_abi import presale_contract_abi

bot_chat_id = '-1001795206544'
bot_api_key = '5945276453:AAGww6gRNaOEsTz_aJOt2ru-vuaieQSKF4w'

aclhemy_url = 'https://polygon-mumbai.g.alchemy.com/v2/XXGBKxwudOEfk0lt_F0hICAzFO5b_zt4'
presale_contract_address = '0x70ab9C214818560f6Fd63d9AF9C38cF4D37Fe5A0'

slack_webhook_url = 'https://hooks.slack.com/services/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'

provider_url = 'https://bsc-dataseed.binance.org/'
web3 = Web3(Web3.HTTPProvider(provider_url))

print(web3.isConnected())

contract = web3.eth.contract(address=web3.toChecksumAddress(presale_contract_address), 
                                abi=presale_contract_abi)

logger = logging.getLogger('Ajira_Pay_Presale_Logs')
logger.setLevel(logging.DEBUG)

def log_message_to_slack(message):
    message = str(message)
    try:
        requests.post(url=slack_webhook_url, data=json.dumps({'text': message.replace('@everyone', '<!channel>') + ' '}),
                        headers={'Content-type': 'application/json'})
    except Exception as e:
        logger.error('Error sending message to slack \n ' + traceback.format_exc())


def send_message(message):
        req = 'https://api.telegram.org/bot%s/sendMessage' % (bot_api_key)
        requests.get(req, params={'chat_id': bot_chat_id, 'text': message}, timeout=10)


def handle_new_presale_token_purchase(event):
    try:
        result = json.loads(Web3.toJSON(event))

        tx_hash = result['transactionHash']
        print(tx_hash)

    except Exception as e:
        print(traceback.print_exc())
        log_message_to_slack('@everyone ' + traceback.format_exc())


async def listen_to_new_token_purchase_event(event_filter, poll_interval):
        while True:
            try:
                for Contribute in event_filter.get_new_entries():
                    handle_new_presale_token_purchase(Contribute)
                await asyncio.sleep(poll_interval)

            except asyncio.CancelledError as e:
                print(traceback.print_exc())
                log_message_to_slack('@everyone ' + traceback.format_exc())

            except asyncio.TimeoutError as e:
                print(traceback.print_exc())
                log_message_to_slack('@everyone ' + traceback.format_exc())

            except Exception as e:
                print(traceback.print_exc())
                log_message_to_slack('@everyone ' + traceback.format_exc())


def main():
    print('begin bot...')

    new_ajirap_pay_presale_purchase_event_filter = contract.events.Contribute.createFilter(fromBlock='latest')

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(
            asyncio.gather(
                listen_to_new_token_purchase_event(new_ajirap_pay_presale_purchase_event_filter, 2)
            ))

    except Exception as e:
        print(traceback.print_exc())
        log_message_to_slack('@everyone ' + traceback.format_exc())
    finally:
        loop.close()



if __name__ == '__main__':
    main()