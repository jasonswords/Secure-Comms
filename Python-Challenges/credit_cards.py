import sys
import random


#string = "123456789"
checkDigit = ""

#using luhn algorithm, take in card number and return 0 for valid, anything else is invalid
def validate_card(cardNumber, swap):  #declare function
    reverse_string= cardNumber[::-1]    #reverse card number
    new_list = []

    for i in range(len(reverse_string)):    #loop through range equal to card number lenght
        if i%2==swap:  #if index is odd
            new_list.append(int(reverse_string[i])*2)   #multiply numbers by 2 and store in new_list
            if new_list[i]> 9:  #if number is greater than 9, subtract 9 and store in new_list
                new_list[i] = new_list[i]-9 #store value in new_list
        else:
            new_list.append(int(reverse_string[i])) #store value in new_list
    return sum(new_list)%10 #return the sum of new_list mod 10 --- should be 0 for valid cards


#return random digits within range 0-9
def random_numbers(number_of_digits):
    random_card_number=""
    for i in range(int(number_of_digits)):
        random_card_number += str(random.randint(0,9))
    return random_card_number #return string containing random numbers


#tuples of vendors and their possible prefix numbers
#each tuple has first index card name and then prefis numbers
visa_electron = "visa electron", "4026","417500","4508","4844","4913","4917"
mastercard = "mastercard", "51","52","53","54","55"
maestro = "maestro", "5018","5020","5038","5893","6304","6759","6761","6762","6763"
american_express = "american express", "34","37"
discover = "discover", "6011","644","645","646","647","648","649","65"
diners_club = "diners club", "300", "301", "302", "303", "304", "305"


#list of vendor names to easily allow search through each vendor
vendors= visa_electron, mastercard, maestro, american_express, discover, diners_club


#list of prefix lenghts for each vendor
card_prefix_length = {'visa electron' : [16],
               'mastercard':[16],
               'maestro': [16,17,18,19],
               'american express': [15],
               'discover': [16,17,18,19],
               'diners club': [14]}


#function to return a random prefix from list using the vendors name
def return_random_prefix(name):
    for v in vendors:   #loop through list of vendors
        if v[0].lower() == name.lower():#compare
            return random.choice(v[1:])#return random prefix value
    return -1

#function to search for prefix numbers limiting the search to first six digits
def output_vendor(cardNumber):
    #cardNumber.replace(" ", "")
    for v in vendors: #loop through vendors
        for n in v:#loop through vendor prefix values
            if n in cardNumber[:6]: #check for equal values
                return v[0] #return name of vendor
            else:
                continue
    return -1#if no value found


#function calculate the check digit of card number without check digit included
def calculate_check_sum(partial_card_number):
    #search vendors for name that matches prefix digits
    name = output_vendor(partial_card_number[:6])
    #return random card length specific to vendor
    try:
        card_length = random.choice(card_prefix_length.get(name))
        #create random digits to length calculated minus one for check sum
        string =  random_numbers((card_length - len(partial_card_number))-1)
        #append random digits to partial card number
        partial_card_number += ''.join(str(e) for e in string)

        #check if returned value is 0
        if validate_card(partial_card_number, swap=0) > 0:
            #append didgit to card number if return value above 0
            partial_card_number += str(10 - validate_card(partial_card_number, swap=0))
        else:
            #append 0 to partial card number
            partial_card_number += str(0)

        #return valid card number
        return partial_card_number

    except:
        return -1



#generate credit card numbers for specific vendors
def generate_credit_card_numbers(vendor_name):
    #get randomly selected prefix for vendor
    prefix = return_random_prefix(vendor_name)
    #check for invalid vendor names
    if prefix == -1:
        print("Error.... no vendor located")
    #get random length value specific to vendor
    card_length = random.choice(card_prefix_length.get(vendor_name))
    #assign the prefix and random numbers -1 to fill remaining spaces
    new_card = str(prefix) + random_numbers((card_length - len(prefix))-1)

     #check if returned value is 0
    if validate_card(new_card, swap=0) > 0:
        #append didgit to card number if return value above 0
        new_card += str(10 - validate_card(new_card, swap=0))
    else:
        #append 0 to partial card number
        new_card += str(0)

    #return valid card number
    return new_card



#create menu to display options
ans = True
while ans:
    choice = input(  """
        1. Verify Cred Card Number
        2. Vendor Discovery
        3. Calculate Checksum
        4. Generate Credit Card Number
        5. Exit
        """)

#check choice and display relevant menu
    if int(choice) == 1:
        card = input("Please input credit card number:  ")
        valid = validate_card(card, swap=1)
        if valid == 0:
            print("The card is a Valid card")
        else:
            print("This is an Invalid card")
    elif int(choice) == 2:
        card = input("Please input credit card number:  ")
        vendor = output_vendor(card)
        if vendor != -1:
            print("The issuing vendor is ", vendor)
        else:
            print("The card number is not recognised")
    elif int(choice) == 3:
        card = input("Please input the partial credit card number:  ")
        valid_number = calculate_check_sum(card)
        if valid_number != -1:
            print("The valid credit card number is : ", valid_number)
        else:
            print("The card number was not recognised")
    elif int(choice) == 4:
        card = input("Please input the vendor:  ")
        try:
            card_number = generate_credit_card_numbers(card)
            print("The card number is: -  ", card_number)
        except:
            print("Problem finding vendor")
    elif int(choice) == 5:
        print("Goodbye")
        ans = False




