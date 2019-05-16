# GradeCalculator.py
# James Fearnley
# 16/11/2018

# Introducing the program
print("Welcome to the Final Grade Calculator")

# Requesting and obtaining user input, floats for half marks.
project_mark = float(input("Enter your Project mark total out of 72 here: "))
exam_mark = float(input("Enter your Exam mark total out of 112 here: "))

# Calculation Project mark to percentage
project_percentage = ((project_mark / 72) * 100)

# Calculation Exam mark to percentage
exam_percentage = ((exam_mark / 112) * 100)

# Output message for percentages
print("You achieved", project_percentage, "% in your Project")
print("You achieved", exam_percentage, "% in your Exam")

# Calculation Overall percentage
avg_percent = (exam_percentage + project_percentage) / 2

# Output message for overall percent
print("You achieved", avg_percent, "% for your Average Percentage")

# Percentage to grade statements
if avg_percent >= 0 and avg_percent < 50:
    print("Scored below 50% assigned: Fail")
elif avg_percent >= 50 and avg_percent <= 59:
    print("Scored between 50% and 59% assigned: D")
elif avg_percent >= 60 and avg_percent <= 69:
    print("Scored between 60% and 69% assigned: C")
elif avg_percent >= 70 and avg_percent <= 79:
    print("Scored between 70% and 79% assigned: B")
elif avg_percent >= 80:
    print("Scored above 80% assigned: A")
else:
    print("You entered marks incorrectly please try again")

# Exit option for closing in windows terminal
input('Press ENTER to exit')

"""Case study for testing program:
I will try 0, half marks, and a nearly 100% grade:

Case 1: User did not attend and got 0 for all marks;
I would expect 0% for all three returned results and a fail mark;

Welcome to the Final Grade Calculator
Enter your Project mark total out of 72 here: 0
Enter your Exam mark total out of 112 here: 0
You achieved 0.0 % in your Project
You achieved 0.0 % in your Exam
You achieved 0.0 % for your Average Percentage
Scored below 50% assigned: Fail
Press ENTER to exit

Case 2: User achieved 36.5 for project and 80 for exam;
I would expect 50.7%, 71.4%, and 61.0% respectively with a C grade;

Welcome to the Final Grade Calculator
Enter your Project mark total out of 72 here: 36.5
Enter your Exam mark total out of 112 here: 80
You achieved 50.69444444444444 % in your Project
You achieved 71.42857142857143 % in your Exam
You achieved 61.06150793650794 % for your Average Percentage
Scored between 60% and 69% assigned: C
Press ENTER to exit
 
Case 3: User achieved 70 and 110 with an A grade;

Welcome to the Final Grade Calculator
Enter your Project mark total out of 72 here: 36.5
Enter your Exam mark total out of 112 here: 80
You achieved 50.69444444444444 % in your Project
You achieved 71.42857142857143 % in your Exam
You achieved 61.06150793650794 % for your Average Percentage
Scored between 60% and 69% assigned: C
Press ENTER to exit

Case studies finished and all tests were successful.
"""