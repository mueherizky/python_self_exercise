'''
Python Exercise 
Link ==> https://www.w3resource.com/python-exercises/python-basic-exercises.php
'''

### NUMBER 1
# print('''
# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are
# ''')

### NUMBER 2
# import sys
# print("Python version")
# print(sys.version)
# print("Version info.")
# print(sys.version_info)

### NUMBER 3
# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))

### NUMBER 4
# from math import pi
# r = float(input('How many radius want you insert? '))
# area = pi * r ** 2
# print((f'{area:.2f}'))

### NUMBER 5
# first_name = input('Input your first name: ')
# last_name = input('Input your Last Name: ')
# print(f"Hello {last_name} {first_name}")

### NUMBER 6
# number = input('Give me many numbers separated by comma \n ==> ').split(',')
# print(f"List: {number}")
# print(f"Tuple: {tuple(number)}")

### NUMBER 7
# filename = input('''
# Input your file name and extension! 
# Like this "cool.exe"
# ==> ''')
# extension = filename.split('.')
# print(f"Your file extension is {extension[-1]}")

### NUMBER 8
# color_list = ["Red","Green","White" ,"Black"]
# print(f"Your first color is {color_list[0]} and Your last color is {color_list[-1]}")

### NUMBER 9
# exam_st_date = (11, 12, 2014)
# print(f"The examination will start from: %i / %i / %i"%exam_st_date)

### NUMBER 10
number = int(input("Input one number to see the result: \n ==> "))
print('Formula i used " n + nn + nnn ... "')
for num in number:
    number += num
