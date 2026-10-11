def greet():
    print("Hello, Python!")

greet()
greet()


def square(number):
    return number * number

print(square(3))
print(square(5))
print(square(10))

# default parameters
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Sarun")

#multiple return values
def calculate(a, b):
    total = a + b
    difference = a - b
    return total, difference

x, y = calculate(10, 4)

print(x)
print(y)