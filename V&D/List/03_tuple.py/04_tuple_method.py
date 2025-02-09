tuple = (2,34,54,77,False,"Nitish","Anurag","Banti")
print(tuple)
Is_present  =tuple.count("Bijendra")
print(Is_present)

""" **** second method******
Index()
This method returns the index of the first occurrence of the specified element.
syntax:tuple.index(element)

"""
Fruits_name = ("Mango","Banana","Gauvbha","PineApple","Orange","Apple")
print(Fruits_name.index("Banana"))

# Note that i the element is not found, a ValueError will be raised.

"""
Third Method len()
Through not exclusive to tuples, len() is commonly used to get the number of element in a tuple
Syntax
len(tuple)

"""

Indian_player = ("Virat Kohli","Rohit Sharma","Sachin Tendulkar","MS Dhoni","HArdik Pandya")
print(len(Indian_player))

"""
Four Method:min() and max()
Again, not exclusive to tuples,but useful for findinf the 
minimun ans maximum values in the tuple.
Syntax:
min(tuple)
max(tuple)
"""
letters = ("a","b","s","g","r","y","w","q",)
print(min(letters))
print(max(letters))

"""
Fift method sum():
You can use the sum() function to get the sum of all elements iin the tuple, as long as the elements are numeric.
Syntax:
sum(tuple):
these methods help you interact with tuples in useful
ways! let me know if you want more examples or have
specific questions about them!
"""

Number = (2,3,4,23,5,654,57,864)
print(sum(Number))

