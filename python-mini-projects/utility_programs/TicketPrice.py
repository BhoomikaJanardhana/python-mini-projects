age = int(input("Enter age: "))
day = input("Enter day: ")
tickets = int(input("Enter number of tickets: "))

# Age-based price
if age < 3:
    price = 0
elif age <= 12:
    price = 150
elif age <= 59:
    price = 300
else:
    price = 200

print("Base price per ticket:", price)

# Day-based discount
if day in ["Friday", "Saturday", "Sunday"]:
    discount = price * 0.20
else:
    discount = 0

print("Discount per ticket:", discount)

final_price = price - discount
total_amount = final_price * tickets

print("Price after discount:", final_price)
print("Total amount:", total_amount)