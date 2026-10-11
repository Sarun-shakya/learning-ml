a = 5 #integer
name = "sarun" #string (double quote)
sur_name = 'shakya' # string (single quote)

print(a)
print(name)

#casting (giving specific data type)
x = str(3);
y = int(4);
z = float(5);

print(type(x))
print(type(y))
print(type(z))

# assign multi values to a variables
a, b, c = "apple", "banana", "orange"

print(a);
print(b);
print(c);

# one value to multiple variable
p = q = r = "laptop"

print(p)
print(q)
print(r)

# unpack a collection
subjects = ["physics","chemistry","biology","mathematics"]
a1, a2, a3, a4 = subjects

# output mmultiple variables
print(a1 , a2 , a3 , a4);

# Global variables
feel = "awesome"

def myFunc():
    print(feel)
    global myVar # use global keyword for global variable
    myVar = "hehe"

myFunc()
print(myVar)
