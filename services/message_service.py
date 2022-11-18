from py_singleton import singleton
import traceback
import asyncio
from utils.logger import send_error_message_to_slack

@singleton
class MessageService(object):
    pass

    def handle_new_presale_token_purchase(event):
        pass

    async def listen_to_new_trade_position_event(event_filter, poll_interval):
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
