#sanity Check
import os

print("--------------------")
print("RUNNING THE SANITY CHECK")
print("--------------------")

#### Basic check of the encryptor
# Running the encryptor
os.system("python encryptor.py")

# Checking that the cipher file was generated and is not empty
if os.path.exists("cipher.txt"):
    cipher_file = open("cipher.txt", "r").read()
    if len(cipher_file) > 0:
        print("The cipher file was generated successfully.")
    else:
        raise Exception("The cipher file is empty!")
else:
    raise Exception("The cipher file was not generated successfully!")

# Checking that the private_key file was generated and is not empty
if os.path.exists("private_key.txt"):
    private_key_file = open("private_key.txt", "r").read()
    if len(private_key_file) > 0:
        print("The private_key file was generated successfully.")
    else:
        raise Exception("The private_key file is empty!")
else:
    raise Exception("The private_key file was not generated successfully!")

# Checking that the n file was generated and is not empty
if os.path.exists("n.txt"):
    n_file = open("n.txt", "r").read()
    if len(n_file) > 0:
        print("The n file was generated successfully.")
    else:
        raise Exception("The n file is empty!")
else:
    raise Exception("The n file was not generated successfully!")

#### Basic check of the decryptor
os.system("python decryptor.py")

# Checking that the decrypted_message file was generated and is not empty
if os.path.exists("decrypted_message.txt"):
    decrypted_message_file = open("decrypted_message.txt", "r").read()
    if len(decrypted_message_file) > 0:
        print("The decrypted_message file was generated successfully.")
    else:
        raise Exception("The decrypted_message file is empty!")
else:
    raise Exception("The decrypted_message file was not generated successfully!")

# Checking that the decrypted_message file and the message_to_encrypt file have the same contents
import filecmp
if filecmp.cmp("message_to_encrypt.txt", "decrypted_message.txt", shallow=False):
    print("************\n\n\nSUCCESS: THE ORIGINAL MESSAGE AND THE ENCRYPTED MESSAGE MATCH!!!!")
else:
    raise Exception("ERROR: THE ORIGINAL MESSAGE AND THE ENCRYPTED MESSAGE DON'T MATCH!!!!")
