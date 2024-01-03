#how to take input from user

num1 = input("enter the first value \n")
num2 = input("enter the second value \n")

print("number before swapping: \n")
print("the value of num1 is:",num1)
print("the value of num2 is:",num2)

temp = num1;
num1 = num2;
num2 = temp;

print("number after swapping: \n")
print("the value of num1 is:",num1)
print("the value of num2 is:",num2)
