import ctypes

def libc():
    print("======= Libc =======")
    libc = ctypes.CDLL('libc.so.6')
    #dir(libc)
    #['_FuncPtr', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_func_flags_', '_func_restype_', '_handle', '_name']
#char * strstr(const char *text, con

    libc.strstr.restype = ctypes.c_char_p
    libc.strstr.argstype = [ctypes.c_char_p, ctypes.c_char_p]

    res = libc.strstr(b"ababac", b"baba")
    print(res)

def mylibc():
    print("======= MyLibC =======")
    lib = ctypes.CDLL('./libutils.so')
    lib.func1.argstype = [ctypes.c_int,]
    for num in range(10):
        print(lib.func1(num))

    s = b"cat"
    lib.func2.argstype = [ctypes.c_char_p, ctypes.c_int]
    lib.func2(s, len(s))
    pass

def mylibcpp():
    print("======= MyLibCpp =======")
    lib = ctypes.CDLL('./libutilscpp.so')
    lib.int2str.restype = ctypes.c_char_p
    lib.int2str.argstype = [ctypes.c_int,]
    dup_str = lib.int2str(100500)
    print(dup_str)

def main():
    libc()
    mylibc()
    mylibcpp()

if __name__ == "__main__":
    main()
