#Caesar cipher
#Extablishing characters of the cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS) #1 - 52 is the possible range

def getMode():#function asking user whether they want to decrypt or encrypt
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('Enter your message: ')
    return input() #grabbing user's message
    #message=input('Enter your message: ')

def getKey(): #this functions forces the key range to be within 1 and 52
    key = 0
    while True: #keeps prompting user for key in range 1 - 52
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)#for each character in the message
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol
        else:
            #Encrypt or decrypt
            symbolIndex += key
        if symbolIndex >= len(SYMBOLS): #the shift starts happening here depending on length of SYMBOL list and the key
            symbolIndex -= len(SYMBOLS)
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)

        translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode() #these are the call functions
message = getMessage()
key = getKey()
print('Your translated text is: ') #print statements
print(getTranslatedMessage(mode, message, key)) #print statements