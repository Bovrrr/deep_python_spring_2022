import cffi

import utils

def ABI():
    # ABI
    print("===== ABI =====")
    ffi = cffi.FFI()
    lib = ffi.dlopen('./libarea.so')
    ffi.cdef('''
    struct Point {
        int x;
        int y;
    };

    int area(struct Point *p1, struct Point *p2);
    int fibonacci(int n);
    ''')

    p1 = ffi.new('struct Point *')
    p2 = ffi.new('struct Point *')
    p1.x, p1.y = (10, 10)
    p2.x, p2.y = (0, 0)

    area = lib.area(p1, p2)
    print(f"Area of point {p1}, {p2} is {area}")
    s1 = ffi.new('char []', b'hello kitty')
    print(s1)
    print([lib.fibonacci(n) for n in range(10)])

def API():
    print("===== API =====")
    print([utils.lib.fibonacci(n) for n in range(10)])

def main():
    ABI()
    API()

if __name__ == "__main__":
    main()
