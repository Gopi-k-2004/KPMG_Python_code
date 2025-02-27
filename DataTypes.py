# everything is object in python
# so u can diretly call methods

x = 'seven'
print(x)

x = 'seven'.capitalize()
print(x)

y = 'gopi krishna'.upper()
print(y)

x = "seven {} {}".format(8,9)
print(f"Value of x is {x}")
print(x)

x = "seven {1} {0}".format(8,9)
print(f"Value of x is {x}")
print(x)

y = "seven"
print("y is {}".format(y))

print("data types")

a = 7*3
print(type(a))

b = 7*3.14
print(type(b))

c = 7/3
print(type(c))

d = 7//3
print(d)
print(type(d))

e = 7%3
print(e)
print(type(e))

x = "" # None is false, "" is false
print(f"value of x is {x}")
print(type(x))
if x:
    print("true")
else:
    print("false")

# list [] is a mutable
# tuple () is immutable

x = [1,2,3,4,5]

print(type(x))
x[2] = 42
for i in x:
    print(f"i is {i}")

x = (1,2,3,4,5)
print(type(x))
# x[2] = 42
for i in x:
    print(f"i is {i}")

# list and tuple can contain elements of any datatype
x = (1,"two",3.0,[4,'four'],False)
y = (1,"two",3.0,[4,'four'],False)
#x[3] = [2,'four'] # this is invalid
# x[3][0] = True
print(f"x is {x}")
print(type(x))
# id returns a unique identifier for each element
print(id(x))
print(id(y))
a =1
print(id(x[0]))
print(id(y[0]))
print(id(a))

if x is y :
    print("same ")
else:
    print("different")

# is checks the reference but == checks the values

# if type(x) == 'tuple'  # this gives false becuase it is comparing type with a string

if x.__class__ == ().__class__:
    print("true")

