total = float(input("Enter total bill: "))
people = int(input("Number of people: "))
tax_percent = float(input("Tax %: "))
tip_percent = float(input("Tip %: "))

tax = total * tax_percent / 100
after_tax = total + tax
tip = after_tax * tip_percent / 100
final_total = after_tax + tip

print("Per person:", final_total / people)