from py_singleton import singleton
import traceback
import asyncio
from utils.logger import send_error_message_to_slack
from utils.consts import WEB3_CONSTS
from artifacts.abi.presale_abi import presale_contract_abi

import json
import time
from web3 import Web3

infura_rpc = ''
web3 = Web3(Web3.HTTPProvider(infura_rpc))

contract = web3.eth.contract(address=web3.toChecksumAddress(WEB3_CONSTS.presale_contract_address), 
                                abi=presale_contract_abi)

@singleton
class MessageService(object):
    def handle_new_presale_token_purchase(event):
        try:
            result = json.loads(Web3.toJSON(event))

            tx_hash = result['transactionHash']
            print(tx_hash)

        except Exception as e:
            print(traceback.print_exc())
            send_error_message_to_slack('@everyone ' + traceback.format_exc())

    async def listen_to_new_token_purchase_event(event_filter, poll_interval):
        while True:
            try:
                for Contribute in event_filter.get_new_entries():
                    MessageService.handle_new_presale_token_purchase(Contribute)
                await asyncio.sleep(poll_interval)

            except asyncio.CancelledError as e:
                print(traceback.print_exc())
                send_error_message_to_slack('@everyone ' + traceback.format_exc())

            except asyncio.TimeoutError as e:
                print(traceback.print_exc())
                send_error_message_to_slack('@everyone ' + traceback.format_exc())

            except Exception as e:
                print(traceback.print_exc())
                send_error_message_to_slack('@everyone ' + traceback.format_exc())


async def main():
    print('begin bot...')

    new_ajirap_pay_presale_purchase_event_filter = contract.events.Contribute.createFilter(fromBlock='latest')

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(
            asyncio.gather(
                MessageService.listen_to_new_token_purchase_event(new_ajirap_pay_presale_purchase_event_filter, 2)
            ))

    except Exception as e:
        print(traceback.print_exc())
        send_error_message_to_slack('@everyone ' + traceback.format_exc())
    finally:
        loop.close()



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())