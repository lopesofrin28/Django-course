############################FUNCTIONS

def my_func(param1="defaut"):
    '''
    THIS IS THE DOC STRING
    '''
    print("my first python function! {}".format(param1))

my_func()



def hello():
    print("hello")
hello()



def hello():
    return("hello")
result=hello()
print(result)


def addnum(num1,num2):
    return(num1+num2)
result=addnum(2,2)
print(result)


def addnum(num1,num2):
    return(num1+num2)
result=addnum("hi","world")
print(result)

result=addnum("2","3")
print(type(result))




def addnum(num1,num2):
    if type(num1)==type(num2)==type(10):
        return(num1+num2)
    else:
        return"Sorry,I need Integers"
result=addnum("2","2")
print(result)

#  ##########  lAMBDA EXPRESSION
mylist=[1,2,3,4,5,6,7,8]
def even_bool(num):
    return num%2==0

evens=filter(even_bool,mylist)
print(list(evens))

evens=filter(lambda num:num%2==0,mylist)
print(list(evens))



tweet="Go Sports! #Sports"
result=tweet.split("#")[1]
print(result)






print('x' in [1,2,3,'x'])
