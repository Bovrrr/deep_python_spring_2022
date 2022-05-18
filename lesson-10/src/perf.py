import time
import ctypes

import cffi

import utils

def fibonacci(n):
    if n < 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

MAX_LEN = 35

def main():
    start_ts = time.time()
    res_py = [fibonacci(n) for n in range(MAX_LEN)]
    end_ts = time.time()
    print(f"Time of execution of python fibonacci is {end_ts - start_ts} seconds")


    lib = ctypes.CDLL('./ctypes/libutilscpp.so')
    lib.fibonacci.argstype = [ctypes.c_int,]
    start_ts = time.time()
    res_py = [lib.fibonacci(n) for n in range(MAX_LEN)]
    end_ts = time.time()
    print(f"Time of execution of cpp fibonacci is {end_ts - start_ts} seconds")


    # ABI
    ffi = cffi.FFI()
    lib = ffi.dlopen('./cffi/libarea.so')
    ffi.cdef('''
    int fibonacci(int n);
    ''')

    start_ts = time.time()
    res_cffi = [lib.fibonacci(n) for n in range(MAX_LEN)]
    end_ts = time.time()
    print(f"Time of execution of cffi fibonacci is {end_ts - start_ts} seconds")

    start_ts = time.time()
    res_py = [utils.fibonacci(n) for n in range(MAX_LEN)]
    end_ts = time.time()
    print(f"Time of execution of c-extentions fibonacci is {end_ts - start_ts} seconds")

if __name__ == "__main__":
    main()
