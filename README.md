# Simplest RSA (Rivest–Shamir–Adleman)

Simplest implementation of RSA algorithm **encryption** and **decryption**.

## Using RSA

```sh
$ php rsa.php
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
