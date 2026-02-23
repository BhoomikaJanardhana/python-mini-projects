num = int(input("Enter a number: "))

if num < 0:
    print("Factorial not defined for negative numbers")

elif num == 0:
    print("0! = 1")

else:
    factorial = 1
    print(num, "! =", end=" ")

    for i in range(num, 0, -1):
        factorial *= i
        print(i, end="")
        if i != 1:
            print(" x ", end="")

    print(" =", factorial)