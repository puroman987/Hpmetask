# 21.03.
# Task 1
n = int(input('Computer count: '))
display_price = 100
system_unit_price = 200
print(n * (display_price + system_unit_price))

# Task 2
tanya_age = int(input("Tanya's age is: "))
mytya_age = int(input("Mytya's age is: "))
summ = (tanya_age + mytya_age) / 2
print(summ)
st = summ - tanya_age
sm = summ - mytya_age
if st < 0:
    st *= -1
    print(st)
    print(sm)
elif sm < 0:
    sm *= -1
    print(st)
    print(sm)
elif st == 0:
    print("Tanya's age is equals Mytya's age")
else:
    print(summ - tanya_age)
    print(summ - mytya_age)

# Task 3
step = False
attack = False
xf1 = int(input('Start cord X: '))
yf1 = int(input('Start cord Y: '))
xf2 = int(input('Finish cord X: '))
yf2 = int(input('Finish cord Y: '))
xl = int(input('Cord X of figure: '))
yl = int(input('Cord Y of figure: '))
if xf1 - yf1 == xf2 - yf2 or xf1 == xf2 or yf1 == yf2:
    step = True
if step == True and xf2 == xl and yf2 == yl:
    attack = True

# Task 4
a = -1
b = -1
while (a and b) not in range(11):
    a = int(input('Enter first num: '))
    b = int(input('Enter second num: '))
    if (a and b) not in range(11):
        print('Entered num are not include in range 0-10')
    else:
        print(a * b)

# Task 5
import random
x = random.randint(0, 101)
tri = 101
while tri != x:
    tri = int(input('Enter your num:' ))
    if tri > x:
        print('Too big num')
    elif tri < x:
        print('Too small num')
    else:
        print("You're guessed!")

# Task 6
n = int(input())
count = 0
m = 0
while m != n:
    m += 1
    if m % 2 != 0:
        count += m
    else:
        continue
print(count)

# Task 7
n = int(input('Enter your num: '))
m = 0
chet = 0
nechet = 0
while n / 10 >= 1:
    if (n % 10) % 2 == 0:
        chet += 1
    else:
        nechet += 1
    n //= 10
    m += 1
print(chet, nechet)


# Task 8
import random
n = int(input())
arr = [random.randint(0, n) for i in range(200)]
print(arr)
arr.sort()
print(arr[0], arr[-1])

# Task 9
import random
m = int(input())
arr = list([random.randint(-500, m) for i in range(200)])
neg =[]
pos = []
for i in arr:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)
print(neg)
print(pos)

# Task 10
import random
arr = list([random.randint(-500, 500) for i in range(200)])
new = []
for i in arr:
    if i % 2 == 0 and arr[i % 2 != 0]:
        new.append(arr.index(i))
print(new)
# Посмотри 10 задание не уверен в правильности



































