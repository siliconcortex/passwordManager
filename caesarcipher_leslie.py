def caesarEncrypt(message, offset):

  encrypt = " " 

  for char in message:
      if not char.isalpha(): #changed
          encrypt = encrypt + char
      elif char.isupper():
          encrypt = encrypt + chr((ord(char) + offset - 65) % 26 + 65) # for uppercase Z
      else:
          encrypt = encrypt + chr((ord(char) + offset - 97) % 26 + 97) # for lowercase z
  return encrypt

