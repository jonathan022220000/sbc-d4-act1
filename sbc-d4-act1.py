from random import randint      #This line imports the randint function from the random module.

p1= int(input("'0' for hayang, '1' for kulob: "))    #This line prompts the user to input either '0' for "hayang" or '1' for "kulob"

       #This line converts the user input stored in p1 from a string to an integer
p1, C2, C3 = randint(0, 1), randint(0, 1), randint(0, 1)    #This line generates three random integers (either 0 or 1) using the randint function and assigns them to the variables p1, C2, and C3 respectively.
choice = {0: "hayang", 1: "kulob"}      #This line creates a dictionary where the keys are 0 and 1, representing the choices "hayang" and "kulob" respectively.
print(f"p1: {choice[p1]}")      #This line prints the user choice based on the integer input p1 by retrieving the corresponding value ("hayang" or "kulob") from the choice dictionary.
print(f"C2: {choice[C2]}")      #This line prints the computer's choice (C2) by retrieving the corresponding value ("hayang" or "kulob") from the choice dictionary 
print(f"C3: {choice[C3]}")      #This line prints the computer's choice (C3) by retrieving the corresponding value ("hayang" or "kulob") from the choice dictionary

if p1 != C2 & p1 != C3:       #If the sum of the user's choice, C2, and C3 is odd, the user wins.
    print("you win")        #the user wins.
elif C2 != p1 & C2 != C3  :     #If the user's choice is different from C2, C2 wins.     
    print("C2 win")
elif  C3 != p1 & C3 != C2 :     #If the user's choice is different from C3, C3 wins.
    print("C3 win")
else:       
    print("It's a tie play again!")     ##If none of the above conditions are met, play again
