def jumble(a):
    if a>96:
        a+=9
    v=2*(a%16)
    if v>15:
        v+=1
    return v

print(jumble(ord('p')))
result="mlaebfkoibhoijfidblechbggcgldicegjbkcmolhdjihgmmieabohpdhjnciacbjjcnpcfaopigkpdfnoaknjlnlaohboimombk"
s=[0]*100

