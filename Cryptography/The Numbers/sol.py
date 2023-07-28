a=[16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]
b=""

for i in range(len(a)):
    if i==6:
        b+=chr(a[i]+64)+"{"
    elif i==len(a)-1:
        b+=chr(a[i]+64)+"}"
    else:
        b+=chr(a[i]+64)
print(b)
