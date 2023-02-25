import traceback
import asyncio
import json
import time
import logging
from web3 import Web3
import requests
from datetime import datetime
from artifacts.abi.presale_abi import presale_contract_abi
from artifacts.abi.v2_presale_abi import v2_abi
from artifacts.abi.stablecoin_presale_abi import stable_coin_presale_contract_abi
from dotenv import load_dotenv
import os

load_dotenv()

BOT_CHAT_ID = os.getenv("BOT_CHAT_ID")
BOT_API_KEY = os.getenv("BOT_API_KEY")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

presale_contract_address = '0x70ab9C214818560f6Fd63d9AF9C38cF4D37Fe5A0'
presale_v2_contract_address = '0x4A7c5A4EfB90D3CBD1C3c25b775b822EBA600081'
stablcoin_presale_contract_address = '0x1dd6f0610B42f09048913B525B112d6984452E5C'

DAI = "0x1AF3F329e8BE154074D8769D1FFa4eE058B1DBc3"
BUSD = "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56"
USDT = "0x55d398326f99059fF775485246999027B3197955"
USDC = "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d"

provider_url = 'https://bsc-dataseed.binance.org/'

web3 = Web3(Web3.HTTPProvider(provider_url))

print(web3.isConnected())

v1_contract = web3.eth.contract(address=web3.toChecksumAddress(presale_contract_address), 
                                abi=presale_contract_abi)

v2_contract = web3.eth.contract(address=web3.toChecksumAddress(presale_v2_contract_address), 
                                abi=v2_abi)

stable_coin_presale_contract = web3.eth.contract(address=web3.toChecksumAddress(stablcoin_presale_contract_address),
                                abi=stable_coin_presale_contract_abi)

total_usd_raised = web3.fromWei(stable_coin_presale_contract.functions.totalUsdRaised().call(),'ether')
#print(total_usd_raised)

logger = logging.getLogger('Ajira_Pay_Presale_Logs')
logger.setLevel(logging.DEBUG)

def get_stable_coin_name_from_contract_address(contract_address):
    _str_contract = str(contract_address).lower()
    try:
        if _str_contract == DAI.lower():
            return 'DAI'
        elif _str_contract == BUSD.lower():
            return 'BUSD'
        elif _str_contract == USDT.lower():
            return 'USDT'
        else:
            return 'USDC'
            
    except Exception as e:
        print(traceback.print_exc())
        log_message_to_slack('@everyone ' + traceback.format_exc())

def get_total_contributions():
    return v2_contract.functions.totalInvestors().call()

def get_total_bnb_contributions():
    wei_val = v2_contract.functions.totalWeiRaised().call()
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

def send_discord_notification(message):
    try:
        params = {"content": message}
        response = requests.post(DISCORD_WEBHOOK_URL, json=params)
        print(response.status_code)
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
        send_discord_notification(message)
        print(message)
        print("Total USD Raised: ", total_usd_raised)
        return 
    except Exception as e:
        print(traceback.print_exc())
        log_message_to_slack('@everyone ' + traceback.format_exc())

def handle_new_presale_stable_coin_token_purchase(event):
    try:
        result = json.loads(Web3.toJSON(event))

        url = 'https://bscscan.com/tx/%s' % result['transactionHash']
        beneficiary = result['args']['investor']
        stable_coin = get_stable_coin_name_from_contract_address(result['args']['stableCoin'])
        stable_coin_spent = web3.fromWei(result['args']['stableCoinAmount'], 'ether')
        tokens_bought = web3.fromWei(result['args']['tokensBought'], 'ether')
        timestamp = result['args']['timestamp']
        date = datetime.fromtimestamp(timestamp)
        
        presale_link = 'https://portal.ajirapay.finance'

        Flag = {'buy': ' 🔥 🟢'}
        flag = str(Flag['buy'])
        message = flag + 'New $AJP Presale Contribution 🔥:\n \n %s Spent: %s %s\n\n $AJP Bought: %s AJP\n\n Contributor: %s\n \n Presale Live At: %s\n\n Date: %s\n\n TxHash: %s\n' %(
            stable_coin, stable_coin_spent, stable_coin, tokens_bought, beneficiary, presale_link, date, url)
        send_purchase_message_to_telegram(message)
        send_discord_notification(message)
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

async def listen_to_new_stable_coin_token_purchase_event(event_filter, poll_interval):
        while True:
            try:
                for BuyWithStableCoin in event_filter.get_new_entries():
                    handle_new_presale_stable_coin_token_purchase(BuyWithStableCoin)
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
    print('Listening to new presale contributions event...')

    new_ajira_pay_finance_presale_purchase_event_filter = v2_contract.events.Contribute.createFilter(fromBlock='latest')
    new_ajira_pay_finance_stable_coin_presale_purchase_event_filter = stable_coin_presale_contract.events.BuyWithStableCoin.createFilter(fromBlock='latest')

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(
            asyncio.gather(
                listen_to_new_token_purchase_event(new_ajira_pay_finance_presale_purchase_event_filter, 2),
                listen_to_new_stable_coin_token_purchase_event(new_ajira_pay_finance_stable_coin_presale_purchase_event_filter, 2)
            ))

    except Exception as e:
        print(traceback.print_exc())
        log_message_to_slack('@everyone ' + traceback.format_exc())
    finally:
        loop.close()


if __name__ == '__main__':
    main()