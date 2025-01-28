name = "Travis Benedict"
age = 26
hight = "5ft 10in"
favorite_color = "green"
print("Name")
print(name)
print(" ")
print("Age")
print(age)
print("")
print("Hight")
print(hight)
print()
print("Favorite Color")
print(favorite_color)
print()

print(name, age, hight, favorite_color)
print()

print(f"Hello! My name is {name}. I am {hight} tall, I'm {age} years old, and my favorite color is {favorite_color}.")
print()

n = 17
print(f"the number {n:03d} is one of many out of 100")
print()

print(f"""
Name: {name}
Age: {age}
""")

import math

circle_area = math.pi * 5**2
print(f"{circle_area:.1f}")
print("")
print("square root of age")
print(math.sqrt(age))
print()
hight_inches = 5 * 12 + 10
print("sin of hight")
print(math.sin(hight_inches))
print()
print("cos of hight")
print(math.cos(hight_inches))
print()

print(age + 5)
print(hight_inches - 4)
print(age * hight_inches)
print(hight_inches/2)
print(age/3)
print(age**2)


print(f"""
The sum of age and 5 is ({age + 5})
The difference between height and 4 is ({hight_inches - 4})
The product of age and height is ({age * hight_inches})
The quotient of height and 2 is ({hight_inches/2})
The remainder of age divided by 3 is ({age % 3})
age raised to the power of 2 is ({age**2})
""")
print()

f = int(input("Please input the value in Fahrenheit that you want converted into Celsius: "))
print(f"{f}°F in Fahrenheit is {(f - 32) * 5/9:.1f}°C in Celsius")

