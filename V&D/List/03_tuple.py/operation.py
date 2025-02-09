
"""
Concatination(+):
You can concatenate two or more tuples together using the + oprator.

Below example
"""
Politician_Name =("Narendra Modi","Amit shah","Yogi Aditya Nath","Nitish Kumar","Lalu Yadev")
Cricket_player =("Rohit Sharma","Virat Kohli","Sachin Tendulkar","MS Dhoni")
print(Politician_Name+Cricket_player)

"""
Operation Repetition(*)
You can repeat a tuple multiple times using the operator
"""

my_brother = ("Bijendra kumar","Golu Kumar","Banti Kumar")
print((my_brother)*3)

"""
Operation third
Membership Test (in and not in)
You can check if an element exists in a tuple using the in operation or check if it does not exist using not in.



*****
In Python, tuples are immutable sequences,
and you can perform various operations on them. 
Here are some common tuple operations:
"""

"""
Slicing a Tuple in Python:
Slicing allows you to extract a protion of tuple using the syntax:
tuple[start:stop:step]
.Start-The index where the slice begins(inclusive)
.Stop-The index where the slice ends(exclusive).
.Step-The step size for skipping elements(optional)


"""
teacher_name = ("Shailesh Verma","Yogendra Kumar","Jitendra Kumar","shailendra Kumar","Kishan Kumar","Bijendra KUmar")
print(teacher_name[1:3])

"""
Accessing Elements
Description:You can access element using indexing
(Starting from 0 for positive and -1 for negative).

"""
table = (2,4,6,8,10,12,14,16,18,20)
print(table[1])
print(table[-1])

"""
Tuple Unpacking:
Description:Assign tuple element to multiple variables.

"""
Table_3 =(3,6,9,12,15,18,21,24,27,30)
a,b,c,d,e,f,g,h,i,j = Table_3
print(a,b,c,d,e,f,g,h,i,j)

"""
Finding Index of an Element
Description:Returns the first occurrence index of an element using index().

"""
Non_veg = ("Chiken","Egg","Fish","Mutton")
print(Non_veg.index("Mutton"))

"""
Counting Occurrances
Description:Counts how many times an element appers using count().

"""
Lett_c = (23,43,42,334,54,34,67,33,44,555,32,45,65,33)
print(Lett_c.count(33))

"""
Iterating Through a tuple
Description:loops through a tuple using a for loop.
 Example below
 """
t = (10, 20, 30,40,50,60,70,80,90,100)
for i in t:
    print(i)
# Output:
# 10
# 20
# 30

"""
Converting List to Tuple
Description:Use tuple() to convert a list a tuple
Below Example
"""
lst = [23,34,23,55,4,56,764,4,5,77]
bin = tuple(lst)
print(bin)

"""
Converting tuple to list
Description:Use list() to convert a tuple to a list.
Below the example
"""
bant = (2,343,456,65,43,678,76,554)
golu = list(bant)
print(golu)


"""
Deleting a tuple
Description:Tuples are immutable, but you can delete an entire tuple using del.

"""
Rakesh  = (23,44,34,56,76,84,35)
del Rakesh

