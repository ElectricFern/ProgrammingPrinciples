# BingoGame.py
# By James Fearnley
# 16/11/2018

# Defined variables and lists
bingo_card = [7, 26, 40, 58, 73, 14, 22, 34, 55, 68]
bingo_card_i = [7, 26, 40, 58, 73, 14, 22, 34, 55, 68]
cells_left = len(bingo_card)

# Generic intro message
print('''Welcome to the game of Bingo. 
The numbers you can choose are 1-80 inclusive.
If you 'hit' you have a match with the bingo card.
You will receive a BINGO message when all 10 numbers have been chosen.
''')

# Outer loop condition if list is empty = bingo and end
# Inner loop matches list with user input if = true then hit and remove list item
while len(bingo_card) > 0:
    user_input = int(input("Enter a number from 1-80: "))
    for item in bingo_card:
        if user_input == item:
            print(item, "hit")
            bingo_card.remove(item)
            print(len(bingo_card), "more to go")
            break
        else:
            print("miss, your number is not on the card")
            continue

# End the game messages, and exit
print("BINGO!!!")
print("The numbers of the winning card were", bingo_card_i)
input('Press ENTER to exit')

"""Case study testing of program:
First I will test all the numbers on the card to test the outer loop for the bingo message.
Then I will test some numbers not on the card to be sure the user message "miss" displays.

First case:
Welcome to the game of Bingo. 
The numbers you can choose are 1-80 inclusive.
If you 'hit' you have a match with the bingo card.
You will receive a BINGO message when all 10 numbers have been chosen.

Enter a number from 1-80: 7
7 hit
9 more to go
Enter a number from 1-80: 26
26 hit
8 more to go
Enter a number from 1-80: 40
40 hit
7 more to go
Enter a number from 1-80: 58
58 hit
6 more to go
Enter a number from 1-80: 73
73 hit
5 more to go
Enter a number from 1-80: 14
14 hit
4 more to go
Enter a number from 1-80: 22
22 hit
3 more to go
Enter a number from 1-80: 34
34 hit
2 more to go
Enter a number from 1-80: 55
55 hit
1 more to go
Enter a number from 1-80: 68
68 hit
0 more to go
BINGO!!!
The numbers of the winning card were [7, 26, 40, 58, 73, 14, 22, 34, 55, 68]
Press ENTER to exit

Second case:
Enter a number from 1-80: 72
miss, your number is not on the card
miss, your number is not on the card
miss, your number is not on the card
miss, your number is not on the card
miss, your number is not on the card
miss, your number is not on the card
miss, your number is not on the card
miss, your number is not on the card
miss, your number is not on the card
miss, your number is not on the card
Enter a number from 1-80: 70
miss, your number is not on the card
miss, your number is not on the card
miss, your number is not on the card
miss, your number is not on the card
miss, your number is not on the card
miss, your number is not on the card
miss, your number is not on the card
miss, your number is not on the card
miss, your number is not on the card
miss, your number is not on the card
Enter a number from 1-80:

Case tests were successful after a miss the option to continue works as do the user messages. 
"""