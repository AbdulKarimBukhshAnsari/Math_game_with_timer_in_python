import random as rd
import time
import sys          #for stdin and stdout purpose.
import threading    # to run 2 program continuosly


def problems(a,b): #to genrate the problem 
    
    operators = ["+","-","*","%"]
    right_operand = str(rd.randint(a,b))
    left_operand = str(rd.randint(a,b))
    operators_choice = rd.choice(operators)
    quesion = left_operand +" "+operators_choice+" "+right_operand
    answer = eval(quesion)       #change the string into python code and perform  relevant operation.
    
    return quesion,answer


def display_timer():
    second = 0
    while True:
        sys.stdout.write(f"\rTime: {second} seconds.    ")
        sys.stdout.flush()
        time.sleep(1)
        second += 1

#Start of the Code
        
intro = "This game is design to check your maths ability."
starting ="Hello,The greater would be the number the greater would be the difficulty level."
print(intro.center(60,"*"))
print(starting)

while True:  #taking start and ending values
    start = int(input("Enter the start of the number: "))
    end = int(input("Enter the end of the number: "))
    problem = int(input("number of problems: "))
    if start>end:
        print("Start value must be less than the end value.")  #there is a possibility that user will write start value greater than the end value by mistake.
    else:
        break
    
# Start the timer
timer_thread = threading.Thread(target=display_timer)
timer_thread.daemon = True
timer_thread.start()


start_time = time.time()  #display the current time.
for i in range(problem):
    question, answer = problems(start, end)
    print(f"\nQuestion #{i+1}: {question}")
    checker = 0   #checker initialize with zero to check how mnay time would you take to guess the correct answer.
    while True:
        print("Enter Answer: ")
        sol = float(input())
        
        if sol == answer:
            print(f"You guessed the correct answer after {checker+1} attempt(s)!")
            break
        else:
            print("Incorrect. Try again!")
            checker += 1
            
Total_time = time.time() - start_time
print(f"Total Time: {int(Total_time)} seconds")   # used int function to get an integer.

if Total_time<problem*5:
    print("You are good at mathematics.") 

else:
    print("Needs an improvement to be good in mathematics")          
        
