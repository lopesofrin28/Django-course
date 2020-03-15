################################EXERCISES
s='django'
print(s[0])
print(s[-1])
print(s[:4])
print(s[1:4])
print(s[4:])


print(s[::-1])

#################PROBLEM2

l=[3,7,[1,4,'hello']]
print(l)
l[2][2]='goodbye'
print(l)


###########################PROBLEM3

d1={'simple_key':'hello'}
d2={'k1':{'k2':'hello'}}
d3={'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

##############################PROBLEM4

mylist=[1,1,1,1,1,2,2,2,2,3,3,3,3]
x=set(mylist)
print(x)


#####################################PROBLEM5

age=4
name="Sammy"

print("hello my dogs name is ",name," and he is ",age," years old")
print("hello my dogs name is {b} and he is {a} years old".format(a=age,b=name))
