#1
s = str('alabuga polytech')

print(s[2])

print(s[4])

print(s[05])

print(s[04])

print(s[02])

print(s[12])

print(s[-1])

print(s[-2])

print(len(s))
#2
s = 'lorem ipsum afuys gshgd'
print(s.count(' ')+1)
#3
s = 'Strokaafigennaya'
s1 = s[round(len(s)2)]
s2 = s[len(s)2]
print(s1 , s2)
#4
s = 'find fallen fame'

if s.count('f') == 1
    print(s.find('f'))
elif s.count('f') = 2
    print(s.find('f'), s.rfind('f'))
#5    
s = input()
s = s[s.find('h')] + s[s.rfind('h') + 1]
print(s)
#6   
print('1hgfd1'.replace('1', 'one'))
#7
print(input().replace('@', ''))
#8
s = input()
a = s[s.find('h') + 1] 
b = s[s.find('h') + 1s.rfind('h')]
c = s[s.rfind('h')]
s = a + b.replace('h', 'H') + c
print(s)
#9
a = int(input())
b = int(input())
if a  b
    print(a)
else
    print(b)
#10
x = int(input())
if x  0
    print(1)
elif x == 0
    print(0)
else
    print(-1)
#11
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0
    print('yes')
else
    print('no')
#12
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
    print('yes')
else
    print('no')
#13
a = int(input())
b = int(input())
c = int(input())
if a == b == c
    print(3)
elif a == b or b == c or a == c
    print(2)
else
    print(0)
#14
x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())
if x_1 == x_2 or y_1 == y_2
    print('yes')
else
    print('no')
#15
s = int(input())
a = int(input())
k = int(input())
if k  s  a and ((k % s == 0) or (k % a == 0))
    print('yes')
else
    print('no')
#16

a= int(input())
b = int(input())
x = int(input())
y = int(input())
if a  b
    a, b = b, a
if x = a  2
    x = a - x
if y = b  2
    y = b - y
if x  y
    print(x)
else
    print(y)
