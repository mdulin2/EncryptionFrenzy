
# the diffie hellman algorithm.
# Both public
p =random_prime(10^20,10^30) # prime number
r = mod(primitive_root(p),p) # primative root

#private values for alice and bob
alice_rand = randint(1,p)
bob_rand = randint(1,p)

#numbers that we transfer, public
a = r ^ alice_rand
b = r ^ bob_rand

print a, b
# gets the same value for bob and alice as the key
print a ^ bob_rand
print b ^ alice_rand
