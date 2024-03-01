import re
#1
f = open(r"C:\Users\Хима\labs\lab5\row.txt", encoding="utf8")
cont = f.read()
x = re.findall("ab*", cont)
print(x)

#2
f = open(r"C:\Users\Хима\labs\lab5\row.txt", encoding="utf8")
cont = f.read()
x = re.findall("ab{2,3}", cont)
print(x)

#3
f = open(r"C:\Users\Хима\labs\lab5\row.txt", encoding="utf8")
cont = f.read()
x = re.findall("[a-z]_", cont)
print(x)

#4
f = open(r"C:\Users\Хима\labs\lab5\row.txt", encoding="utf8")
cont = f.read()
x = re.findall("[A-Z][a-z]", cont)
print(x)

#5
f = open(r"C:\Users\Хима\labs\lab5\row.txt", encoding="utf8")
cont = f.read()
x = re.findall("a.*b", cont)
print(x)

#6
f = open(r"C:\Users\Хима\labs\lab5\row.txt", encoding="utf8")
cont = f.read()
ans = re.sub("[ ,.]", ":", cont)
print(ans)

#7
f = open(r"C:\Users\Хима\labs\lab5\row.txt", encoding="utf8")
cont = f.read()
ans = re.sub("[_]", "", cont)
print(ans)

#8
f = open(r"C:\Users\Хима\labs\lab5\row.txt", encoding="utf8")
cont = f.read()
ans = re.split("[A-Z]", cont)
print(ans)

#9
f = open(r"C:\Users\Хима\labs\lab5\row.txt", encoding="utf8")
cont = f.read()
ans = re.sub("(?<!^)(?=[A-Z])", " ", cont)
print(ans)

#10
f = open(r"C:\Users\Хима\labs\lab5\row.txt", encoding="utf8")
cont = f.read()
def camel_to_snake(something):
    return re.sub(r'([A-Z])', r'_\1', something).lower().lstrip('_')
snake_case_str = camel_to_snake(cont)
print(snake_case_str)