def isprime (upper):
    #only numbers ending with 1,3,7 or 9 can be prime
    endings = [1,3,7,9]
    #primes that we are starting with (we dont need to try 2 or 5)
    primes = [3,7]
    #iterate from 1 to the upper range / 10 (I add ten first so that it does not round off to be smaller than the upper range)
    #I do this because we are going up in 10s
    for x in range(1, int((upper + 10) / 10)):
        #iterate through all of the endings
        for i in range(0,len(endings)):
            #set isprime to be intially True
            isprime = True;
            #add the ending/units digit to the tens digit
            number = x * 10 + endings[i];
            #iterate through all of the primes
            for z in range (0, len(primes)):
                #if the number is divisible by any of the existing primes it is not prime
                if (number % primes[z] == 0):

                    isprime = False;
                    #continue to the next number
                    break;
            #if the number is prime and it is less than the upper range
            #append it to the primes list
            if isprime == True and number <= upper:

                primes.append(number)
    #add the primes 2 and 5 back in
    primes.insert(1,5)
    primes.insert(0,2)
    #return the list of primes
    return primes

def findpriv (totient, coprime):
    #initialze x to equal 0
    x = 0
    #declare priv as a float
    priv = 0.1
    #while priv is not a while number
    while (priv != int(priv)):
        #set priv such that priv * coprime = 1 in mod totient
        priv = ((totient * x) + 1) / coprime
        #if increase x for the next interation
        x+=1
    #return the private key as an int 
    return int((priv))