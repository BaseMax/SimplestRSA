# Max Base
# 2022-04-20
# Simplest RSA
# https://github.com/BaseMax/SimplestRSA

def gcd(a, b):
    return gcd(b,a % b) if (a % b > 0) else b

p = 61
q = 53
message = 517

n = p * q
phi = (p-1)*(q-1)
for i in range(2, phi):
    if gcd(i, phi) == 1:
        break
key = (1 % (phi)) / i
encrypt = pow(message, i)
decrypt = pow(encrypt, key)

print(str(encrypt))
print(str(decrypt))
