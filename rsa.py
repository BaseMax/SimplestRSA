# Max Base
# 2022-04-20
# Simplest RSA
# https://github.com/BaseMax/SimplestRSA

import math

p = 61
q = 53
message = 517

n = p * q
phi = (p - 1) * (q - 1)
for i in range(2, phi):
    if math.gcd(i, phi) == 1:
        break
key = (1 % (phi)) / i
encrypt = pow(message, i)
decrypt = pow(encrypt, key)

print(encrypt)
print(decrypt)
