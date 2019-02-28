import hashlib
import sys


#declare starting value
input = "ecsc"

#hash the starting value
input2 = hashlib.md5(input.encode()).hexdigest()

#end value
s2 = "c89aa2ffb9edcc6604005196b5f0e0e4"

while s2 != input2:
    #repeatedly hash value until a comparson is successful
    input2 = hashlib.md5(input2.encode()).hexdigest()
    print(input2)


