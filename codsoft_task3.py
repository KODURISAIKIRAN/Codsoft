import random
symbols = ["!","@","#","$","%","^","&","*","(",")"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print("Welcome to Password Generator")
S_n = int(input("How many no. of symbols do you want in your Password"))
L_n = int(input("How many no. of Letters do you want in your Password"))
N_n = int(input("How many no. of Numbers do you want in your Password"))
password = []
for i in range(1,S_n+1):
    char = random.choice(symbols)
    password += char
for i in range(1,L_n+1):
    char = random.choice(letters)
    password += char
for i in range(1,N_n+1):
    char = random.choice(numbers)
    password += char
random.shuffle(password)
print()
print("Your Password is:")
password2 =""
for i in password:
    password2 += i
print(password2)