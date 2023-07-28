from scipy.io import wavfile

samplerate,data=wavfile.read("main.wav")

hexed=[]
for i in data:
    r=(i-1000)//500
    hexed.append(hex(r)[2:])

print(bytearray.fromhex(''.join(hexed)).decode())
