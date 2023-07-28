import string
from itertools import product
import hashlib
from pwn import *
import random
from tqdm import *
import gmpy2

r=remote('mercury.picoctf.net',26695)

def find_p(e,n):
    BITS=20
    m=random.randint(2,n//2)
    for i in tqdm(range(1,1<<BITS)):
        p=gmpy2.gcd((gmpy2.powmod(m,i*e,n)-m)%n,n)
        if p!=1:
            print("[+] found...")
            print(p)
            return p

def setup():
    p=r.recvline().strip().decode()
    pre=p[33:38]
    suf=p[-6:]
    for i in product(string.printable,repeat=10):
        s=pre+"".join(i)
        if hashlib.md5(s.encode()).hexdigest()[-6:]==suf:
            r.sendline(s.encode())
            print(s)
            break

setup()
n=int(r.recvline().strip().decode().split(' :  ')[1])
e=int(r.recvline().strip().decode().split(' :  ')[1])
p=find_p(e,n)
q=n//p
r.sendline(str(p+q).encode())
print(r.recvline())
