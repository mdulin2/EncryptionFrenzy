
# the diffie hellman algorithm.
# Both public
def diffie(p,g,alice_rand,bob_rand):

    #p =random_prime(2,(2**10)-1) # prime number
    #p = 191
    print "p,g",p,g
    s = primitive_root(p)
    r = mod(s,p) # primative root
    r = g
    #private values for alice and bob
    #alice_rand = randint(1,p)
    #alice_rand = 133
    print "alice:",alice_rand

    #numbers that we transfer, public
    print "bob",bob_rand
    a = r ** alice_rand % p

    return bob_rand ** alice_rand % p

print diffie(23,5,3,4)
