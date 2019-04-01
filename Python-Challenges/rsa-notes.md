# RSA Notes

Notes were extracted from [Here](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

e = 2 to power 16 | 65537 | can be smaller but leaves encryption weaker
e = public key exponent and needed for encryption
d = private key exponent and needed for decryption

n = (p*q)

n is used as the modulus for both public and private keys

public key = e%n

public key = (n,e)

m = message 

convert m -> to numbers

c = cipher-text

encryption 

c === m-pow-e (mod n)  | python pow(m, e, n)

decryption

c pow d === m pow e pow d === m (mod n)

example

p=61
q=53
n=p*q = 3233
e=17
d=413

phi(n)=1cm(p-1, q-1)
phi(3233)=1(60,52) =780

d x e = 1 mod phi(n)
413 x 17 =1 mod 780

Public key = Encryption function
n=3233
e=17
c(m) = m pow 17 mod 3233

Private key = Decryption function
n=3233
d=413
m(c) = c pow 413 mod 3233

To Encrypt Message m
m=65
c = 65 pow 17 mod 3233 = 2790

To Decrypt Message m
c = 2790
m = 2790 pow 413 mod 3233 = 65

Calculate dp, dq and q inverse
dp = d mod (p-1) = 413 mod(61-1) = 53
dq = d mod (q-1) = 413 mod(53-1) = 49
q-inv = q pow -1 mod p = 53 pow -1 mod 61 = 38
(q-inv x q) mod p = 38 x 53 mod 61 = 1


m1 = c dp mod p = 2790 pow 53 mod 61 = 4
m2 = c dq mod q = 2790 pow 49 mod 53 = 12
h = (q-inv x (m1 x m2)) mod p = (38 x 8) mod 61 = 1
m = m2 + h x q = 12 + 1 x 53 = 65


phi(n)=(p-1)*(q-1)
phi(3233)=(61-1)*(53-1)=60*52=3120

m = c pow d mod n

phi = (p - 1)*(q - 1)
d = modinv(e,phi(n))

Encrypt
m = m pow e mod n  =  pow(m,e,n)

Decrypt
e x d mod phi(n) = 1


