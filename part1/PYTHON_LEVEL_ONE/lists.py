# #######################################################LISTS
# LISTS ARE MUTTABLE
# mylist=[1,2,3]
# print("length:",len(mylist))
#
# mylist1=['jdskfauyk',1,2,33,3.2,True,'asedf',[1,2,3]]
# print(mylist1)
#
#
# ###################################################### INDEXING
# mylist2=['a','b','c']
# print(mylist2[-1])
# print(mylist2[0])
#
# print("\n\n")
# # SLICING
# mylist3=['a','b','c','d','e','f']
# print("Before Reassignment:\n",mylist3)
# mylist3[0]='NEW ITEM'
# print("After Reassignment:\n",mylist3)


######################################### APPEND AT THE END
# mylist3.append("new item")
# print(mylist3)

# listtwo=['x','y','z']
# mylist3.append(["x",'y','z'])
# print(mylist3)
# mylist3.extend(listtwo)
# print(mylist3)
#
#
#
# item=mylist3.pop()
# print(mylist3)
# print(item)
#
# item1=mylist3.pop(6)
# print(mylist3)
# print(item1)

# mylist=['a','b','c','d','e']
# mylist.reverse()
# print(mylist)
#
# mylist1=[1,2,3,4,5]
# mylist1.reverse()
# print(mylist1)
#
# mylist2=[4,2,8,6,9]
# mylist2.sort()
# print(mylist2)


######################################### NESTED LISTS

mylist=[1,2,['x','y','z']]
print(mylist[2][1])

matrix=[[1,2,3],[4,5,6],[7,8,9]]

first_col=[row[0] for row in matrix]
print(first_col)
