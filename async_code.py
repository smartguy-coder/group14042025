# from time import sleep
import asyncio
from asyncio import sleep, gather


# def foo1():
#     print("foo1 start")
#     sleep(1)
#     print("foo1 end")
#
#
# def foo2():
#     print("foo2 start")
#     sleep(1)
#     print("foo2 end")
#
#
# foo1()
# foo2()


async def foo1():
    print("foo1 start")
    await sleep(1)
    print("foo1 end")


async def foo2():
    print("foo2 start")
    await sleep(1)
    print("foo2 end")


async def main():
    await gather(
        foo1(),
        foo2(),
        foo2(),
        foo2(),
        foo2(),
        foo2(),
        foo2(),
        foo2(),
        foo2(),
        foo2(),
        foo2(),
        foo2(),
        foo2(),
        foo2(),
        foo2(),
        foo2(),
    )


asyncio.run(main())
