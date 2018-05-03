#-*-coding: utf-8-*-
# def sdesEncrypt(message, k):
#     bitArrays = []
#     for char in message:
#         charInt = ord(char)
#         p = list(bin(charInt))[2:]
#         for i in range(len(p)):
#             if p[i] == '1':
#                 p[i] = 1
#             elif p[i] == '0':
#                 p[i] = 0
#         if len(p) < 8:
#             while len(p) < 8:
#                 p.insert(0,0)
#
#         subkey1, subkey2 = subkeys(k)
#         bitArrays.append(Feistel_Enc(p,k, subkey1, subkey2)) # replace w group function
#
#         ciphertext = ""
#         #print bitArrays
#         for bitArray in bitArrays:
#             value = 0
#             for i in range(8):
#
#                 if bitArray[i] == 1:
#                     value += (2**(7 - i))
#
#             #print value
#             ciphertext += chr(value)
#             # print "Value: " + str(value)
#     #print type(ciphertext)
#     #print ciphertext[1]
#     return ciphertext

def sdesEncrypt(message, k):
    num = txt_to_num(message)
    bitArray = []
    bitstr = str(bin(num))
    bitstr = bitstr[2:]
    subkey1, subkey2 = subkeys(k)
    cipherNum = 0
    for i in range(0,len(bitstr),8):
        b = bitstr[i:(i+8)]
        if len(b) < 8:
            while len(b) < 8:
                b = "0" + b
        p = []
        for i in range(8):
            if b[i] == '0':
                p.append(0)
            else:
                p.append(1)
        f = Feistel_Enc(p,k, subkey1, subkey2)
        for bit in f:
            bitArray.insert(0, bit)
    exp = len(bitArray)
    for i in range(exp):
        cipherNum += (bitArray[i] * (2 ** (exp - i)))
    return num_to_txt(int(cipherNum))

def sdesDecrypt(ciphertext, k):
    num = txt_to_num(ciphertext)
    bitArrays = []
    bitstr = str(bin(num))
    bitstr = bitstr[2:]
    subkey1, subkey2 = subkeys(k)
    for i in range(0,len(bitstr),8):
        b = bitstr[i:(i+8)]
        p = []
        for i in range(8):
            if b[i] == '0':
                p.append[0]
            else:
                p.append[1]
        bitArrays.append(Feistel_Enc(p,k, subkey1, subkey2))
    return bitArrays


#msg_in is a string. Credit: Dr. Paul De Palma
def txt_to_num(msg_in):
    #transforms string to the indices of each letter in the 8-bit ASCII table
    msg_idx = map(ord,msg_in)
    #computes the base 256 integer formed from the indices transformed to decimal.
    #each digit in the list is multiplied by the respective power of 256 from
    #right to left.  For example, [64,64] = 256^1 * 64 + 256^0 * 64
    num = ZZ(msg_idx,256)
    return num

#Converts a digit sequence to a string
#Return the string
#num_in is a decimal integer composed as described above
# Credit: Dr. Paul De Palma
def num_to_txt(num_in):
    #returns the list described above
    msg_idx = num_in.digits(256)
    print msg_idx
    #maps each index to its associated character in the ascii table
    m = map(chr,msg_idx)
    #transforms the list to a string
    m = ''.join(m)
    return m


# def sdesDecrypt(ciphertext, k):
#     intValues = parseForUniqueChars(ciphertext)
#     bitArrays = []
#     for charInt in intValues:
#         p = list(bin(charInt))[2:]
#         for i in range(len(p)):
#             if p[i] == '1':
#                 p[i] = 1
#             elif p[i] == '0':
#                 p[i] = 0
#         if len(p) < 8:
#             while len(p) < 8:
#                 p.insert(0,0)
#
#         subkey1, subkey2 = subkeys(k)
#         bitArrays.append(Feistel_Dec(p,k,subkey1,subkey2))
#         #print "BitArrays:"
#         #print bitArrays
#         message = ""
#         for bitArray in bitArrays:
#             value = 0
#             for i in range(8):
#                 if bitArray[i] == 1:
#                     value += (2**(7 - i))
#             #print value
#             message += chr(value)
#     return message

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


# sdes = SimplifiedDES()
# k = [0,0,0,0,0,1,1,1,1,1]
# output = sdesEncrypt("dog",k)
# print output
# message = sdesDecrypt(output,k)
# print message


def get_k(p):

    while(True):
        rand_val = randint(2,p-1)
        if(gcd(rand_val,p -1) == 1):
            return rand_val

def key_gen():
    p = raw_input("Enter a prime: ")
    a = primitive_root(p)
    r = mod(a,p)
    alice_rand = raw_input("Enter a random value less than p")
    a = r ^ alice_rand % p
    print "Now send ", a , "to Bob!"
    print """

          """
    bob_rand = raw_input("What value did Bob send you back? ")
    print "The key is: ", a ^ bob_rand % p

def encrypt():
    k = raw_input("What is the 10 bit key?\n")
    message = raw_input("What message do you want to encrypt?\n")
    k = k.split(" ")
    key = [int(x) for x in k]
    output = sdesEncrypt("dog",key)
    """
    print output
    message = sdesDecrypt(output,key)
    print message
    """
def decrypt():
    k = raw_input("What is the 10 bit key?\n")
    message = raw_input("What message do you want to decrypt?\n")
    k = k.split(" ")
    key = [int(x) for x in k]
    message = sdesDecrypt(message, key)
    print "The decrypted message is ", message

def signing():
    message = 100
    print message
    # Bobs information
    P = 467
    print("P: " + str(P))

    a = primitive_root(P)
    a = 2
    print("a: " + str(a))

    x = randint(2,(P) -2)
    xA= 127
    print("xA: " + str(xA))
    Y = mod(a^xA,P)
    print("Y: " + str(Y))

    print("Private Key: ", x)
    print("Public Key: ",P,a,Y)

    x = get_k(P)
    x = 213
    r = a ** x %  P

    x_inv = inverse_mod(x,P-1)
    inside = (message - xA*r) * x_inv
    s = mod(inside, P-1)
    print x_inv,s

    print a ** message % P
    print "verify: "
    c1 = (Y**r * r ** s) % P
    print c1

# signing()
