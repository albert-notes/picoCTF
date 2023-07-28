from pwn import *
import string

r=remote('mercury.picoctf.net',4572)
r.recvuntil(': ')
flag_ct=r.recvline().strip().decode()
r.recvline()
r.recvline()

def enc(s):
    r.sendlineafter(': ',s)
    r.recvuntil(': ')
    return r.recvline().strip().decode()

def gp(prefix,c,dt):
    s=enc(prefix+c)
    for k in dt.keys():
        s=s.replace(k,"")
    return s

dt={}
known='picoCTF{'
flag=""

for c in known:
    rp=gp(flag,c,dt)
    dt[rp]=c
    flag+=c
    flag_ct=flag_ct.replace(rp,"")

ch="_}"+string.digits+string.ascii_lowercase+string.ascii_uppercase

while not flag.endswith('}'):
    for c in ch:
        rp=gp(flag,c,dt)
        if rp not in flag_ct:
            continue
        dt[rp]=c
        flag+=c
        flag_ct=flag_ct.replace(rp,"")
        print(flag)
        break
