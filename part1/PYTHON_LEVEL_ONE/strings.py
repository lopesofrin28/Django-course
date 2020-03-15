# STRINGS
# STRINGS ARE IMMUTABLE

# Basics
'hello'
"hello"

"I'm a dog"

# Indexing
mystring='abcdefg'
print(mystring[2])
print(mystring[4])


# Slicing
print(mystring[2:])
print(mystring[0:3])
print(mystring[2:5])
print(mystring[:3]) #upto but not including following index
print(mystring[::])
print(mystring[::2])



# Basic Methods
x=mystring.upper()
print(x)


mystring1='Hello world'
x=mystring1.split()
print(x)

y=mystring1.split('e')
print(y)

z=mystring1.split('o')
print(z)



#Print Formatting
a="Insert another string here:{}".format("INSERT ME!")
print(a)
b="Item one:{x} Item two:{y}".format(x="dog",y="cat")
print(b)
