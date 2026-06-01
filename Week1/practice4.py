a= """I'am the python developer 
and i have the 4 years experience.  """
print(a)

x=1
y=2.8
z=1j
print(type(x))
print(type(y))
print(type(z))

#List example
list = ["apple","mango","orange"]
print(list)
print(list[1])
print(list[1:3])

#tuple
mytuple =("ishtiaq","ahmed","umer")
print(mytuple[1])

#dictoniry
thisdict={
    "brand": "sony",
    "price": 2000,
    "year": 1964
}
print(thisdict)
print(thisdict["brand"])

#set, frozen set
thisset = {"apple","banna","orange"}
thisset.add("melon")
#update use for multiple item
thisset.update(["watermellon","appricot"])
thisset.remove("appricot")
print(thisset)

#boolean
print(10>9)
print(20>30)