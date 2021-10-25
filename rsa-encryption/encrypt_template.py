"""
This is a template script. Please work off of this.
To test the functionality of the script as you build
it, you can run this by opening a terminal, using 
"cd encryption_project_fellow" and then running 
"python encryptor.py".

Do NOT change the name of any of the files in the
zipped folder. If you do, the autograder will error out
and your project will receive a failing grade.

Your name: Cristina Samano-Romo
Your e-mail: cristysr@live.com
Date finished: 
"""

# Step 1
# Import the message_to_encrypt.txt file
# file = open("message_to_encrypt.txt", "r") 
# message = file.read()
message = "i have a pet parrot it likes to gossip and eat sunflower seeds"
# file.close()


# Step 2

# Encrypt the message following the instructions that were
# provided to you in the accompanying project description.
# If you find yourself having trouble with the newline character \n
# (which is invisible but is at the end of each line in the file)
# remember that you can remove it from each line with the .strip() method

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
e = 5
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

cipher = []
print('message: {}'.format(message))
for i in message:
    if i != '\n':
        translation = alphabet[i]
        c = (translation ** e) % n
        cipher.append(c)

print('cipher: {}'.format(cipher))


# Step 3
# Save the cipher to a file called "cipher.txt"
cipher_string = ''
for number in cipher:
    cipher_string += str(number)
    cipher_string += ' '
cipher_string = cipher_string[:-1]

f = open("cipher.txt", "w")
f.write(cipher_string)
f.close()

# Step 4
# Save the private key (not your public key!)
# as the "private_key.txt" file
f = open("private_key.txt", "w")
f.write(str(d))
f.close()

# Step 5
# Save the number n as the "n.txt" file
f = open("n.txt", "w")
f.write(str(n))
f.close()


# Step 6
# Go to the "decryptor.py" file and write the decryption code
f = open("e.txt", "w")
f.write(str(e))
f.close()