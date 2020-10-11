import random
characters = ["Charizard","Greninja","Sceptile","Pikachu","Lycanroc","Dragonite","Glaceon","Alakazam","Scizor","Golurk","Togekiss","Hitmonlee"]
switcher = {
        1: "Charizard",
        2: "Greninja",
        3: "Sceptile",
        4: "Pikachu",
        5: "Lycanroc",
        6: "Dragonite",
        7: "Glaceon",
        8: "Alakazam",
        9: "Scizor",
        10: "Golurk",
        11: "Togekiss",
        12: "Hitmonlee"
    }
print("Hello there !")
print(" ")
print("Are you ready for a Pokemon Battle Frontier ?")
print(" ")
name=input("What's your name ? ")
print(f"Hey {name}")
print(" ")
print("**** [-About the game-] ****")
print(" ")
print("- Choose your Pokemon and I will choose one too")
print("- We have 10 rounds")
print("- The fight is based on Type Advantage")
print("- Who ever wins each round gets 1 point")
print(" ")
print("So let's start")
print("\n\n\n ****************************** Pokemon Battle Frontier *******************************")
flag='y'
print("\n\n\n")
while(flag=='y'):
    turns=10
    i=1
    mpoint=0
    upoint=0
    j=1
    while(turns>0):
        print("Choose a Pokemon :")
        print(" ")
        for character in characters:
            print(i," - ",character)
            i=i+1
        print(" ")
        mychar = random.choice(characters)
        print("Round : ",j)
        print(" ")
        choice=int(input("Select the Pokemon Number : "))
        if(choice<0 or choice>12):
            print("Invalid choice")
            print("Let's do again")
        else:
            guess=switcher.get(choice)
            print("You choose ",guess)
            print(mychar," I choose you !")
            print(" ")
            print(guess," VS ",mychar)
            if(guess==mychar):
                print("We both choose the same.")
                print("No points")

            elif(guess=="Charizard"):                                             #VS Charizard
                if(mychar=="Greninja"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Sceptile"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Pikachu"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Lycanroc"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Dragonite"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Glaceon"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Alakazam"):
                    print("It's neutral. No points")
                elif(mychar=="Scizor"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Golurk"):
                    print("It's neutral. No points")
                elif(mychar=="Togekiss"):
                    print("It's neutral. No points")
                elif(mychar=="Hitmonlee"):
                    upoint=upoint+1
                    print("You won !")
                else:
                    print("----------------------------- Game not working -----------------------------")
            elif(guess=="Greninja"):                                                      #VS Greninja
                if(mychar=="Charizard"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Sceptile"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Pikachu"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Lycanroc"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Dragonite"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Glaceon"):
                    print("It's neutral. No points")
                elif(mychar=="Alakazam"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Scizor"):
                    print("It's neutral. No points")
                elif(mychar=="Golurk"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Togekiss"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Hitmonlee"):
                    mpoint=mpoint+1
                    print("I won !")
                else:
                    print("----------------------------- Game not working -----------------------------")
            elif(guess=="Pikachu"):                                                          #VS Pikachu
                if(mychar=="Charizard"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Sceptile"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Greninja"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Lycanroc"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Dragonite"):
                    print("It's neutral. No points")
                elif(mychar=="Glaceon"):
                    print("It's neutral. No points")
                elif(mychar=="Alakazam"):
                    print("It's neutral. No points")
                elif(mychar=="Scizor"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Golurk"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Togekiss"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Hitmonlee"):
                    print("It's neutral. No points")
                else:
                    print("----------------------------- Game not working -----------------------------")


            elif(guess=="Sceptile"):                                             #VS Sceptile
                if(mychar=="Greninja"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Charizard"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Pikachu"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Lycanroc"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Dragonite"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Glaceon"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Alakazam"):
                    print("It's neutral. No points")
                elif(mychar=="Scizor"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Golurk"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Togekiss"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Hitmonlee"):
                    print("It's neutral. No points")
                else:
                    print("----------------------------- Game not working -----------------------------")
                
            elif(guess=="Lycanroc"):                                             #VS Lycanroc
                if(mychar=="Greninja"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Charizard"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Pikachu"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Sceptile"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Dragonite"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Glaceon"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Alakazam"):
                    print("It's neutral. No points")
                elif(mychar=="Scizor"):
                    print("It's neutral. No points")
                elif(mychar=="Golurk"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Togekiss"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Hitmonlee"):
                    mpoint=mpoint+1
                    print("I won !")
                else:
                    print("----------------------------- Game not working -----------------------------")

            elif(guess=="Dragonite"):                                             #VS Dragonite
                if(mychar=="Greninja"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Charizard"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Pikachu"):
                    print("It's neutral. No points")
                elif(mychar=="Sceptile"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Lycanroc"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Glaceon"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Alakazam"):
                    print("It's neutral. No points")
                elif(mychar=="Scizor"):
                    print("It's neutral. No points")
                elif(mychar=="Golurk"):
                    print("It's neutral. No points")
                elif(mychar=="Togekiss"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Hitmonlee"):
                    upoint=upoint+1
                    print("You won !")
                else:
                    print("----------------------------- Game not working -----------------------------")

            elif(guess=="Glaceon"):                                             #VS Glaceon
                if(mychar=="Greninja"):
                    print("It's neutral. No points")
                elif(mychar=="Charizard"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Pikachu"):
                    print("It's neutral. No points")
                elif(mychar=="Sceptile"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Lycanroc"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Dragonite"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Alakazam"):
                    print("It's neutral. No points")
                elif(mychar=="Scizor"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Golurk"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Togekiss"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Hitmonlee"):
                    mpoint=mpoint+1
                    print("I won !")
                else:
                    print("----------------------------- Game not working -----------------------------")
        
            elif(guess=="Alakazam"):                                             #VS Alakazam
                if(mychar=="Greninja"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Charizard"):
                    print("It's neutral. No points")
                elif(mychar=="Pikachu"):
                    print("It's neutral. No points")
                elif(mychar=="Sceptile"):
                    print("It's neutral. No points")
                elif(mychar=="Lycanroc"):
                    print("It's neutral. No points")
                elif(mychar=="Dragonite"):
                    print("It's neutral. No points")
                elif(mychar=="Glaceon"):
                    print("It's neutral. No points")
                elif(mychar=="Scizor"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Golurk"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Togekiss"):
                    print("It's neutral. No points")
                elif(mychar=="Hitmonlee"):
                    upoint=upoint+1
                    print("You won !")
                else:
                    print("----------------------------- Game not working -----------------------------")

            elif(guess=="Scizor"):                                             #VS Scizor
                if(mychar=="Greninja"):
                    print("It's neutral. No points")
                elif(mychar=="Charizard"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Pikachu"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Sceptile"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Lycanroc"):
                    print("It's neutral. No points")
                elif(mychar=="Dragonite"):
                    print("It's neutral. No points")
                elif(mychar=="Glaceon"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Alakazam"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Golurk"):
                    print("It's neutral. No points")
                elif(mychar=="Togekiss"):
                    print("It's neutral. No points")
                elif(mychar=="Hitmonlee"):
                    print("It's neutral. No points")
                else:
                    print("----------------------------- Game not working -----------------------------")

            elif(guess=="Golurk"):                                                    #VS Golurk
                if(mychar=="Greninja"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Charizard"):
                    print("It's neutral. No points")
                elif(mychar=="Pikachu"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Sceptile"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Lycanroc"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Dragonite"):
                    print("It's neutral. No points")
                elif(mychar=="Glaceon"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Alakazam"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Scizor"):
                    print("It's neutral. No points")
                elif(mychar=="Togekiss"):
                    print("It's neutral. No points")
                elif(mychar=="Hitmonlee"):
                    print("It's neutral. No points")
                else:
                    print("----------------------------- Game not working -----------------------------")

            elif(guess=="Togekiss"):                                                     #VS Togekiss
                if(mychar=="Greninja"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Charizard"):
                    print("It's neutral. No points")
                elif(mychar=="Pikachu"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Sceptile"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Lycanroc"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Dragonite"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Glaceon"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Alakazam"):
                    print("It's neutral. No points")
                elif(mychar=="Scizor"):
                    print("It's neutral. No points")
                elif(mychar=="Golurk"):
                    print("It's neutral. No points")
                elif(mychar=="Hitmonlee"):
                    upoint=upoint+1
                    print("You won !")
                else:
                    print("----------------------------- Game not working -----------------------------")

            elif(guess=="Hitmonlee"):                                                     #VS Hitmonlee
                if(mychar=="Greninja"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Charizard"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Pikachu"):
                    print("It's neutral. No points")
                elif(mychar=="Sceptile"):
                    print("It's neutral. No points")
                elif(mychar=="Lycanroc"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Dragonite"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Glaceon"):
                    upoint=upoint+1
                    print("You won !")
                elif(mychar=="Alakazam"):
                    mpoint=mpoint+1
                    print("I won !")
                elif(mychar=="Scizor"):
                    print("It's neutral. No points")
                elif(mychar=="Golurk"):
                    print("It's neutral. No points")
                elif(mychar=="Togekiss"):
                    mpoint=mpoint+1
                    print("I won !")
                else:
                    print("----------------------------- Game not working -----------------------------")

            else:
                print("----------------------------- Game not working -----------------------------")
            turns=turns-1
            j=j+1
            i=1
    print("\n\n\n")
    print("So it came to an end")
    print("What a game")
    print("\n\n")
    print("So the final score is ")
    print("\n\n")
    print("Your score ",upoint)
    print("My score ",mpoint)
    if(upoint>mpoint):
        print(":( You WON !!!")
        print("Well.. Next time, I will win")
        print("Anyway, congrats buddy")
    elif(upoint<mpoint):
        print("He he he... I won")
    else:
        print("Its a tie !")
    print("How about we play again ?")
    print("y - Yes")
    print("n - No")
    flag=input("Your answer : ")
    flag.lower()
print("Thanks for the game")
print("Goodbye :)")
