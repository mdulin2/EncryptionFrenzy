
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


k1 = [0,1,1,0,1,0,1,1]
k2 = [1,0,1,0,1,0,1,0]
pt = [0,1,0,1,0,1,0,1]
key = [0,0,0,0,1,1,1,1]

print pt
cipher = Feistel_Enc(pt,key,k1,k2)
plain_txt = Feistel_Dec(cipher,key,k1,k2)
print plain_txt
