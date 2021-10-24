#  Write a Python program to print the following string in a specific format (see the
# output).

# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# Twinkle, twinkle, little star,
# How I wonder what you are


# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


# 2. Write a Python program to get the Python version you are using


# import sys
# print("Your Python version is ",sys.version)


# 3. Write a Python program to display the current date and time.


# import datetime
# today = datetime.datetime.today()
# print ("Current date and time : ")
# print (today.strftime("%d-%M-%Y %H:%M:%S"))


# 4. Write a Python program which accepts the radius of a circle from the user and compute
# the area.


# radius = int(input("Enter Radius :"))
# area = 3.142 * radius * radius
# print(area)

# 5. Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.


# first_name = str(input("Enter Your First Name :"))
# last_name = str(input("Enter Your Last Name :"))
# print(last_name + " " + first_name)



# 6. Write a python program which takes two inputs from user and print them addition


# num1 = input("Enter First :")
# num2 = input("Enter Second :")
# rint = num1 + " " + num2
# print(rint)



# 7. Write a program which takes 5 inputs from user for different subject’s marks, total it
# and generate mark sheet using grades ?


# name = str(input("Please Enter Your Name :"))
# phy = int(input("Enter Your Physics Marks :"))
# chem = int(input("Enter Your Chemistry Marks :"))
# bio = int(input("Enter Your English Marks :"))
# maths = int(input("Enter Your Mathematics Marks :"))
# comp = int(input("Enter Your Computer Marks :"))
# result = phy + chem + bio + maths + comp
# print(name,"Your Total Marks is",result)
# per = float(result/500*100)
# print(name,"Your Percentage is",per)



# 8. Write a program which take input from user and identify that the given number is even
# or odd?


# num = int(input("Enter Number :"))
# if num % 2 == 0:
#     print("The Number is Even")
# else:
#     print("The Number is Odd")



# 9. Write a program which print the length of the list?

# thislist = ["apple", "banana", "cherry" , "strawberry"]
# print ("Number of items in the list = ", len(thislist))


# 10.Write a Python program to sum all the numeric items in a list?

# thislist = [ 1 , 2 , 3 , 4]
# b = sum(thislist)
# print (b)


# 11.Write a Python program to get the largest number from a numeric list.

# numbers = [1, 2, 3, 5, 9, 6, 101, 55, 7, 1, 3, 88, 99, 101, 6, 88, 66, 6, 101, 55, 1001]
# print(max(numbers))




# 12. Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Write a program that prints out all the elements of the list that are less than 5.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# new_list = []

# for item in a:
#     if item < 5:
#         new_list.append(item)
# print(new_list)