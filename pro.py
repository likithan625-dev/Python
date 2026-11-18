"""
s="hello"
print(s.upper())

ch=input("enter the characters:")
if 'A'<=ch<='Z':
    print("It is a uppercase")
elif 'a'<=ch<='z':
    print("It is a lowercase")
elif '0'<=int(ch)<='9':
    print("it is a digit")
else:
    print("it is a special character")

ch=input("enter the characters:")
if ch.isalpha():
    if ch in "aeiouAEIOU":
        print("It is a vowel")
    else:
        print("It is a consonant")
else:
    print("It is not an alphabet")

l=eval(input("enter the list:"))
if type(l)==list:
    if len(l)%2==0:
        print(l)
    else:
        print("it is a list")
else:
    print("it is not a list")

ch=1
while ch<=5:
    print("hello")
    ch+=1

l=eval(input("enter the list:"))
i=0
while i<len(l):
        print(l[i])
        i+=1

n=int(input("enter the number:"))
rev=0
while n>0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
print("the reverse of the number is:",rev)

for i in range(5):
    print("hello")

s=input("enter the string:")
output=""
for i in s:
    if 'A'<=i<='Z':
        output=output+chr(ord(i)+32)
    else:
        output+=i
print("output string is:",output)

s=[12,10,'hello','Good',5j,'Bye']
out={}
for i in s:
    if type(i)==str:
        out[i]=i[0]+i[-1]
print(out)

for i in range(1,6):
    for j in range(1,6):
     print('*', end='')
    print()

def convert():
    s=input("enter the string:")
    output=""
    for i in s:
        if 'A'<=i<='Z':
            output=output+chr(ord(i)+32)
        else:
            output+=i
    print("output string is:",output)
convert()

def add(a,b):
    print("the sum is:",a+b)
add(10,20)"""

def add(a,b):
    return a+b
print("the sum is:",add(10,20))