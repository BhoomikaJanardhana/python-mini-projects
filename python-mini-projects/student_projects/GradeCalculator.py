total = 0
pass_all = True

# Loop for 5 subjects
for i in range(1, 6):
    marks = int(input(f"Enter marks for Subject {i}: "))
    
    if marks < 40:
        pass_all = False
    
    total += marks

# Percentage formula
percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage)

# Check pass or fail
if pass_all:
    print("Result: PASS")
else:
    print("Result: FAIL")

# Grading using if-elif
if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: F")