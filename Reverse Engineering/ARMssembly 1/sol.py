from pwn import *

for i in range(10000):
    s=['chall_1',str(i)]
    r=process(s)
    if b'win' in r.recvline():
        print(i)
        break
    r.kill()
