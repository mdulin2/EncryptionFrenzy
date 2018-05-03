import random

def encrypt(message, k):
    subkey1, subkey2 = subkeys(k)
    cipherblocks = []
    cipherblocks.append(bin_to_list(bin(random.randint(128))))
    for i in range(len(message)):
        p = xorBinList(cipherblocks[i], bin_to_list(bin(ord(message[i]))))
        c1 = Feistel_Enc(p, k, subkey1, subkey2)
        cipherblocks.append(c1)
    return cipherblocks

def char_to_array(char):
    num = list(bin(ord(char)))[2:]
    for i in range(len(num)):
        if num[i] == '0':
            num[i] = 0
        else:
            num[i] = 1
    return num

def bin_to_list(binvalue):
    thelist = list(binvalue)[2:]
    for i in range(len(thelist)):
        if thelist[i] == '0':
            thelist[i] = 0
        else:
            thelist[i] = 1
    return thelist

def xorBinList(list1, list2):
    if len(list1) < 8:
        list1 = bufferZeros(list1, 8)
    if len(list2) < 8:
        list2 = bufferZeros(list2, 8)
    final = []
    for i in range(8):
        if list1[i] == list2[i]:
            final.append(0)
        else:
            final.append(1)
    return final

def bufferZeros(thelist, length):
    while len(thelist) < length:
        thelist.insert(0,0)
    return thelist
