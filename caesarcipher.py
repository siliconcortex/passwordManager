# encryption
message = input("Enter a message to be encrypted: ") # user inputs message to be encrypted
offset = int(input ("Enter an offset: ")) # user inputs offset
print ("\t")

encrypt = " " 

for char in message:
    if not char.isalpha(): #changed
        encrypt = encrypt + char
    elif char.isupper():
        encrypt = encrypt + chr((ord(char) + offset - 65) % 26 + 65) # for uppercase Z
    else:
        encrypt = encrypt + chr((ord(char) + offset - 97) % 26 + 97) # for lowercase z

print ("Your original message:",message)
print ("Your encrypted message:",encrypt)
print ("\t")
