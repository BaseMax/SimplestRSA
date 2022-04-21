# Simplest RSA (Rivest–Shamir–Adleman)

Simplest implementation of RSA algorithm **encryption** and **decryption**.

> Richard Feynman: What I cannot create, I do not understand

## What is RSA?

RSA(Rivest-Shamir-Adleman) is an Asymmetric encryption technique that uses two different keys as public and private keys to perform the encryption and decryption. With RSA, you can encrypt sensitive information with a public key and a matching private key is used to decrypt the encrypted message.

## Using RSA

```sh
$ php rsa.php
OR
$ python rsa.py
```

### Semicode

```
p = 61;
q = 53;
message = 517;

n = p * q;
phi = (p-1)*(q-1);
i = 2;
gcd(a,b) = (a % b > 0) ? gcd(b,a % b) : b;
for(; i < phi; i++) {
    if(gcd(i, phi) == 1) break;
}
key = (1 % (phi)) / i;
encrypt = pow(message, i);
decrypt = pow(encrypt, key);
```

© Copyright Max Base, 2022
