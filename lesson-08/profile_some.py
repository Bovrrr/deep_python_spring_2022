# import cProfile, pstats, io

from memory_profiler import profile


def fib(n):
    if n < 2:
        return 1

    return fib(n - 1) + fib(n - 2)


def time_sleep():
    import time
    time.sleep(0.5)

    fib(30)

    time.sleep(0.5)


class PointOrdinal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 3


class PointSlot:
    __slots__ = ("x", "y", "z", "s")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 3



@profile
def mem_stat():
    lst1 = [PointOrdinal(5, 5) for i in range(100_000)]
    lst2 = [PointSlot(5, 5) for i in range(100_000)]
    print("xxx")



if __name__ == "__main__":
    # time_sleep()
    mem_stat()


# pr = cProfile.Profile()
# pr.enable()
#
# time_sleep()
#
# pr.disable()
#
#
# out = io.StringIO()
# # sortby =
# ps = pstats.Stats(pr, stream=out)
# ps.print_stats()
#
# print(out.getvalue())
