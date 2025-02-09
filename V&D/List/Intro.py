"""
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in python used to store 
collections of data, the other 3 are Tuple,set and Dictionary, all with different quilities and usage.

rules Lists are Created using square brackets: 

"""

frineds = ["Apple","Orange",45,False,"Akash","Nitish"]
print(frineds)
print(frineds[4])
frineds[0] = "Mango"#Unlike Strings lists are mutable
print(frineds[0:5])

li = [23,43,32,12,55,33,43,22,56,87,54,53]
# li.sort()
# li.reverse()
li.insert(4,345)#Insert 345 such that its index in the list is 3
print(li.remove(12))
print(li)

# ************ To all Method in Python ********
"""
In Python, The list type has severals useful methods that allow you to manipule
and interact with lists.Here's a quick overview of some the most common list methods


"""
# append():Adds an element to the end of the list.
Student_names = ["Nitish","Satyam","Anshu","Murari","Bijendra"]
Student_names.append("Sunny")
print(Student_names)

# extend():Adds all elements from an iterable (Like another list) to the end of the list
Natural_No = [1,2,3,4,5,6,7,8,9,10]
Natural_No.extend([11,12,13,14,15,16,17,18,19,20])
print(Natural_No)
# insert():Inserts an element at a specific position in the list.
my_list = [1, 2, 4]
my_list.insert(2, 3)
print(my_list)  # Output: [1, 2, 3, 4]

# remove():Removes the first occurrence of  a specified value
#  if the value is not found , it raises a valueError.

Roomate = ["Prem","Anshu","Bhagat Bom","Rakesh"]
Roomate.remove("Bhagat Bom")
print(Roomate)
