# Write a menu driven python program which performs the following: (Implement
# using if-else)
# a. Find area of circle ( 3.14 * r * r)
# b. Find area of triangle (0.5 * base * height)
# c. Find area of square and rectangle (side * side)(length * breath)
# d. Find Simple Interest

# Menu - Driven program
print("-----Menu-----")
print("1.Area of Circle")
print("2.Area of Triangle")
print("1.Area of Square")
print("1.Area of Rectangle")
print("1.Area of Interest")

choice = int(input("Enter your choice :"))
if choice == 1:
    radius = float(input("Enter your choice :"))
    area = 3.14 * radius * radius
    print("Area of Circle is ",area)
elif choice == 2:
    base = float(input("Enter your choice :"))
    height = float(input("Enter height :"))
    area = 0.5 * base * height
    print("Area of Triangle is ",area)
elif choice == 3:
    side = float(input("Enter side :"))
    area = side * side
    print("Area of Square is ",area)
elif choice == 4:
    length = float(input("Enter your choice :"))
    breadth = float(input("Enter breadth :"))
    area = length * breadth
    print("Area of Rectangle is ",area)
elif choice == 5:
    principal = float(input("Enter your choice :"))
    rate = float(input("Enter rate of interest :"))
    time = float(input("Enter time in years :"))
    si = (principal * rate * time) / 100
    print("Simple Interest is ", si)
else:
    print("Invalid Choice")