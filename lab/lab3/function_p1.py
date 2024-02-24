#ex1

def func(grams):
    ounces = grams * 28.3495231 
    print(ounces)
func(2)

#ex2

def temp(fahren):
    cels = (5/9) * (fahren - 32)
    print(cels)
temp(13)

#ex3

def farm(heads, legs):
    rab = (legs - 2 * heads)//2
    chick = heads - rab
    print("chicken =", chick, "rabbits =", rab)
farm(35, 94)

#ex4

def check_prime(i):
  for x in range(2, i):
      if i % x == 0:
         return False
  return True

lis = [1, 3, 4, 5, 8, 12, 11]      
def filter_prime(some_list):
  arr = []
  for i in some_list:
    if check_prime(i) == True:
        arr.append(i)
  return arr
lis1 = filter_prime(lis)

#ex5

from itertools import permutations
st = input("input the string you want to permutate - ")
list1 = list(permutations(st))
for x in list1:
  print(x)

#ex6
  
string = 'abd fre der'
def Convert(string):
  li = list(string.split(" "))
  print(*li[::-1])
Convert(string)

#ex7

def has_33(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 3 and nums[i+1] == 3:
       return True
  return False

has_33([1, 3, 3]) #→ True
has_33([1, 3, 1, 3]) #→ False
has_33([3, 1, 3]) #→ False

#ex8

def spy_game(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 0:
      count += 1
    if count == 2 and nums[i] == 7:
      return True
    elif count != 2 and nums[i] == 7:
      return False
  return False

print(spy_game([1,2,4,0,0,7,5])) #--> True
print(spy_game([1,0,2,4,0,5,7])) #--> True
print(spy_game([1,7,2,0,4,5,0])) #--> False

#ex9

def Volume(rad):
  print(4/3 * 3.14 * rad**3)
Volume(3)

#ex10

def uniqe(smth):
  for i in range(len(smth)):
    for j in range(i + 1, len(smth)):
      if smth[j] == smth[i]:
        smth[j] = -1
  arr = []
  for i in smth:
    if i != -1:
      arr.append(i)
  return arr
smth = [1, 1, 1, 1, 3, 3, 4, 5, 6, 7, 7, 8]
print(*uniqe(smth))


#ex11

def ispalindrome(word):
  copy = word[::-1]
  if copy == word:
    return True
  return False
print(ispalindrome("abbad")) #false
print(ispalindrome("abba")) #true

#ex12

def histogram(arr):
  for i in arr:
    strin = '*'
    print(strin * i)
histogram([3, 4, 2])


#ex13

import random
def guess():
  number = random.randint(1, 21)
  name = input("Hello! What is your name?\n")
  print("Well, "+ name + ", I am thinking of a number between 1 and 20.\n")
  count = 0
  for i in range(20):
    count += 1
    x = int(input("Take a guess.\n"))
    if x < number:
      print("Your guess is too low.\n")
    elif x > number:
      print("Your guess is too high.")
    elif x == number:
      print("Good job, " + name +", You guessed my number in "+ str(count)+ " guesses!")
      break
guess()
