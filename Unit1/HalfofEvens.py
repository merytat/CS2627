# input
number = int(input("Enter a number: "))

# calculate
isEven = number % 2 == 0 # True if even

if isEven:
    print("This is an even number")
    print("Divided by 2: ", number / 2)
    
print("Good day!")
