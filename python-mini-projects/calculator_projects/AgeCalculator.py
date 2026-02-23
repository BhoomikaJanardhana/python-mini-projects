from datetime import datetime

birth_year = int(input("Enter birth year: "))
current_year = datetime.now().year

age = current_year - birth_year

print("Age:", age)
print("Age in months:", age * 12)
print("Age in days:", age * 365)
print("Age in hours:", age * 365 * 24)
print("Age in minutes:", age * 365 * 24 * 60)
print("Years until 100:", 100 - age)