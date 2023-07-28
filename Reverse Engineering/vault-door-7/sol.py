from pwn import *

a=[1096770097,1952395366,1600270708,1601398833,1716808014,1734291511,960049251,1681089078]

print("picoCTF{"+"".join(p32(i,endian='big').decode() for i in a)+"}")
