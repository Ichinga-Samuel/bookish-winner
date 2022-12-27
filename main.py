# import logging

from tests.check import mainc, fun

fmt = "%(asctime)s %(message)s %(one)s %(two)s"
# logging.basicConfig(filename='example.log', format=fmt)

fun()
mainc()
class Cacheable:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        self.cache = {}

    def key(self, *args, **kwargs):
        return ''.join(str(i) for i in args) + ''.join(str(i) for i in kwargs.items())

    def __call__(self, fun):
        @functools.wraps(fun)
        async def wrapper(*args, **kwargs):
            key = self.key(*args, **kwargs)
            print(self.cache.get(key))
            self.cache[key] = self.cache.get(key) or await fun(*args, **kwargs)
            return self.cache[key]
        return wrapper


@Cacheable()
async def check(a, b):
    await asyncio.sleep(5)
    return a+b


async def main():
    b = await check(5, 7)
    v = await check(5, 7)
    v = await check(5, 7)

asyncio.run(main())
# b = Cacheable(fn=check, b=6)