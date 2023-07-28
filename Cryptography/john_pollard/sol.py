from Crypto.PublicKey import RSA
from sage.all import *

key=RSA.importKey(open('cert').read())
pr=list(str(factor(key.n)).split(' * '))
print("picoCTF{"+pr[1]+","+pr[0]+"}")
