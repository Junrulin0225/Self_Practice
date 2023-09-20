###HW WEEK 1
##HW1 1. Number size -> complete!
# num = input('Please enter three numbers, float or int: ').split()

# for n in num:
#     n = float(n)
#     if n == max(num):
#         print(n)
# print(n)
##HW1 2. 

#HW1 3. Temperature Convert -> complete!
# F = C * 1.8 + 32
# C = 5/9(F - 32)

# user = input('Please enter "C to F" or "F to C" , the number you want to calculate : ').split(',')
# user[1] = float(user[1])
# if user[0] =='C to F':
#     temperature = user[1] * 1.8 + 32
#     print(round(temperature,2))
# elif user[0] == 'F to C':
#     temperature = 5/9 * (user[1] - 32 )
#     print(round(temperature,2))
# else:
#     print('Invalid')

##HW1 4. Discount Calculator -> complete!
# cost = float(input('Please enter your cost: '))

# if cost > 100.00:
#     tip = cost * 0.10
#     total_cost = cost - tip
#     print(cost,  tip, total_cost )
# else:
#     print(cost, 0.00, cost)


##HW1 5. Password Strength Checker -> complete!
# user = input('Please enter a password:')
# if len(user) < 6:
#     print('Weak')
# elif 6 < len(user) < 10:
#     print('Moderate')
# else:
#     print('Strong') 


#懷元solution
import math
# 1
print(f"{max([float(i) for i in input('please input 3 numbers: ').split()]):.2f}")

# 2
a, b, c = [float(i) for i in input('please input a b c: ').split()]
tmp = math.sqrt(b * b - 4 * a * c)
if tmp == 0:
    x = -b / (2 * a)
    print(f'{x:.3f}')
else:
    x = [(-b + tmp) / (2 * a), (-b - tmp) / (2 * a)]
    print(' '.join([f'{i:.3f}' for i in x]))

# 3
mode, t = input('please input condiction and temperature: ').split(',')
if mode == 'C to F':
    f = float(t) * 9 / 5 + 32
    print(f'{f:.2f}')
elif mode == 'F to C':
    c = float(t) - 32 * 5 / 9
    print(f'{c:.2f}')
else:
    print('Invalid')

# 4
price = float(input('please input price: '))
if price > 100:
    discount = price * 0.1
    print(f'{price:.2f} {discount:.2f} {price - discount:.2f}')
else:
    print(f'{price:.2f} 0.00 {price:.2f}')

# 5
password_len = len(input('please input password: '))
if password_len < 6:
    print('Weak')
elif password_len <= 10:
    print('Moderate')
else:
    print('Strong')







###HW WEEK 2

#HW 2.1  -> complete!
num = float(input('Enter a number : '))
if num % 2 == 0:
    print('even')

elif num != int(num):
    print('This number is not an integer.')

else:
    print('odd')


#HW 2.2 -> complete!
num = input('').split() 
if num[0] > num[1]:
    print(num[0])
else:
    print(num[1])



#HW 2.3 Leap Year or not -> complete!
year = int(input(''))
if year % 400 == 0:
    print('Leap year')
elif year % 100 == 0:
    print('Not a leap year')
elif year % 4 == 0:
    print('Leap year')
else:
    print('Not a leap year')
