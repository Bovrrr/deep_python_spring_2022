import mmap
import os
import time


m = mmap.mmap(-1, 13)
m.write(b"hello world")


pid = os.fork()

if pid == 0:
    m.seek(0)
    print("child", m.read())
    m[4:10] = b"123456"
else:
    print("parent")
    time.sleep(1)
    m.seek(0)
    print("par", m.read())

