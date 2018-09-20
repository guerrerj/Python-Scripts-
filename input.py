import random
name = input("What is your name?")
print("Your name is " + name)

age = input("What is your age now?")
print(4* (" You are " + age + " years old \n")) #note can ony concatenate strings not int


num = int(input("Please enter the number of items you want in the list"))

my_list = []

for ch in range(num):
    temp = input()
    my_list.append(temp)

for element in my_list:
    print(element)


#checking all the divisors of a number
check = int(input("Enter a number to be factored by divisors?"))
x = range(2,check)
divisors = []
for element in x:
    if check % element == 0:
        divisors.append(element)

for elem in divisors:
    print(elem)

print(5 in divisors)
print("five in divisors")



    

    

    
