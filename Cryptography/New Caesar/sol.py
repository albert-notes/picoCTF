flag_enc="kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"

def b16decode(enc):
    flag=""
    for a,b in zip(enc[::2],enc[1::2]):
        flag+=chr((ord(b)-ord("a"))+(ord(a)-ord("a"))*16)
    return flag

for i in range(16):
    shifted="".join(chr(((ord(c)-ord("a")+i)%16)+ord("a"))for c in flag_enc)
    print(i,"picoCTF{"+b16decode(shifted)+"}")
