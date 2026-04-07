print("Triangle Type Checker")

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

# Check if triangle is valid
if a + b > c and b + c > a and a + c > b:

    # Check triangle type
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")

else:
    print("Not a valid triangle")

# Calculate perimeter
perimeter = a + b + c
print("Perimeter:", perimeter)

# Check triangle size
if perimeter > 50:
    print("Large triangle")
else:
    print("Small triangle")