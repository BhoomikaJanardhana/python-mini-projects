number = int(input("Enter number: "))
end = int(input("Enter range (end): "))

print("\nMultiplication Table of", number)

for i in range(1, end + 1):
    print(number, "x", i, "=", number * i)