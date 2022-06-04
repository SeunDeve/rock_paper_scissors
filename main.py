import random


def rock_paper_scisssors(choice=input("Enter rock paper or scissors: ")):
    cpu = random.choice(['r', 'p', 's'])
    print(cpu)
    choices = ['r', 'p', 's']
    if choice.lower() not in choices:
        return 'enter either rock, paper and scissors'
    elif choice.lower() == "r" and cpu == "s":
        return 'player wins'
    elif choice.lower() == "p" and cpu == "r":
        return 'player wins'
    elif choice.lower() == "s" and cpu == "p":
        return 'player wins'
    elif choice.lower() == cpu:
        print("It is a tie")
        return rock_paper_scisssors(choice=input("Enter rock paper or scissors: "))
    else:
        return "cpu wins"


print(rock_paper_scisssors())