from Crypto.Util.number import *

a=[104,85,69,354,344,50,149,65,187,420,77,127,385,318,133,72,206,236,206,83,342,206,370]
ch="Xabcdefghijklmnopqrstuvwxyz0123456789_"
flag=""

for i in a:
    flag+=ch[inverse(i,41)]

print("picoCTF{"+flag+"}")
