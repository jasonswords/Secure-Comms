import sys

#declare vaiables for each cipher
caesar = 26
rot47 = 93
rot5 = 10

#function to loop through input and rotate characters
def cipher( max_iterations, input, base):
#iterate the input a specified number of times
    for k in range(max_iterations):   #iterate through each characte
        for i in input:
#using the decimal values of the characters, and setting each value to zero, increase the value of the
#character each time the loop iterates.
            print(chr((((ord(i)-base)+k)%max_iterations)+base),end="")
        print("")


#check what arguments are passed
if sys.argv[1].lower() == 'caesar':
    cipher(caesar, sys.argv[2], base=97)

elif sys.argv[1].lower() == 'rot47':
    cipher(rot47, sys.argv[2], base=33)

elif sys.argv[1].lower() == 'rot5':
    cipher(rot5, sys.argv[2], base=48)
else:
    print("python rotational-cipher.py [caesar/rot47/rot5] [string-input]")

