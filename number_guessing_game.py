from ast import match_case
import random
print("Description: You need to provide range of number and computer will choose a number in that range. Based on hardness you have to find out what that number was in fixed attempt.")
lower = int(input("Enter the lower limit number. "))
upper = int(input("Enter the upper limit number. "))
diff = int(input("Enter the corresponding number of difficulty in which you want to play.\n1.Very Easy(Noob)\n2.Easy\n3.Hard\n4.Very Hard(Legend)\n5.God Mode\n"))
rang= upper - lower
if (rang>10):
    match diff:
        case 1:
            x = rang/2
            attempt = int(rang/2)
        case 2:
            attempt = int(rang/3)
        case 3:
            attempt = int(rang/5)
        case 4:
            attempt = int(rang/7)
        case 5:
            attempt = 1
else:
    match diff:
        case 1:
            attempt = 5
        case 2:
            attempt = 4
        case 3:
            attempt = 3
        case 4:
            attempt = 2
        case 5:
            attempt = 1
choosed = random.randint(lower,upper)
for i in range(attempt):
    guess = int(input("Guess the number the computer has choosed. "))
    if (choosed>guess):
        print("Choose higher. ")
    elif(choosed<guess):
        print("Guess lower. ")
    else:
        print("Yay!!, You won. ")
        break
    if ( i==attempt - 1 and guess!=attempt):
        print("You lost. ")

