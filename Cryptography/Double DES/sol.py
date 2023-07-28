from Crypto.Cipher import DES
import string
from itertools import product
from tqdm import tqdm
from pwn import *
import binascii

def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()

r=remote('mercury.picoctf.net',1903)
r.recvline()
flag_ct=bytes.fromhex(r.recvline().strip().decode())

test='41'
r.sendlineafter('What data would you like to encrypt? ',test)
test_ct=bytes.fromhex(r.recvline().strip().decode())
test=pad(binascii.unhexlify(test).decode())

table={}

for k in tqdm(product(string.digits,repeat=6),total=10**6):
    key=pad(''.join(k))
    ct=DES.new(key,DES.MODE_ECB).encrypt(test)
    table[ct]=key

for k in tqdm(product(string.digits,repeat=6),total=10**6):
    key=pad(''.join(k))
    ct=DES.new(key,DES.MODE_ECB).decrypt(test_ct)
    if ct in table:
        key1=table[ct]
        print(key,key1)
        flag=DES.new(key1,DES.MODE_ECB).decrypt(DES.new(key,DES.MODE_ECB).decrypt(flag_ct))
        print(flag)
        break
