#Mini Project 3: Encryption, decryption machine

#Create an RSA key pair

#start with a pair of prime numbers p and q, where p >= 13 and q >= 17

p = 13
q = 17

#we define n as n = p x q

n = p *q
print("n =", n)

#define phi of n
phi_n = (p-1) * (q-1)
print("phi_n =", phi_n)

#define an int e
# e = int(input("pick a key greater than 1 and less than phi_n not divisible by phi_n \n"))
e = 7
print("e =", e)
#check e value is greater than 1 and less than phi_n
import math
if e <= 1 or e >= phi_n:
    print("e is NOT valid")

#check e value is not divisible by phi_n
if math.gcd(phi_n, e) != 1:
    print("e is a factor of phi_n, pick new e")
   
#calculate private key d
i = int(2)
d = int((i * phi_n + 1)/e)
print("private key (d) =", d)

#Encrypting using a public key

#define alphabet replacement dictionary

alphabet= {
        'a' : 1, 
        'b' : 2, 
        'c' : 3, 
        'd' : 4, 
        'e' : 5, 
        'f' : 6, 
        'g' : 7, 
        'h' : 8, 
        'i' : 9, 
        'j' : 10, 
        'k' : 11, 
        'l' : 12, 
        'm' : 13, 
        'n' : 14, 
        'o' : 15, 
        'p' : 16, 
        'q' : 17, 
        'r' : 18, 
        's' : 19, 
        't' : 20, 
        'u' : 21, 
        'v' : 22, 
        'w' : 23, 
        'x' : 24, 
        'y' : 25, 
        'z' : 26,
        ' ' : 27
    }

indexes = {
        1: 'a', 
        2: 'b', 
        3: 'c', 
        4: 'd', 
        5: 'e', 
        6: 'f', 
        7: 'g', 
        8: 'h', 
        9: 'i', 
        10: 'j', 
        11: 'k', 
        12: 'l', 
        13: 'm', 
        14: 'n', 
        15: 'o', 
        16: 'p', 
        17: 'q', 
        18: 'r', 
        19: 's', 
        20: 't', 
        21: 'u', 
        22: 'v', 
        23: 'w', 
        24: 'x', 
        25: 'y', 
        26: 'z',
        27: ' '
    }


message = 'apple'
cipher = []
for i in message:
    translation = alphabet[i]
    c = (translation ** e) % n
    cipher.append(c)

print('cipher: {}'.format(cipher))

print('Start the decryption process')

translation = []

decrypted = ''

for c in cipher:
    index = (c**d) % n
    decrypted += indexes[index]

print(decrypted)

    
