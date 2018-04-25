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

message = 126

# Bobs information
P =random_prime(10^10,10^20) # prime
print("P: " + str(P))
#P = 389
G = randint(0,P-2)
print("G: " + str(G))
#G = 320
#x = randint(2,(P) -2)
x = 204
print("X: " + str(x))
Y = mod(G^x,P)
print("Y: " + str(Y))

#Alice's turn to encrypt
alice_rand = randint(0,21) # if this is huge, it takes a while...
print ("alice_rand: " + str(alice_rand))

r2 = mod(G^ alice_rand, P)
print("r2: " + str(r2))
t = mod(((Y^alice_rand) * message), P)
print("t: " + str(t))


M = (t/(r2^x)) % P

print("M: the final message... " + str(M))
