import random
i=0
j=0
for n in range(0,10000):
    a=["rock","paper","scissor"]
    c=random.choice(a)
    p=None


    while p not in a:
        p=input("rock,paper,scissor:").lower()
    if p==c:
        print("computer:",c)
        print("user:",p)
        print("tie")
    elif p == "rock":
        if c == "scissor":
            print("computer:",c)
            print("user:",p)
            print("you win")
            i=i+1
        if c== "paper":
            print("computer:",c)
            print("user:",p)
            print("you lose")
            j=j+1
    elif p == "scissor":
        if c == "rock":
            print("computer:",c)
            print("user:",p)
            print("you lose")
            j=j+1
        if c == "paper":
            print("computer:",c)
            print("user:",p)
            print("you win")
            i=i+1
    elif p == "paper":
        if c == "scissor":
            print("computer:",c)
            print("user:",p)
            print("you lose")
            j=j+1
        if c == "rock":
            print("computer:",c)
            print("user:",p)
            print("you win")
            i=i+1
    again=input("\nplay again (yes/no):").lower()
    if again!="yes":
        break
    
print("\nyour score",i)
print("computer score",j)
if (i>j):
    print("you win the game")
elif(i==j):
    print("tieeeeeeeeeee")
else:
    print("you lose")

