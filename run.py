import asyncio
import signal
import example

loop = asyncio.get_event_loop()

def stop():
    loop.remove_signal_handler(signal.SIGTERM)
    loop.stop()

loop.add_signal_handler(signal.SIGTERM, stop)

try:
    loop.run_forever()
finally:
    loop.close()
