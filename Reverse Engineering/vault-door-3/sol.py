a="jU5t_a_sna_3lpm18gb41_u_4_mfr340"
flag=[""]*32

for i in range(8):
    flag[i]=a[i]

for i in range(8,16):
    flag[i]=a[23-i]

for i in range(16,32,2):
    flag[i]=a[46-i]

for i in range(31,16,-2):
    flag[i]=a[i]

print('picoCTF{'+''.join(flag)+'}')
