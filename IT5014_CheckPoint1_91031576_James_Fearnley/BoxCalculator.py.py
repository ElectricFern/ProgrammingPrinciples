# BoxCalculator.py
# James Fearnley
# 15/11/2018


# Defining Box Size Variables,
big_box = 5
medium_box = 3
small_box = 1

print("Welcome to the box calculator. \n")

# Initial user directed input request
user_input = int(input("Please enter the number of watermelon you would like to put into boxes: \n"))

# Calculations on User_Input using // for number of full boxes and % for overflow
# Case study of 0, 1, 4, 7, 9, and 1004 melons

# Big Box Calculations
big_required = user_input // big_box
big_overflow = user_input % big_box

# Medium Box Calculations
medium_required = big_overflow // medium_box
medium_overflow = big_overflow % medium_box

# Small Box Calculation
small_required = medium_overflow // small_box

# Output message
print(big_required, "Big boxes were used")
print(medium_required, "Medium boxes were used")
print(small_required, "Small boxes were used")

# Exit option for closing in windows terminal
input('Press ENTER to exit')


"""Case study for testing program:
I chose 0, a larger number, and numbers to test each box type and combinations of different box types:

Case 1 - User enters 0: I would expect 0 for all three sizes;
Welcome to the box calculator. 

Please enter the number of watermelon you would like to put into boxes: 
0
0 Big boxes were used
0 Medium boxes were used
0 Small boxes were used
Press ENTER to exit

Case 3 - User enters 1: I would expect 1 small box to be used only;
Welcome to the box calculator. 

Please enter the number of watermelon you would like to put into boxes: 
0
0 Big boxes were used
0 Medium boxes were used
1 Small boxes were used
Press ENTER to exit

Case 4 - User enters 4: I would expect one small box and one medium box to be used only;
Welcome to the box calculator. 

Please enter the number of watermelon you would like to put into boxes: 
4
0 Big boxes were used
1 Medium boxes were used
1 Small boxes were used
Press ENTER to exit

Case 5 - User enters 7: I would expect one big box and two small boxes only;
Please enter the number of watermelon you would like to put into boxes: 
7
1 Big boxes were used
0 Medium boxes were used
2 Small boxes were used
Press ENTER to exit

Case 6 - User enters 9: I would expect one of each box only;
Welcome to the box calculator. 

Please enter the number of watermelon you would like to put into boxes: 
9
1 Big boxes were used
1 Medium boxes were used
1 Small boxes were used
Press ENTER to exit

Case 7 - user enters 1004: I would expect 200 big, one medium and one small box to be full;
Welcome to the box calculator. 

Please enter the number of watermelon you would like to put into boxes: 
1004
200 Big boxes were used
1 Medium boxes were used
1 Small boxes were used
Press ENTER to exit
"""