import rsa

'''
Generates user 1's and user 2's public and private rsa keys

user1_public, user1_private = rsa.newkeys(1024)
with open("user1_public.pem", "wb") as fileWrite:
    fileWrite.write(user1_public.save_pkcs1("PEM"))

with open("user1_private.pem", "wb") as fileWrite:
    fileWrite.write(user1_private.save_pkcs1("PEM"))

user2_public, user2_private = rsa.newkeys(1024)
with open("user2_public.pem", "wb") as fileWrite:
    fileWrite.write(user2_public.save_pkcs1("PEM"))

with open("user2_private.pem", "wb") as fileWrite:
    fileWrite.write(user2_private.save_pkcs1("PEM"))

'''
# Now assume user 1 and user 2 have exchanged rsa keys

# Let's first simulate a send from user 1 to user 2

# Opens user 2's public key from PEM file
with open("user2_public.pem", "rb") as fileRead:
    user2_public = rsa.PublicKey.load_pkcs1(fileRead.read())

# User 1 declares the message
message1 = "What is the answer to 3 + 2?"

# Encrypts message using public key
encrypted_message1 = rsa.encrypt(message1.encode(), user2_public)

# The message is now sent to user 2

# Opens user 2's private key from PEM file
with open("user2_private.pem", "rb") as fileRead:
    user2_private = rsa.PrivateKey.load_pkcs1(fileRead.read())

# Decrypts message using user 2's private key
clear_message1 = rsa.decrypt(encrypted_message1, user2_private)

# Now to print the results
print("Encrypted Message 1:")
print(encrypted_message1)
print("Decrypted Message 1:")
print(clear_message1.decode())

# To simulate a send from user 2 to user 1, we must load user 1's public key before sending
with open("user1_public.pem", "rb") as fileRead:
    user1_public = rsa.PublicKey.load_pkcs1(fileRead.read())

# User 2 declares the message
message2 = "The answer is 5"

# Then, we will encrypt the message
encrypted_message2 = rsa.encrypt(message2.encode(), user1_public)

# The message is now sent to user 1

# Opens user 1's private key from PEM file
with open("user1_private.pem", "rb") as fileRead:
    user1_private = rsa.PrivateKey.load_pkcs1(fileRead.read())

# Decrypts message using user 1's private key
clear_message2 = rsa.decrypt(encrypted_message2, user1_private)

# Now to print the results
print("Encrypted Message 2:")
print(encrypted_message2)
print("Decrypted Message 2:")
print(clear_message2.decode())




# The below 2 lines write the encrypted message into a file, if needed
# with open("encrypted.message1", "wb") as f:
#    f.write(encrypted_message1)