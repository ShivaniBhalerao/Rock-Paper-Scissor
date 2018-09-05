import random

list1=['rock','paper','scissor']
mydict={"rock":1,"paper":3,"scissor":2}
play='y'
while (play=='y' or play=='Y'):    
    chance=3
    compscore=0
    userscore=0
    while(chance>0):
        myvar=random.choice(list1)
        comp=mydict[myvar]
       # print(comp)
        user1=input("Enter rock,paper or scissor?")
        user1=user1.lower()
        user=mydict[user1]
        diff=user-comp
        if diff in [-2,1] :
            compscore=compscore+1
            chance=chance-1
            print("comp=",compscore)
        elif diff in [-1,2]:
            userscore=userscore+1
            chance=chance-1
            print("User=" ,userscore)
        elif diff==0:
            chance=chance-1
            print("same")
    if(compscore>userscore):
        print("Sorry you lost")        
    elif(compscore<userscore):
        print("You Won")
    else:
        print("Tie")
    play=input("Want to play again? Y/N")
