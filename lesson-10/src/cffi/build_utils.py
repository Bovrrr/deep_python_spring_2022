import cffi

def main():
    ffibuilder = cffi.FFI()
    ffibuilder.cdef('''
    int fibonacci(int n);
    ''')

    ffibuilder.set_source('utils',
    r'''
    int fibonacci(int n)
    {
        if (n < 2)
            return 1;
        return fibonacci(n-2) + fibonacci(n-1);
    }
    ''')
    ffibuilder.compile()

if __name__ == "__main__":
    main()
