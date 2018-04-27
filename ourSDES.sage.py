from sage.all_cmdline import *   # import sage library
from sage.crypto.block_cipher.sdes import SimplifiedDES

sdes = SimplifiedDES()

def sdesEncrypt(message, k):
    bitArrays = []
    for char in message:
        charInt = ord(char)
        p = list(bin(charInt))[2:]
        for i in range(len(p)):
            if p[i] == '1':
                p[i] = 1
            elif p[i] == '0':
                p[i] = 0
        if len(p) < 8:
            while len(p) < 8:
                p.insert(0,0)
        bitArrays.append(sdes.encrypt(p,k))
    return bitArrays
