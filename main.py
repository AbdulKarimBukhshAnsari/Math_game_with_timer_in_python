import random as rd
import math

def problems(a,b):
    
    operators = ["+","-","*","/","%"]
    right_operand = str(rd.randint(a,b))
    left_operand = str(rd.randint(a,b))
    operators_choice = rd.choice(operators)
    quesion = left_operand +" "+operators_choice+" "+right_operand
    answer = eval(quesion)
    
    return quesion,answer
    

intro = "This game is design to check your maths ability."
starting ="Hello,The greater would be the number the greater would be the difficulty level."
print(intro.center(60,"*"))
print(starting)


start = int(input("Enter the start of the number: "))
end = int(input("Enter the end of the number: "))
problem = int(input("number of problems: "))
checker = 0

for i in range(problem):
    question , answer =problems(start,end)
    while True:
        sol = float(input(f"Question #{i+1} : {question} = "))
        if sol == answer:
            print(f"You guessed the correct answer after {checker+1} turn! ")
            break
        else:
            print("You guessed wrong Try Again!!")
            checker+=1
            
        
