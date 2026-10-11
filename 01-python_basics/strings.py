# strings in python

print("Hello")
print('Hello I am "sarun"') # double quote inside single
print("Hello I am 'sarun'") # single quote inside double

# Assign String to a Variable
myStr = "hello"
print(myStr)

# Multiline Strings
a = """This is a multi line string. 
        You can easily write it with triple quotes 
        """
print(a)

# Strings are Arrays
b = "Hello, World"
print(b[1]) # starts with 0

# String Length
print(len(b))

# Looping Through a String
for ch in b:
    print(ch)

# Check String
txt = "My name is regina phelange"
print("regina" in txt) # true
print("regina" not in txt) # false

num = 5
print("The number is " , num)