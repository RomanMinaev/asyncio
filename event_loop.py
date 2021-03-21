import datetime as dt
from functools import wraps
import asyncio


def async_measure_time(func):
	@wraps(func)
	async def wrap(*args,**kwargs):
		start = dt.datetime.now()
		result = await func(*args, **kwargs)
		end  = dt.datetime.now()
		print(f'Func {func.__name__} ran for {end-start}.')
		return result
	return wrap

async def tick():
	print('Tick')
	await asyncio.sleep(1)
	print('Tock')


@async_measure_time
async def main():
	await asyncio.gather(tick(), tick(), tick())


if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	try:
		#loop.create_task(main())
		#loop.run_forever()
		#loop.run_until_complete(main())
		asyncio.run(main())
		print(f'Coroutines have finished')
	#except KeyboardInterrupt:
		#print('Manually killed loop')
	finally:
		loop.close()
		print(f'Loop is closed = {loop.is_closed()}')