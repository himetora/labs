"""
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
"""

"""
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
"""

"""
list1 = ["abc", 34, True, 40, "male"]
"""

"""
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
"""

"""
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
"""

"""
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
"""

"""
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
"""

"""
Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
"""

"""
"This example returns the items from the beginning to, but NOT including, "kiwi" "

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
"""

"""
This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
"""

"""
This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
"""

"""
Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

"""

"""
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
"""

"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
    
"""

"""
Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

"""

"""
Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

"""

"""
Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


"""

"""
Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) 

"""

"""
Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
"""

"""
Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

"""

"""
Remove the first occurance of "banana":

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

"""

"""
Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
"""

"""
Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
"""

"""
Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

"""

"""
Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist
"""

"""
Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
"""

"""
Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
"""

"""
Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
"""

"""
A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
"""

"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

"""

"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
"""

"""
Only accept items that are not "apple":

newlist = [x for x in fruits if x != "apple"]
"""

"""
With no if statement:

newlist = [x for x in fruits]
"""

"""
You can use the range() function to create an iterable
newlist = [x for x in range(10)]
"""

"""
Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]
"""

"""
Set the values in the new list to upper case:

newlist = [x.upper() for x in fruits]
"""

"""
Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]
"""

"""
Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]
"""

"""
Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
"""

"""
Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
"""

"""
Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
"""

"""
Sort the list descending:

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
"""

"""
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
"""

"""
Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
"""

"""
Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
"""

"""
Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
"""

"""
Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
"""

"""
Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
"""

"""
Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
"""

"""
Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
"""

"""
Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
"""

"""
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

"""

  Exercise:

"""

"""
Print the second item in the fruits list.


fruits = ["apple", "banana", "cherry"]
print(fruits[1])
"""

"""
Change the value from "apple" to "kiwi", in the fruits list.


fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

"""

"""
Use the append method to add "orange" to the fruits list.


fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
"""

"""
Use the insert method to add "lemon" as the second item in the fruits list.


fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
"""

"""
Use the remove method to remove "banana" from the fruits list.


fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

"""

"""
Use negative indexing to print the last item in the list.


fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
"""

"""
Use a range of indexes to print the third, fourth, and fifth item in the list.


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
"""

"""
Use the correct syntax to print the number of items in the list.


fruits = ["apple", "banana", "cherry"]
print(len(fruits))
"""
