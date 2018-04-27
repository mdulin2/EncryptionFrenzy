from sage.all_cmdline import *   # import sage library
from sage.crypto.block_cipher.sdes import SimplifiedDES

sdes = SimplifiedDES()

def sdesEncrypt(message, k):
    bitArrays = []
    for char in message:
        charInt = ord(char)
        p = list(bin(charInt))[2:]
        # alter p to always be 8 bits long
        if len(p) < 8:
            while len(p) < 8:
                p.insert(0,0)
        bitArrays.insert(sdes.encrypt(p, k),-1)
    return bitArrays
