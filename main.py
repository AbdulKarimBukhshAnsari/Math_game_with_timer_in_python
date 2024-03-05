import random as rd


def problems(start,end,problems):
    right_operand = rd.randint(start,end)
    left_operand = rd.randint(start,end)
    

intro = "This game is design to check your maths ability."
starting ="Hello,The greater would be the number the greater would be the difficulty level."
print(intro.center(60,"*"))
print(starting)

start = int(input("Enter the start of the number: "))
end = int(input("Enter the end of the number: "))
problems = int(input("Enter nymber of problems: "))

problems(start,end,problems)