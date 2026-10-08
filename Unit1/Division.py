num1 = int(input("Enter first number: "))
num2 = int(input("Enter first number: "))

# check if num 2 is zero
if num2 == 0:
    print("Division by 0 is not possible")
else:
    result = num1/num2
    print(result)
    if result > 1:
        print("The result is above 1")
    elif result < 1:
        print("The result is below 1")
