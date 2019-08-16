import string
from sys import exit

#global variables
chars_to_numbers = {}
numbers_to_code = {}
caps = ['Q','R','U','P','D','H','L','C','N','W','T','I','A','F','J','Z','V','M','E','Y','O','S','G','K','X','B']
nums = [1,4,7,0,3,6,9,2,5,8]
s_and_s = ['a','@','s','#','d','$','f','%','g','^','h','&','j','*','k']

def initial_map():
    '''
    Initializing the maps for encryption and decryption
    '''
    #all the global variables
    global chars_to_numbers
    global numbers_to_code
    global caps
    global nums
    global s_and_s

    #initializing everything for the map
    letters = string.printable
    count = 0
    code_count = 0

    #initializing the map
    for letter in letters:
        chars_to_numbers[letter] = count
        count += 1
    chars_to_numbers[' '] = count
    for i in chars_to_numbers.values():
        numbers_to_code[i] = caps[code_count%len(caps)]+str(nums[code_count%len(nums)])+s_and_s[code_count%len(s_and_s)]
        code_count += 1
    
def map_for_decrypt():
    '''
    this function is for reversing the map for decryption
    '''
    global chars_to_numbers
    global numbers_to_code
    chars_to_numbers = {v:k for k,v in chars_to_numbers.items()}
    numbers_to_code = {v:k for k,v in numbers_to_code.items()}

def encrypt(message):
    '''
    function to encrypt the given message
    '''
    global chars_to_numbers
    global numbers_to_code
    temporary = message
    message = ''
    for character in temporary:
        message += numbers_to_code[chars_to_numbers[character]]
    return message

def decrypt(message):
    '''
    function to decrypt the message
    '''
    global chars_to_numbers
    global numbers_to_code
    start = 0
    end = 3
    temporary = message
    message = ''
    while start != len(temporary):
        try:
            message += chars_to_numbers[numbers_to_code[temporary[start:end]]]
            start += 3 
            end += 3
        except KeyError:
            exit('Sorry there was a problem decrypting the file please check the key and try again.')
    return message

def bin_ende(message, key, eord):
    '''
    function to binary encrypt/decrypt the message
    '''
    bytecount = 0
    message = bytearray(message)
    for index, value in enumerate(message):
        message[index] = value ^ (key[bytecount%len(key)])%20
        #~message[index]
        bytecount += 1
    if eord == 'e':
        return message
    elif eord == 'd':
        message = bytes(message)
        message = str(message)
        message = message[2:len(message)-1]
        return message


if __name__ == "__main__":
    choices = ['e', 'd']
    print('Keep the program and the file in the same directory !!!!')
    #entering the choice of e/d
    while True:
        try:
            choice = input('Encrypt or Decrypt the file (e/d) :')
            choice = choice.lower()
            if choice not in choices:
                print('Please enter the correct option ')
                continue
            break
        except:
            print('Please enter the correct option ')
    
    #take the file name
    while True:
        try:
            file_name = input('Enter the name of the file :')
            file = open(file_name)
            file.close()
            break
        except FileNotFoundError:
            print('Please enter a valid file name and make sure the file and the program are in the same directory!!')

    #entering the key
    key_string = input('Enter the key :')
    key = bytearray(key_string, 'utf-8')

    if choice == 'e':
        initial_map()
        with open(file_name, 'r') as file:
            message = file.read()
        message = encrypt(message)
        with open(file_name, 'w') as file:
            file.write(message)
        with open(file_name, 'rb') as file:
            message = file.read()
        message = bin_ende(message, key, 'e')
        with open(file_name, 'wb') as file:
            file.write(message)
        print('File encrypted successfully')
    elif choice == 'd':
        initial_map()
        map_for_decrypt()
        with open(file_name, 'rb') as file:
            message = file.read()
        message = bin_ende(message, key, 'd')
        '''
        with open(file_name, 'wb') as file:
            file.write(message)
        with open(file_name, 'r') as file:
            message = file.read()
        '''
        message = decrypt(message)
        with open(file_name, 'w') as file:
            file.write(message)
        print('File decrypted successfully')