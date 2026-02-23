# Take user input
name = input("Enter name: ")
age = input("Enter age: ")
course = input("Enter course: ")
college = input("Enter college: ")
email = input("Enter email: ")

width = 32  # Width inside the box

print("╔" + "═" * width + "╗")
print("║" + "STUDENT BIO CARD".center(width) + "║")
print("╠" + "═" * width + "╣")

print("║" + f"Name : {name}".ljust(width) + "║")
print("║" + f"Age : {age} years".ljust(width) + "║")
print("║" + f"Course : {course}".ljust(width) + "║")
print("║" + f"College : {college}".ljust(width) + "║")
print("║" + f"Email : {email}".ljust(width) + "║")

print("╚" + "═" * width + "╝")