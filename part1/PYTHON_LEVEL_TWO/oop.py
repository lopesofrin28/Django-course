# mylist=[1,2,3]
# mylist.append(4)
# print(mylist)
#
# print(type(mylist))
# print(type(200))


##########################################

# class Sample():
#     pass
#
# x=Sample()
# print(type(x))

############################################# OOP PART 2
#
# class Dog():
#     pass
#
# mydog=Dog()
# print(type(mydog))
################################################

# class Dog():
#
#     def __init__(self,breed):
#         self.breed=breed
#
#
#
# mydog=Dog(breed="lab")
# otherdog=Dog(breed="huskie")
# print(mydog.breed)
# print(otherdog.breed)

#################################################

# class Dog():
#
#     def __init__(self,breed,name):
#         self.breed=breed
#         self.name=name
#
#
#
# mydog=Dog(breed="lab",name="sammy")
# mydog1=Dog("labradoodle","sami")
# print(mydog.breed,mydog.name)
# print(mydog1.breed,mydog1.name)

##################################################

# class Dog():
#
#     #CLASS OBJECT ATTRIBUTE
#     species='mammal'
#
#     def __init__(self,breed,name):
#         self.breed=breed
#         self.name=name
#
#
#
# mydog=Dog(breed="lab",name="sammy")
# print(mydog.breed,mydog.name,mydog.species)

#################################################

# class Circle():
#     pi=3.14
#
#     def __init__(self,radius=1):
#         self.radius=radius
#
#     def area(self):
#         return self.radius*self.radius*Circle.pi
#
#     def set_radius(self,new_r):
#         self.radius=new_r
#
# myc=Circle(3)
# myc.set_radius(999)
# print(myc.area())

############################################################### OOP PART 3

############################## #INHERITANCE
# class Animal():
#
#
#     def __init__(self):
#         print("ANIMAL CREATED")
#
#     def whoAmI(self):
#         print("ANIMAL")
#
#     def eat(self):
#         print("Eating")
#
# class Dog(Animal):
#     def __init__(self):
#         #Animal.__init__(self)
#         print("DOG CREATED")
#
#     def bark(self):
#         print("WOOF")
#
#     def eat(self):
#         print("DOG EATING")

# mya=Animal()
# mya.whoAmI()
# mya.eat()

# myd=Dog()
# myd.whoAmI()
# myd.eat()
# myd.bark()


#SPECIAL METHODS

class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):
        return "Title:{},Author:{},Pages:{}".format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book has been destroyed")

b=Book("python","jose",200)
print(len(b))
print(b)        #prints the book
del b           #deletes the book















































































#
