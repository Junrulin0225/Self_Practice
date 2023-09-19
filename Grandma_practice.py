# #製作BMI計算機: 資料型態轉換, round四捨五入, f-string,\n表換行
# height = float(input('please enter your height:'))
# weight = float(input('please enter your weight:'))
# height = height/100
# BMI = weight / height**2
# BMI = round(BMI, 1)
# if BMI < 18.5:
#     print(f'your BMI is {BMI}, you are too light!')
# elif BMI < 24:
#     print(f'your BMI is {BMI}, you are healthy!')
# else:
#     print(f'your BMI is {BMI}, you need to lose weight!')


#print(f'your BMI is {BMI}' )


# num = float(input('please enter an integer:'))
# if num%2 == 0:
#     print('it is an odd number')
# else:
#     print('it is not odd')

#Create a meal order machine
# print('welcome to The Puapoo')
# choose_burger_first = input('please pick the burger you want (enter 1,2 or 3):\n(1) NTD100 chicken burger\n(2) NTD120 beef burger\n(3) NTD80 vegan burger\n' )
# add_meal = input('add meal? (enter y or n):').lower()
# add_drinks = input('add drinks? (enter y or n):').lower()

# initial_bill = 0
# if choose_burger_first == '1':
#     initial_bill= initial_bill + 100
# elif choose_burger_first == '2':
#     initial_bill= initial_bill + 120
# else:
#     initial_bill= initial_bill + 80

# if add_meal =='y':
#     initial_bill = initial_bill + 50
# else:
#     initial_bill = initial_bill
# if add_drinks=='y':
#     initial_bill = initial_bill + 30
# else:
#     initial_bill = initial_bill

# print (f'total price = : { initial_bill}')

# create puapoo family member info
# def print_info(name, gender, age, nationality, species, hobby, address):
#     print(f'name:{name}\ngender:{gender}\nage:{age}\nnationality:{nationality}\nspecies:{species}\nhobby:{hobby}\naddress:{address}')
        
# print_info('nunu', 'M', 4, 'Japan', 'light blue penguin', 'sleep and miss peng peng', 'Beblo and Candy home')

# print_info('nono', 'M', 2, 'Japan', 'light blue penguin', 'top gun style flying and be clingy to Beblo', 'Beblo and Candy home')


# #找出最大值
# def find_max(n1,n2,n3):
#     if n1 > n2 and n1 > n3:
#         return(n1)
#     elif n2 > n1 and n2 > n3:
#         return(n2)
#     else:
#         return(n3)
# #找出最小值
# def find_min(n1,n2,n3):
#     if n1 < n2 and n1 < n3:
#         return(n1)
#     elif n2 < n1 and n2 < n3:
#         return(n2)
#     else:
#         return(n3)
# #定義一個函式: 最大減去最小值
# def max_min(n1,n2,n3):
#     if type(n1)!=int or type(n2)!=int or type(n3)!=int:
#         return('enter an integer!')
#     else:
#         return find_max(n1,n2,n3) - find_min(n1,n2,n3)

# print(max_min(3,10,3))

# A = [[1,2,3],[3,4,5],[5,6],[8],[9,10]]
# for row in A:
#     for col in row:
#         print(col)

























