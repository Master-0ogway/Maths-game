import time 
import random
from decimal import Decimal
import math
score = 0
score1 = 0
lives = 5
level_cleared = False
level_cleared2 = False
level_cleared3 = False
level_cleared4 = False
Win = False
Dead = False
lvl = 1
Operations = ["*" , "+" , "-" , "/"]
Player_Name = input("WELCOME to my maths game please enter your name: ")
while True:
    Start_Game = input("Press enter to start")
    try:
        Start_Game = str(Start_Game)
    except:
        pass
    if Start_Game == "":
        break
    print("Thats not enter!")
time.sleep(1)
print("""Here are the rules:
    DO maths thats all just maths please\n""")
Num1 = random.randint(0, 2356)
Num2 = random.randint(0, 3457)
ops = random.choice(Operations)
    
  
while True:
    answer = round(eval(str(Num1) + ops + str(Num2)),2)
    print (answer) #for debugging
    question = (str(Num1)+ ' ' + ops + ' ' + str(Num2))
    User_Answer = input("Question"+ str(lvl)+': '+str(question)+ ': ')
    try:
        User_Answer = float(User_Answer)
        if lives <= 0:
            Dead = True
            score = score - score1
            break
        if score == 17:
            level_cleared = True
            score = score - score1
            break
    except:
        pass
    if User_Answer == (round(answer, 2)):
        print("Correct!")
        lvl = lvl + 1
        score = score + 1
        Num1 = random.randint(0, 2356)
        Num2 = random.randint(0, 3457)
        ops = random.choice(Operations)
    else:
        print("Wrong answer!")
        lvl = lvl + 1
        lives = lives - 1
        score1 = score1 + 1
        Num1 = random.randint(0, 2356)
        Num2 = random.randint(0, 3457)
        ops = random.choice(Operations)
    
if level_cleared == True:
    Num1 = random.randint(0, 2356)
    Num2 = random.randint(0, 3457)
    while True:
        answer = math.sqrt(Num1)
        answer2 = math.sqrt(Num2)
        question = (str(u"\u221a") + str(Num1) + '+' + str(u"\u221a") + str(Num2))
        final_answer = round((answer + answer2),2)
        print (final_answer) ##for debugging
        User_Answer2 = input("Question"+ str(lvl)+': '+str(question)+ ': ')
        try:
            User_Answer2 = float(User_Answer2)
            if lives <= 0:
                Dead = True
                score = score - score1
                break
            if score == 27:
                level_cleared2 = True
                score = score - score1
                break
        except:
            pass
        if User_Answer2 == final_answer:
            print("Correct!")
            lvl = lvl + 1
            score = score + 1
            score = score - score1
            Num1 = random.randint(0, 2356)
            Num2 = random.randint(0, 3457)
        else:
            print("Wrong answer!")
            lvl = lvl + 1
            lives = lives - 1
            score1 = score1 + 1
            score = score - score1
            Num1 = random.randint(0, 2356)
            Num2 = random.randint(0, 3457)

if level_cleared2 == True:
    Num1 = random.randint(0, 2356)
    Num2 = random.randint(0, 3457)
    Num3 = random.randint(0, 60)
    Num4 = random.randint(0, 76)
    while True:
        final_answer = round((Num3 / Num4*Num2 + Num1),2)
        print (final_answer) #for debugging
        question = (str(Num3) + '÷' + str(Num4) + '(' + str(Num2) + '+' + str(Num1) + ')')
        User_Answer3 = input("Question"+ str(lvl)+': '+str(question)+ ': ')
        try:
            User_Answer3 = float(User_Answer3)
            if lives <= 0:
                Dead = True
                score = score - score1
                break
            if score == 37:
                level_cleared3 = True
                score = score - score1
                break
        except:
            pass
        if User_Answer3 == final_answer:
            print("Correct!")
            lvl = lvl + 1
            score = score + 1
            Num1 = random.randint(0, 2356)
            Num2 = random.randint(0, 3457)
            Num3 = random.randint(0, 60)
            Num4 = random.randint(0, 76)
        else:
            print("Wrong answer!")
            lvl = lvl + 1
            lives = lives - 1
            score1 = score1 + 1
            Num1 = random.randint(0, 2356)
            Num2 = random.randint(0, 3457)
            Num3 = random.randint(0, 60)
            Num4 = random.randint(0, 76)

if level_cleared3 == True:
    a = random.randint(0, 2356)
    b = random.randint(0, 3457)
    while True:
        final_answer = round(math.sqrt(a * a + b * b),2)
        question = (str(a) + str(u'\u00b2') + '+' + str(b) + str(u'\u00b2'))
        print(final_answer) #for debugging
        User_Answer4 = input("Question"+ str(lvl)+': '+str(question)+ ': ')
        try:
            User_Answer4 = float(User_Answer4)
            if lives <= 0:
                Dead = True
                score = score - score1
                break
            if score == 50:
                level_cleared4 = True
                score = score - score1
                break
            if level_cleared and level_cleared2 and level_cleared3 and level_cleared4 == True:
                Win = True
                break
        except:
            pass
        if User_Answer4 == final_answer:
            print("Correct!")
            lvl = lvl + 1
            score = score + 1
            score = score - score1
            a = random.randint(0, 2356)
            b = random.randint(0, 3457)
        else:
            print("Wrong answer!")
            lvl = lvl + 1
            lives = lives - 1
            score1 = score1 + 1
            a = random.randint(0, 2356)
            b = random.randint(0, 3457)









if Dead == True:
    print("welldone you got "+ str(score) + "\50")
if Win == True:
    print("welldone you got "+ str(score) + "\50")
    


