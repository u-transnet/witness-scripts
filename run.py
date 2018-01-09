import asyncio
import example

loop = asyncio.get_event_loop()

try:
	loop.run_forever()

finally:
    loop.close()
