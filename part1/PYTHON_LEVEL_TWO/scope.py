# x=25
#
# def my_func():
#     x=50
#     return x
#
# print(x)  #Output is 25
# print(my_func()) #Output is 50
#
# my_func()
# print(x)

##############################3

#LOCAL
# lambda x:x**2



#Enclosing Function Locals
# name="This is a global name"
#
# def greet():
#     name="Sammy"
#
#     def hello():
#         print("hello ",name)
#
#     hello()
#
# greet()
# print(name)


##########################################

# x=50
#
# def func(x):
#     print("x is:",x)
#     x=1000
#     print("local x changed to:",x)
#
# func(x)
# print(x)


# ############################
x=50

def func():
    global x
    x=1000


print("Before function call,x is: ",x)
func()
print("After function call,x is: ",x)
