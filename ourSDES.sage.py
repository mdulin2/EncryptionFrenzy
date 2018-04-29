#-*-coding: utf-8-*-
from sage.all_cmdline import *   # import sage library
from sage.crypto.block_cipher.sdes import SimplifiedDES

sdes = SimplifiedDES()

# k = [0,0,0,0,0,1,1,1,1,1]
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

        subkey1, subkey2 = subkeys(k)
        bitArrays.append(Feistel_Enc(p,k, subkey1, subkey2)) # replace w group function

        ciphertext = ""
        #print bitArrays
        for bitArray in bitArrays:
            value = 0
            for i in range(8):

                if bitArray[i] == 1:
                    value += (2**(7 - i))

            #print value
            ciphertext += chr(value)
            # print "Value: " + str(value)
    #print type(ciphertext)
    #print ciphertext[1]
    return ciphertext

def sdesDecrypt(ciphertext, k):
    intValues = parseForUniqueChars(ciphertext)
    bitArrays = []
    for charInt in intValues:
        p = list(bin(charInt))[2:]
        for i in range(len(p)):
            if p[i] == '1':
                p[i] = 1
            elif p[i] == '0':
                p[i] = 0
        if len(p) < 8:
            while len(p) < 8:
                p.insert(0,0)

        subkey1, subkey2 = subkeys(k)
        bitArrays.append(Feistel_Dec(p,k,subkey1,subkey2))
        #print "BitArrays:"
        #print bitArrays
        message = ""
        for bitArray in bitArrays:
            value = 0
            for i in range(8):
                if bitArray[i] == 1:
                    value += (2**(7 - i))
            #print value
            message += chr(value)
    return message

def parseForUniqueChars(ciphertext):
    intValues = []
    i = 0
    for i in range(len(ciphertext)):
        #print ord(ciphertext[i])
        intValues.append(ord(ciphertext[i]))
    #print intValues
    return intValues


# Sammy
def subkeys(k): #k is a list of elements
    #1 - works
    # the ten bits are first permuted according to the permutation:
    # (2,4,1,6,3,9,0,8,7,5)

    #variables to store the initial 10 elements
    e0= k[0]
    e1 = k[1]
    e2 = k[2]
    e3 = k[3]
    e4 = k[4]
    e5 = k[5]
    e6 = k[6]
    e7 = k[7]
    e8 = k[8]
    e9 = k[9]

    #permuted k
    permutedK = [e2,e4,e1,e6,e3,e9,e0,e8,e7,e5]
    #return permutedK

    #2 -works
    #the result is then split into two halves of five bits each
    #(2,4,1,6,3) (9,0,8,7,5)
    list1 = permutedK[0:5]
    list2 = permutedK[5:]
    #print("list1: ", list1)
    #print("list2: ", list2)

    #3 - works
    #for round 1, each half is cyclically shifted one bit to the left
    list1Round1 = shiftLeft(list1,1)
    #print("list1 after 1 shift left: ", list1Round1)
    list2Round1 = shiftLeft(list2,1)
    #print("list2 after 1 shift left: ", list2Round1)

    #4- i think this works
    #subkey one is obtained by taking these bits out of the result of the last operation:
    #(5,2,6,3,7,4,9,8)
    #get all elements in list1Round1 and list2Round1 and set as variables
    #to be used to get subkey one
    so0 = list1Round1[0]
    so1 = list1Round1[1]
    so2 = list1Round1[2]
    so3 = list1Round1[3]
    so4 = list1Round1[4]
    so5 = list2Round1[0]
    so6 = list2Round1[1]
    so7 = list2Round1[2]
    so8 = list2Round1[3]
    so9 = list2Round1[4]
    #create subkey one
    subkey1 = [so5,so2,so6,so3,so7,so4,so9,so8]
    #print ("subkey1: ",subkey1)

    #5- works
    #for round 2, the result of step 3 is shifted two bits to the left:
    #(b,c,d,e,a),(g,h,i,j,f) -> (d,e,a,b,c),(i,j,f,g,h)
    list1Round2 = shiftLeft(list1Round1,2)
    #print("list 1 after 2 more left shifts: ", list1Round2)

    list2Round2 = shiftLeft(list2Round1,2)
    #print("list 2 after 2 more left shifts: ", list2Round2)

    #6
    #then subkey two is obtained by taking the same bits out as were
    #used for subkey obtained
    st0 = list1Round2[0]
    st1 = list1Round2[1]
    st2 = list1Round2[2]
    st3 = list1Round2[3]
    st4 = list1Round2[4]
    st5 = list2Round2[0]
    st6 = list2Round2[1]
    st7 = list2Round2[2]
    st8 = list2Round2[3]
    st9 = list2Round2[4]

    subkey2 = [st5,st2,st6,st3,st7,st4,st9,st8]
    #print("subkey2: ",subkey2)

    return subkey1, subkey2

def shiftLeft (lst, n): #lst = list to be shifted, n = number of times to shift
    if(lst != []):
        for c in range(0,n):
            first = lst[0]

            for i in range (len(lst)-1):
                lst[i] = lst [i+1]
            lst[len(lst)-1] = first
    return lst

#Max

s_box1 =[[1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]]

s_box2 = [[0, 1, 2, 3],
          [2, 0, 1, 3],
          [3, 0, 1, 0,],
          [2, 1, 0, 3]]

"""
Permutes the list of bits
Args:
    lst(list): the list of bits
Returns:
    new_list(list): the scrambled list of bits
"""
def permute(lst):
    permutation = [1,5,2,0,3,7,4,6]
    new_list = list()
    for index in range(8):
        new_list.append(lst[permutation[index]])

    return new_list

"""
Unpermutes the list of bits
Args:
    lst(list): the list of bits
Returns:
    new_list(list): the unscrambled list of bits
"""
def permute_inverse(lst):
    permutation = [3,0,2,4,6,1,7,5]
    new_list = list()
    for index in range(8):
        new_list.append(lst[permutation[index]])
    return new_list


def xOR(lst1,lst2):
    new_list = list()
    for index in range(len(lst1)):
        if(lst1[index] == 0 and lst2[index] == 0):
            new_list.append(0)
        elif(lst1[index] == 1 and lst2[index] == 0):
                    new_list.append(1)
        elif(lst1[index] == 0 and lst2[index] == 1):
            new_list.append(1)
        else:
            new_list.append(0)

    return new_list

# the mixing function
def mix(byte_lst,subkey):
    scrambled = [3,0,1,2,1,2,3,0]
    new_list = list()
    for index in range(8):
        new_list.append(byte_lst[scrambled[index]])
    return xOR(new_list,subkey)

# splits the value into two parts
def split_value(byte_lst):
    return byte_lst[0:4],byte_lst[4:8]

#permutes the list in the Feistel step
def permute_fesisal(byte_lst):
    permute_lst = [1,3,2,0]
    new_list = list()
    for index in range(len(permute_lst)):
        new_list.append(byte_lst[permute_lst[index]])
    return new_list

def bin_to_index(byte_lst):
    if(byte_lst[0] == 0 and byte_lst[1] == 0):
        return 0
    elif(byte_lst[0] == 0 and byte_lst[1] == 1):
        return 1
    elif(byte_lst[0] == 1 and byte_lst[1] == 0):
        return 2
    else:
        return 3

def index_to_bin(value):
    if(value == 0):
        return [0,0]
    elif(value == 1):
        return [0,1]
    elif(value == 2):
        return [1,0]
    else:
        return [1,1]


def sbox_mix(byte_lst,box):
    outer1 = byte_lst[0]
    outer2 = byte_lst[3]
    inner1 = byte_lst[1]
    inner2 = byte_lst[2]
    row = [outer1,outer2]
    col = [inner1,inner2]

    row = bin_to_index(row)
    col = bin_to_index(col)

    box_get = box[row][col]
    return index_to_bin(box_get)

def interchange(byte_lst):
    first = byte_lst[0:4]
    second = byte_lst[4:8]
    return second + first

def Feistel_Dec(pt,key,subkey1,subkey2):

    p1 = permute(pt)
    p2,p3 = split_value(p1)
    p4 = mix(p3,subkey2)
    p5, p6 = split_value(p4)
    p7 = sbox_mix(p5,s_box1)
    p8 = sbox_mix(p6,s_box2)
    p9 = p7 + p8
    p10 = permute_fesisal(p9)
    p11 = xOR(p2,p10)
    p12 = p11 + p3
    e1 = interchange(p12)

    p2,p3 = split_value(e1)
    p4 = mix(p3,subkey1)
    p5, p6 = split_value(p4)
    p7 = sbox_mix(p5,s_box1)
    p8 = sbox_mix(p6,s_box2)
    p9 = p7 + p8
    p10 = permute_fesisal(p9)
    p11 = xOR(p2,p10)
    p12 = p11 + p3
    final = permute_inverse(p12)

    return final

def Feistel_Enc(pt,key, subkey1, subkey2):

    p1 = permute(pt)
    p2,p3 = split_value(p1)
    p4 = mix(p3,subkey1)
    p5, p6 = split_value(p4)
    p7 = sbox_mix(p5,s_box1)
    p8 = sbox_mix(p6,s_box2)
    p9 = p7 + p8
    p10 = permute_fesisal(p9)
    p11 = xOR(p2,p10)
    p12 = p11 + p3
    e1 = interchange(p12)


    p2,p3 = split_value(e1)
    p4 = mix(p3,subkey2)
    p5, p6 = split_value(p4)
    p7 = sbox_mix(p5,s_box1)
    p8 = sbox_mix(p6,s_box2)
    p9 = p7 + p8
    p10 = permute_fesisal(p9)
    p11 = xOR(p2,p10)
    p12 = p11 + p3
    final = permute_inverse(p12)
    return final
