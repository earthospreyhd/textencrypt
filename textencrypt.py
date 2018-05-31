#run with python 3
from primepriv import isprime, findpriv
import os
#function which choses the keys using the seed that the user enters
def findkeys (strSeed):

    seed = [None] * len(strSeed)

    for x,char in enumerate(strSeed):

        seed[x] = ord(char)

    seedlen = len(seed)

    seedslice = int(seedlen / 3)

    seed1 = sum(seed[0:seedslice]) / seedslice

    seed2 = sum(seed[seedslice:int((seedlen / 3) * 2)]) / seedslice

    seed3 = sum(seed[int((seedlen / 3) * 2):seedlen]) / (int(seedlen - (seedslice)))

    keys = list()

    primes = isprime(10000)

    primeslen = len(primes)

    prime1 = primes [int((primeslen / 6) + (primeslen / 6) * (seed1 / 255))]

    prime2 = primes [int((primeslen / 3) + (primeslen / 3) * (seed2 / 255))]

    mod = prime1 * prime2

    keys.append(mod)

    totient = (prime1 - 1) * (prime2 - 1)

    publickey = primes [int((primeslen / 3) * 2 + (primeslen / 3) * (seed3 / 255))]

    keys.append(publickey)
    #call function which finds the private key
    privatekey = findpriv(totient, publickey)

    keys.append(privatekey)

    return keys

#function which encrypts by calling findkeys function and enrypt char function
def encrypt (inputtext, seed):

    keys = findkeys(seed)

    mod = keys[0]

    publickey = keys[1]

    privatekey = keys[2]

    output = [None] * len(inputtext)

    for x, char in enumerate(inputtext):

        output[x] = str(encryptchar(ord(char) + x, publickey, mod) + x)

    return output
#function which decrypts the file text by using the findkeys function and decrypt int function
def decrypt (inputtext, seed):

    keys = findkeys(seed)

    output = [None] * len(inputtext)

    privatekey = keys[2]

    mod = keys[0]
    #loop which calls the decryptint function and decrypts all the characters in the string
    for x,num in enumerate(inputtext):

        output[x] = chr(decryptint(int(num) - x, privatekey, mod) - x)

    return output
#function which encrypts a char using rsa
def encryptchar (char, publickey, mod):

    char = pow(char, publickey, mod)

    return char
#function which decrypts an int and turns it into a char
def decryptint (num, privatekey, mod):

    char = pow(num, privatekey,mod)

    return char
#loop to make sure user input is correct
while True:

    try:

        status = int(input("Enter 1 to encrypt a file or 0 to decrypt a file: "))
        #test if user input is valid
        if status == 1 or status == 0:

            break

        else:

            print("Please enter a valid number\n")

    except:

        print("Please enter a number\n")
#if user puts in 1, start encrypt routine
if status == 1:

    while True:

        try:

            filename = input("Please enter the name of the file that you would like to encrypt: ")

            file = open (filename)

            inputtext = file.read()

            outfilename = input("Enter the name of the file that you would like to store the encrypted text in: ")


            break

        except:

            print("Please enter valid file names")

    while True:

        try:

            seed = input("Please put in your encryption key (three or more characters): ")
            #call encrypt function
            output = encrypt (inputtext, seed)

            print("Your file has been successfully encrypted into '" + outfilename + "' \n")

            break

        except:

            print("Your key was less than three characters. Please try again")

    outfile = open(outfilename, "w")
    #write output to file
    outfile.write(' '.join(output))
#if user puts in 0, start decrypt routine
else:

    while True:

        try:

            filename = input("Please enter the name of the file that you would like to decrypt: ")

            file = open(filename)

            inputtext = file.read()

            inputtext = inputtext.split(' ')

            outfilename = input("Please enter the name of the file that you would like to store the decrypted text in: ")

            break

        except:

            print("That is not a valid file name\n")

    while True:

        try:

            seed = input ("Put in your decryption key: ")
            #call decrypt function
            output = decrypt(inputtext, seed)

            outfile = open(outfilename, "w")
            #write output to file
            outfile.write(''.join(output))

            print("Your file '" + outfilename + "'' has been successfully decypted")

            break

        except:

            print("You entered the wrong decryption key\n")
#Loop for deleting the original file if the user wants to
while True:

    deletefile = input("Enter 1 if you would like to keep the original file or 0 if you would like to delete it: ")

    if deletefile == '0':

        try:

            os.remove(filename)

            print("The original file '" + filename + "'' has been destroyed")

            break

        except:

            print("An error occurred when trying to delete the original file")

            break

    elif deletefile == '1':

        break

    else:

        print("Please enter a valid option")