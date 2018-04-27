#-*-coding: utf-8-*-
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

        bitArrays.append(sdes.encrypt(p,k)) # replace w group function

        ciphertext = ""
        for bitArray in bitArrays:
            print bitArray
            value = 0
            for i in range(8):

                if bitArray[i] == 1:
                    value += (2**(7 - i))

            ciphertext += chr(value)
            # print "Value: " + str(value)
    return ciphertext

def sdesDecrypt(ciphertext, k):
    bitArrays = []
    for char in ciphertext:
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
        bitArrays.append(sdes.decrypt(p,k))
        message = ""
        for bitArray in bitArrays:
            value = 0
            for i in range(8):
                if bitArray[i] == 0:
                    value += (2**(7 - i))

            message += chr(value)
    return message
