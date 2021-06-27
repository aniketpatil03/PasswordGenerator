# Password Generator Project
import random
#List to choose from
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_qty = int(input("How many letters do you want in your password:\n"))
numbers_qty = int(input("How many numbers do you want in your password:\n"))
char_qty = int(input("How many characters do you want in your password:\n"))
 
password = ""                 #empty string

#used string concatebation
for char in range(0, letters_qty):
    password = password + random.choice(letters)

for char in range(0, numbers_qty):
    password += random.choice(numbers)

for char in range(0, char_qty):
    password += random.choice(symbols)
    
print("Password is ", password)    #Prints the pass





