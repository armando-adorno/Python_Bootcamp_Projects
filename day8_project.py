alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    
    '''The encrypt() function implement the Caesar Cipher encryption algorithm for secure message transmision.'''

    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    encrypted_word = ""
    for letter in text:
        encrypted_word += alphabet[alphabet.index(letter) + shift]
        
    print(f"The encoded text is {encrypted_word}")

# PART 2

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text,shift):
    '''The decrypt() function implement the Caesar Cipher decryption algorithm for secure message transmision'''
    decrypted_word = ""
    for x in text:
      decrypted_word += alphabet[alphabet.index(x) + 26 - shift]
      
    print(f"The decoded text is {decrypted_word}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if(direction == "encode"):
    encrypt(text,shift)
elif(direction == "decode"):
    decrypt(text,shift)


