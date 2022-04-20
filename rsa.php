<?php
// Max Base
// 2022-04-20
// Simplest RSA
// https://github.com/BaseMax/SimplestRSA

function gcd($a,$b) {
    return ($a % $b > 0) ? gcd($b,$a % $b) : $b;
}

$p = 61;
$q = 53;
$message = 517;

$n = $p * $q;
$phi = ($p-1)*($q-1);
$i = 2;
for(; $i < $phi; $i++) {
    if(gcd($i, $phi) == 1) break;
}
$key = (1 % ($phi)) / $i;
$encrypt = pow($message, $i);
$decrypt = pow($encrypt, $key);

print "$encrypt\n";
print "$decrypt\n";
