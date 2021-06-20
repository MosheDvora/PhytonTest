# A
Age = input("Enter a number X ")
Age = int(Age)
y = input("Enter a number Y")
y = int(y)
if Age > y:
    print("Big")
else:
    print("small")

# B
for Age in range(1, 6):
    print(Age)

# C
Age = input("Enter a number X ")
Age = int(Age)
if Age == 1:
    print("summer")
elif Age == 2:
    print("winter")
elif Age == 3:
    print("fall")
elif Age == 4:
    print("spring")
else:
    print("Error Number")

# D
# x10
# 10


# E

Age = 48
LastName = "Dvora"
LastNameFirstLetter = LastName[0]
ShekelDollarCurrency = 3.4
DidYouFlewAbroad = True
ApartmentNumber = 18
ApartmentNumber = int(ApartmentNumber)

print("Your Age: ", Age)
print("Your Last Name First Letter: ", LastNameFirstLetter)
print("The Shekel Dollar Currency: ", ShekelDollarCurrency)
print("Your Apartment Number: ", ApartmentNumber)
print("The Age plus Shekel to dollar Currency", Age + ShekelDollarCurrency)

# F
PhoneNumber = input("Enter Your Phone Number: ")
print("The Phone Number: ", PhoneNumber)


def printHello():
    print("Hello")


def calculate():
    return 5 + 3.2


print(calculate())


# h
def printYourName(Name):
    return Name


print(printYourName("Moshe"))


def divideBy2(Num):
    return Num / 2


print(divideBy2(10))


# I
def sum2number(num1, num2):
    return num1 + num2


print(sum2number(10, 5))


def connect2string(str1, str2):
    return str1 + " " + str2


print(connect2string("Moshe", "Dvora"))

#K
for vertical in range(6):
    for horizontal in range(vertical):
        print("*", end='')
    print("")

#L

for x in range(0, 3, 1):
        for space in range(x):
            print(" ",end='')
        print("*",end='')
        for space1 in range(7-(2 * x)):
            print(" ", end='')
        print("#")
print("    *")
for x in range(3,0,-1):
        for space in range(x):
            print(" ",end='')
        print("*",end='')
        for space1 in range(7-(2 * x)):
            print(" ", end='')
        print("#")
