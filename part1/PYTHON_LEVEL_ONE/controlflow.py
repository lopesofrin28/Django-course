############COMPARISON OPERATORS

#Greater than
1>2
#Less than
1<2
# Greater than or Equal to
1 <= 2
# Less than or Equal to
1 >= 1
# Equality
1 == 1
1 == "1"  #not possible

# Inequality
1!=2

##################################LOGICAL OPERAOTRS
# AND
(1>2) and (2<3)

# OR
(1>2) or (2<3)

# Multiple Logical OPERATORS
(1==2) or (2==3) or (4==4)


###############################CONDITIONAL OPERATORS

# IF OPERATOR
if 1<2:
    print("yes!")

if 1<2:
    if 2<3:
        print("true!")

if 1<2:
    print("First block!")
    if 20<3:
        print("Second block!")


# IF ELSE STATEMENT
if 1<2:
    print("hola!")
else:
    print("Amigo!")


# ELIF LADDER
if 1<2:
    print("IF!")
elif 3==3:
    print("ELIF!")
else:
    print("ELSE!")


########################################LOOPS

################# FOR LOOPS
# seq = [1,2,3,4,5,6]
# for item in seq:
#      # Code here EXAMPLE:if item%2==0:
#          print(item)
#
#
# d={"sam":1,"frank":2,"dan":3}
# for k in d:
#     print(k)
#     print(d[k])
#
#
# mypairs=[(1,2),(3,4),(5,6)]
# for items in mypairs:
#     print(items)
#
# for (tup1,tup2) in mypairs:
#     print(tup1)
#     print(tup2)
#     print("\n")
#     print(tup2)
#     print(tup1)



###########  WHILE LOOPS
i=1

while i<5:
    print("i is: {}".format(i))
    i=i+1

# >>> [1,2,3,4,5]
# [1, 2, 3, 4, 5]
# >>> range(0,5)
# range(0, 5)
# >>> list(range(0,5))
# [0, 1, 2, 3, 4]
# >>> list(range(0,20,2))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# >>>

for item in range(10):
    print(item)



x=[1,2,3,4]

out=[]
for num in x:
    out.append(num**2)
print(out)


out=[num**2 for num in x]
print(out)


#PROGRAM TO PRINT STAR PATTERN 
# print("Program to print half pyramid: ");
# rows = input("Enter number of rows ")
# rows = int (rows)
# for i in range (0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")
