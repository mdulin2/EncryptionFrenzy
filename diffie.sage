
# the diffie hellman algorithm.
# Both public
p =random_prime(2,(2**10)-1) # prime number
p = 191
print ":",p
s = primitive_root(p)
print 'S',s
r = mod(s,p) # primative root
print 'r',r
#private values for alice and bob
alice_rand = randint(1,p)
alice_rand = 133
print "alice:",alice_rand
bob_rand = randint(1,p)

#numbers that we transfer, public
a = r ^ alice_rand % p
b = r ^ bob_rand % p

print a, b
# gets the same value for bob and alice as the key
print a ^ bob_rand % p
print b ^ alice_rand % p
