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