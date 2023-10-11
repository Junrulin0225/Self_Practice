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



#HW 2.4 Vowel or Consonant -> complete!

vowel_list = ['a', 'e', 'i', 'o', 'u']
letter = input('')
if letter in vowel_list:
    print('Vowel')
else:
    print('Consonant')



#HW 2.5 Positive, negative or zero -> complete!
num = int(input(''))
if num > 0:
    print('Positive')
elif num < 0:
    print('Negative')
elif num == 0:
    print('zero')


#HW 2.6 Check the digits -> complete!
user = input('')
if user.isdigit() == True:
    print(f'Contain only digits, {len(user)} ')
else:
    print(f'Does not ontain only digits, {len(user)} ')


#HW 2.7 calculate student's grade based on the criteria
score = float(input(''))
if score != int(score) or score > 100 or score < 0:
    print('Error')
elif 90 <= score < 100:
    print(int(score), 'A')
elif 80 <= int(score) < 90:
    print(int(score), 'B')
elif 70 <= int(score) < 80:
    print(int(score), 'C')
elif 60 <= int(score) < 70:
    print(int(score), 'D')
elif int(score) < 60:
    print(int(score), 'E')
    
#HW 2.8 covert the sec to day:hr:min:sec  -> not yet!

###HW WEEK 3
#HW 3.1 -> python tutor can work but doesn't work on VS
num_list= input('').split(' ')
max_num = num_list[0]
for num in num_list:
    if num > max_num:
        max_num = num
print(max_num)


#HW 3.2 -> 懷元solution
is_digit = True
for i in input('please type a string: '):
    if i not in '0123456789':
        is_digit = False
        break
if is_digit:
    print('digit')
else:
    print('not digit')
 
#HW 3.3 -> complete!
import math
num = int(input('Enter a number: '))
print(math.factorial(num))

#HW 3.4 -> 'reverse the word' -> not sure how to use the while loop here... but it still works.
user = str(input('Please enter a string: '))
print(user[::-1])


#HW 3.5 -> 'set up a password' -> not sure how to use the dic here... but it still works.
set_again = True
 
while set_again:
    password = input('Please enter a new password: ')
    if len(password) >= 8 and any([n.isupper() for n in list(password)]) and any([n.islower() for n in list(password)]) and any([n.isdigit() for n in list(password)]):
        print('The password is strong.')  
        break
                 
    elif len(password) <= 8:
        True
        print('The password is weak.')
    else:
        True
        print('Please make sure to match the criteria.')


#HW 4.1-> calculator with function -> complete! must have simpler codes!
user_enter = input('Please enter num1, operator, num2: ').split(' ')
num1 = float(user_enter[0])
num2 = float(user_enter[2])
def add(a,b):
    print(a + b)
def subtract(a,b):
    print(a - b)
def multiply(a,b):
    print(a * b)
def divide(a,b):
    print(a / b)

if int(user_enter[1]) == 1:
    add(a = num1,b= num2)
elif int(user_enter[1]) == 2:
    subtract(a = num1,b= num2)
elif int(user_enter[1]) == 3:
    multiply(a = num1,b= num2)
elif int(user_enter[1]) == 4:
    if num2 == 0:
        print('Cannot divide by zero.')
    else:
        divide(a = num1,b= num2)
else:
    print('Invalid choice')
