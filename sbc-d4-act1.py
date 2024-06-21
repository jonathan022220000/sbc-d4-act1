from random import randint 

user_choice = int(input("'0' for hayang, '1' for kulob: "))
p1, C2, C3 = randint(0, 1), randint(0, 1), randint(0, 1)
choices = {0: 1}
if (p1 + C2 + C3) % 2 == 1:
    print("you win")
elif (p1 == C2):
    print("C2 win")
elif (C2 == C3):
    print("C3 win")
else:
    print("draw")
