import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    
    '''The encrypt() function implement the Caesar Cipher encryption algorithm for secure message transmision.''' 
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    encrypted_word = ""
    for letter in text:
        encrypted_word += alphabet[alphabet.index(letter) + shift]
        
    print(f"The encoded text is {encrypted_word}")

def decrypt(text,shift):
    '''The decrypt() function implement the Caesar Cipher decryption algorithm for secure message transmision'''
    decrypted_word = ""
    for x in text:
      decrypted_word += alphabet[alphabet.index(x) + 26 - shift]
      
    print(f"The decoded text is {decrypted_word}")
    
def caesar(text,shift,direction):
    '''The caesar() function implement the Caesar Cipher algorithm for secure message trasmision'''
    if(direction == "encode"):
        encrypt(text,shift)
    elif(direction == "decode"):
        decrypt(text,shift)
    else:
        print("Error")
 
caesar(text,shift,direction)


restart_program = input("\nWant Decode or Encode another message? \n\n1. Yes\n2. No\nEnter: ").lower()
if(restart_program == "yes" or restart_program == "1"):
    restart = True
else:
    restart = False

while(restart == True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text,shift,direction)
    
    restart_program = input("\nWant Decode or Encode another message? \n\n1. Yes\n2. No\nEnter: ").lower()
    if(restart_program == "yes" or restart_program == "1"):
      restart = True
    else:
      restart = False
      print("Good Bye")
    
    
    
    
    

    