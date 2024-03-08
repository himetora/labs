#1
def multiply(list):
    result = 1
    for number in list:
        result *= number
    return result
list = [1, 2, 3, 4, 5]
result = multiply(list)
print("answer:", result)

#2
def counter(strr):
    uppers = 0
    lowers = 0
    for i in strr:
        if i.isupper():
            uppers += 1
        elif i.islower():
            lowers += 1
    return f"Uppercase letters: {uppers}, Lowercase letters: {lowers}"
strr = input()
print(counter(strr))

#3
def palindrome(strr):
    copy = strr[::-1]
    if strr == copy:
        return f"{strr} is palindrome"
    else:
        return f"{strr} is not palindrome"
strr = input()
print(palindrome(strr))

#4
import time, math
def idnk(number,milisec):
    second = milisec/1000
    time.sleep(second)
    answer = math.sqrt(number)
    return answer
number = float(input("Your number: "))
milisec = int(input("Time delay: "))
result = idnk(number,milisec)
print(result)

#5
def check_tuple_elements_true(zxc):
    return all(zxc)
my_tuple = (True, 1, "abc")
print(check_tuple_elements_true(my_tuple))