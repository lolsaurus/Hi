import random
userin = int(input("Please select an action \n (1 Rock \t (2 Paper \t (3 Scissors \n (Input the number)\n"))
botnum=random.randint(1,3)

if userin > 3 or userin ==0:
     print ("Invalid Input, Please restart the game")
     exit()
aihonesty = input("IS The AI HONEST?\n Y/N\n Please enter your choice\n")

if aihonesty == "Y" or aihonesty == "y":
    
   if userin > 3 or userin ==0:
    print ("Invalid Input, Please restart the game")
    exit()

   #move demo
    
   if userin == 1:
    print ("Your move was rock\t")
   elif userin == 2:
    print ("Your move was paper\t")
   elif userin == 3:
    print ("Your move was scissors \t")
   
   if botnum == 1:
    print ("AI's move was rock")
   elif botnum == 2:
    print ("AI's move was paper")
   elif botnum ==3:
    print ("AI's move was scissors")

   #results

   if botnum == userin:
    print ("It's a tie!")
   elif botnum > userin and botnum-userin ==1:
    print ("AI won!")
   elif botnum > userin and botnum-userin > 1:
    print ("You won!")
   elif userin > botnum and userin-botnum == 1:
    print ("You won!")
   elif userin > botnum and userin-botnum > 1:
    print ("AI won!")

   print ("Return")


elif aihonesty == "N" or aihonesty == "n":

    #cheat

    if userin <= 2:
      botnum = userin+1
    elif userin == 3:
        botnum = userin-2

    #move demo    

    if userin == 1:
     print ("Your move was rock\t")
    elif userin == 2:
     print ("Your move was paper\t")
    elif userin == 3:
     print ("Your move was scissors \t")
    if botnum == 1:
     print ("AI's move was rock")
    elif botnum == 2:
     print ("AI's move was paper")
    elif botnum ==3:
     print ("AI's move was scissors")

    #results
     
    if botnum == userin:
     print ("It's a tie!")
    elif botnum > userin and botnum-userin ==1:
     print ("AI won!")
    elif botnum > userin and botnum-userin > 1:
     print ("You won!")
    elif userin > botnum and userin-botnum == 1:
     print ("You won!")
    elif userin > botnum and userin-botnum > 1:
     print ("AI won!")
  
    print ("Return 2")
