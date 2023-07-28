from Crypto.Util.number import *
random_strs=[b'my encryption method',b'is absolutely impenetrable',b'and you will never',b'ever',b'break it']

ctxt=long_to_bytes(0x57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637)
key=b"Africa!"

def encrypt(a,b):
    ctxt=b''
    for i in range(max(len(a),len(b))):
        if len(a)>=len(b):
            m=a[i]
            n=b[i%len(b)]
        else:
            m=b[i]
            n=a[i%len(a)]
        ctxt+=bytes([m^n])
    return ctxt

for i in range(2):
        ctxt=encrypt(ctxt,random_strs[0])
        for j in range(2):
                ctxt=encrypt(ctxt,random_strs[1])
                for k in range(2):
                        ctxt=encrypt(ctxt,random_strs[2])
                        for l in range(2):
                                ctxt=encrypt(ctxt,random_strs[3])
                                for m in range(2):
                                        ctxt=encrypt(ctxt,random_strs[4])
                                        ctxt=encrypt(ctxt,key)
                                        print(i,j,k,l,m,ctxt)
