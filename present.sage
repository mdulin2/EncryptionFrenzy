
def get_k(p):

    while(True):
        rand_val = randint(2,p-1)
        if(gcd(rand_val,p -1) == 1):
            return rand_val

def signing():
    message = 100
    print message
    # Bobs information
    P = 467
    P = raw_input(("Please input a prime to be used: "))
    print("P: " + str(P))

    a = primitive_root(P)
    a = 2
    print("primative root: " + str(a))

    xA= 127
    xA = int(raw_input("Input a random value under P:"))
    print("xA: " + str(xA))
    Y = mod(a^xA,P)
    print("Y: " + str(Y))

    print("Private Key: ", xA)
    print("Public Key: ",P,a,Y)

    x = get_k(int(P))
    #x = 213
    print a,x,P
    r = a ** x %  P
    print 'r: ',r
    x_inv = inverse_mod(x,int(P)-1)
    inside = (message - xA*r) * x_inv
    s = mod(int(inside), int(P)-1)
    print 's: ', s
    
def verify():

    a = int(raw_input("What is a?\n"))
    message = int(raw_input("What is the numerical message?\n"))
    P = int(raw_input("What is the prime?\n"))
    s1 = a ** message % P
    print "S1: ",s1

    Y = int(raw_input("What is Y?\n"))
    r = int(raw_input("What is r?\n"))
    s = int(raw_input("What is s?\n"))
    s2 = (Y**r * r ** s) % P
    print 'S2:',s2
    if(s1==s2):
        print s1,"=",s2
        print "Verified!"
    else:
        print "Intruder!"

#signing()
verify()
