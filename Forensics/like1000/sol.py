import tarfile
import os

for i in range(1000,0,-1):
    f=str(i)+'.tar'
    tar=tarfile.open(f)
    tar.extractall()
    tar.close()
    if i!=1:
        os.remove(f)
