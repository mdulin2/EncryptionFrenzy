"""
A good place to learn the algorithm:
https://asecuritysite.com/encryption/elgamal

This algorithm is built upon the discrete log problem.


El Gamel encryption-
Bob chooses chooses:
i) A large prime P
ii) Value G = random val between with 2 <= 2 <= pA -2
iii) Y = G ^ x mod P
iv) Choose the value x randomly as the private key

Public key for Bob is (B,P,Y)
Private key for Alice is x.

Alice takes the public keys then picks some random number k.
She then computes two values:
M = message being sent
a = G^k mod P
b = (Y^k)*m mod P

After this,
Plaintext = M = ((b)/(a^x)) mod P
The message is now decrypted!
"""

def get_k(p):

    while(True):
        rand_val = randint(2,p-1)
        if(gcd(rand_val,p -1) == 1):
            return rand_val
            
message = 100
print message
# Bobs information
P = random_prime(10^10,10^20) # prime
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
