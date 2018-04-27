#Sammy Vowles

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
print(subkeys ([0,1,2,3,4,5,6,7,8,9]))
