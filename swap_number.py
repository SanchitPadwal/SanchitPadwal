
# Python code to swap two numbers

#solution1

# Number1 = int(input("Enter the number1 : "))
# Number2 = int(input("Enter the number2 : "))
#
# print("Before swap two number : " , Number1 , Number2)
#
# temp=Number1
# Number1=Number2
# Number2=temp
#
# print("After swap two number : " , Number1 , Number2)

#solution 2 --- withaout using third variable

Number1 = int(input("Enter the number1 : "))
Number2 = int(input("Enter the number2 : "))

print("Before swap two number : " , Number1 , Number2)

Number1 , Number2 = Number2 , Number1

print("After swap two number : " , Number1 , Number2)
