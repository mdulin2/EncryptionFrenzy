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
message = 126

# Bobs information
P = random_prime(10^10,10^20) # prime
print("P: " + str(P))
P = 859
G = primitive_root(P)
print("G: " + str(G))
G = 2
x = randint(2,(P) -2)
x = 1000
print("X: " + str(x))
Y = mod(G^x,P)
print("Y: " + str(Y))

print("Private Key: ", x)
print("Public Key: ",P,G,Y)

k = get_k(P)
r = mod(G ** k, P)
s = mod(((message - x) / k),P-1)



#Alice's turn to encrypt
alice_rand = randint(0,2000) # if this is huge, it takes a while...
print ("alice_rand: " + str(alice_rand))

r2 = mod(G^ alice_rand, P)
print("r2: " + str(r2))
t = mod(((Y^alice_rand) * message), P)
print("t: " + str(t))


M = (t/(r2^x)) % P

print("M: the final message... " + str(M))
