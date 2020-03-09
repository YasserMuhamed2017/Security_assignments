
def encryptShift(text,n):
  Input = open("input.txt", 'r')
  text = Input.read()
  encryptedText = "" 
  for i in range(len(text)):
   encryptedText += chr((chr(text[i] ) + n-65) % 26 + 65)
   output = open("output.txt", 'w')
   encryptedText = output.write(encryptedText) 
   #return encryptedText


def decryptShift(text,n):
 output = open("output.txt", 'r')
 text = output.read
 decryptedText = ""
 for i in range(len(text)):
   decryptedText += chr((chr(text[i] ) - n-65) % 26 + 65) 
   output = open("output.txt", 'w')
   decryptedText = output.write(decryptedText) 
   #return decryptedText

def affine_encrypt(text, key): 
  Input = open("input.txt", 'r')
  text = Input.read()
  encryptedText = "" 
   # C = (a*X + b) % 26 
  for i in range(len(text)):
   encryptedText += chr((( int(key[0])*(ord(text[i]) - ord('A')) + int(key[1]) ) % 26) + ord('A'))
   output = open("output.txt", 'w')
   encryptedText = output.write(encryptedText)
   #return encryptedText

def affine_decrypt(cipher, key): 
   output = open("output.txt", 'r')
   text = output.read
   decryptedText = ""
  # X = (a^-1 * (C - b)) % 26 
   for i in range(len(text)):

    decryptedText += chr((( int(key[0])*(ord(text[i]) - ord('A')) + int(key[1]) ) % 26) + ord('A'))
    output = open("output.txt", 'w')
    decryptedText = output.write(decryptedText) 
    #return decryptedText