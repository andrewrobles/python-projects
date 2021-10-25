"""
This is a template script. Please work off of this.
To test the functionality of the script as you build
it, you can run this by opening a terminal, using 
"cd encryption_project_fellow" and then running 
"python decryptor.py".

Do NOT change the name of any of the files in the
zipped folder. If you do, the autograder will error out
and your project will receive a failing grade.

Your name:
Your e-mail:
Date finished: 
"""

# Step 1
# Import the cipher.txt file
# file = open("cipher.txt", "r") 
# cipher = file.read()
# file.close()
cipher = "42 40 60 1 133 31 40 1 40 152 31 141 40 152 1 18 18 19 141 40 42 141 40 207 42 163 31 15 40 141 19 40 11 19 15 15 42 152 40 1 131 140 40 31 1 141 40 15 21 131 41 207 19 160 31 18 40 15 31 31 140 15"


# Step 2
# Import the private_key.txt file
file = open("private_key.txt", "r") 
private_key = file.read()
file.close()

# Step 3
# Import the n.txt file
file = open("n.txt", "r") 
n = file.read()
file.close()

# Step 4
# Decrypt the message following the instructions that were
# provided to you in the accompanying project description.
to_letter = {
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

message = ''
for c in cipher.split():
    decrypted = (int(c) ** int(private_key)) % int(n)
    message += to_letter[decrypted]

print('message: {}'.format(message))

# Step 5
# Save the decrypted message to a file called "decrypted_message.txt"
f = open("decrypted_message.txt", "w")
f.write(message)
f.close()

# Step 6
# Run "python sanity_check.py" to verify
# that the original message matches the decrypted message
