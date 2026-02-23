def factorial(n):
    if n < 0:
        return "Invalid"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

def reverse_number(n):
    return int(str(n)[::-1])

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** power
    return total == n

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def is_perfect_number(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

def math_menu():
    while True:
        print("\nNumber System Menu")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("10. Exit")

        choice = int(input("Enter choice: "))

        if choice == 10:
            break

        if choice in [1,2,3,4,5,6,9]:
            n = int(input("Enter number: "))

        if choice == 1:
            print("Factorial:", factorial(n))
        elif choice == 2:
            print("Prime:", is_prime(n))
        elif choice == 3:
            print("Fibonacci:", fibonacci(n))
        elif choice == 4:
            print("Sum of digits:", sum_of_digits(n))
        elif choice == 5:
            print("Reversed:", reverse_number(n))
        elif choice == 6:
            print("Armstrong:", is_armstrong(n))
        elif choice == 7:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))
        elif choice == 8:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))
        elif choice == 9:
            print("Perfect Number:", is_perfect_number(n))
        else:
            print("Invalid choice")

math_menu()