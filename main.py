import traceback
import asyncio
import json
import time
import logging
from web3 import Web3
import requests
from datetime import datetime
from artifacts.abi.presale_abi import presale_contract_abi
from dotenv import load_dotenv
import os

load_dotenv()

BOT_CHAT_ID = os.getenv("BOT_CHAT_ID")
BOT_API_KEY = os.getenv("BOT_API_KEY")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

presale_contract_address = '0x70ab9C214818560f6Fd63d9AF9C38cF4D37Fe5A0'

provider_url = 'https://bsc-dataseed.binance.org/'

web3 = Web3(Web3.HTTPProvider(provider_url))

print(web3.isConnected())

contract = web3.eth.contract(address=web3.toChecksumAddress(presale_contract_address), 
                                abi=presale_contract_abi)

logger = logging.getLogger('Ajira_Pay_Presale_Logs')
logger.setLevel(logging.DEBUG)

def get_total_contributions():
    return contract.functions.totalInvestors().call()

def get_total_bnb_contributions():
    wei_val = contract.functions.totalWeiRaised().call()
    amount = web3.fromWei(wei_val,'ether')
    return amount

def get_total_tokens_purchased():
    pass

def log_message_to_slack(message):
    message = str(message)
    try:
        requests.post(url=SLACK_WEBHOOK_URL, data=json.dumps({'text': message.replace('@everyone', '<!channel>') + ' '}),
                        headers={'Content-type': 'application/json'})
    except Exception as e:
        logger.error('Error sending message to slack \n ' + traceback.format_exc())

def send_purchase_message_to_telegram(message):
    try:
        req = 'https://api.telegram.org/bot%s/sendMessage' % (BOT_API_KEY)
        requests.get(req, params={'chat_id': BOT_CHAT_ID, 'text': message}, timeout=10)

    except Exception as e:
        print(traceback.print_exc())
        log_message_to_slack('@everyone ' + traceback.format_exc())

def handle_new_presale_token_purchase(event):
    try:
        result = json.loads(Web3.toJSON(event))

        url = 'https://bscscan.com/tx/%s' % result['transactionHash']
        beneficiary = result['args']['beneficiary']
        bnb_spent = web3.fromWei(result['args']['weiAmount'], 'ether')
        tokens_bought = web3.fromWei(result['args']['tokenAmountBought'], 'ether')
        timestamp = result['args']['timestamp']
        date = datetime.fromtimestamp(timestamp)

        total_bnb_raised = get_total_bnb_contributions()
        presale_link = 'https://portal.ajirapay.finance'

        Flag = {'buy': ' 🔥 🟢'}
        flag = str(Flag['buy'])
        message = flag + 'New $AJP Presale Contribution 🔥:\n \n BNB Spent: %s BNB\n\n $AJP Bought: %s AJP\n\n Contributor: %s\n\n Total Funding Raised: %s BNB \n \n Presale Live At: %s\n\n Date: %s\n\n TxHash: %s\n' %(bnb_spent, tokens_bought, beneficiary, total_bnb_raised, presale_link, date, url)
        send_purchase_message_to_telegram(message)
        print(message)
        return 
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