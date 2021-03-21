import datetime as dt
from functools import wraps
import asyncio


def measure_time(func):
	@wraps(func)
	def wrap(*args,**kwargs):
		start = dt.datetime.now()
		func(*args, **kwargs)
		end  = dt.datetime.now()
		print(f'Func {func.__name__} ran for {end-start}')
		return func
	return wrap


def async_measure_time(func):
	@wraps(func)
	async def wrap(*args,**kwargs):
		start = dt.datetime.now()
		result = await func(*args, **kwargs)
		end  = dt.datetime.now()
		print(f'Func {func.__name__} ran for {end-start}')
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
	asyncio.run(main())