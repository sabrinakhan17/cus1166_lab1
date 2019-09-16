print ("Practicing Variables")

myvar = 1
print(f"Variable myvar : {myvar} is an {type(myvar)}")

y = 7.7
print(f"Variable y : {y} is an {type(y)}")

print("Done Practicing Variables")

print("Hello World")

myname = input("What is your name: ")
print("Hello "+ str(myname))
print("Hello %s" % myname)

print("Variable Checking")

i = 120
print(f"Variable i has the value {i}")

f = 1.6180339
print(f"Variable f has the value {f} and its type is {type(f)}")

b = True
print(f"Variable b has the value {b}")

n = None
print(f"Variable n has the value of {n}")

print("Done Variable Checking")

# tuple

c = (10,20,10)
print(f" c[0] has the value {c[0]} and is of type: {type(c)}")

# list
l = ["Anna", "Todd", "John"]
l = [10,20,30]
print(f" l[0] has the value {l[0]} and is of type: {type(l)}")

# Sets variables.

s = set()
s.add(1)
s.add(4)
s.add(6)
print(s)

# Dictionary

grades = {"Tom" : "A", "Mark": "B-"}
grades["Tom"]
grades["Anna"] = "F"
print("\n")
print('output of dictionary')
print(grades)
# Create an empty dictionary .
print("empty Dictionary")
mydictionary = dict()


#conditionals

x=10
if (x > 0):
    print("The number x is positive")
elif (x<0):
    print("The number x is negative")
else:
    print("The number x is zero")

#loops

for i in range(5):
    print(i)

for i_idx, i_value in enumerate(range(2,10)):
    print(f"{i_idx} - {i_value}" )

#defining and using functions

print(" let check if the input is even ")
input = int(input("Pick a number"))
def is_even(input):
    if (input % 2) == 0:
        return True
    else:
        return False
        
print(is_even(input))
