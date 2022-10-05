
import random 
points: int
player: str 
ROFL = "\U0001F923"
GOOD_CHOICE = 2
BAD_CHOICE = 1

def greet() -> None:
    global player
    player = input("What would you like your username to be? " "\n")
    print(f"Hello {player}. In this game, you will be placed into scenarios of your choice where you can either hang out with your friends, or hang out with your significant other.")
    print("Of course you are not limited to one, as you can chose one scenario after the other.")
    print("Every question asked in either scenario will be 'Yes or No' questions. Please answer with a 'Yes' or 'No' spelled and capitalized just as shown" "\n")

def friends() -> None:
    global points 
    print(f"\n" "*You will now be put in a group of your friends, and will earn points based on how good of a friend you are {ROFL}.*" "\n")
    pizza_place: str = input(f"Yo {player}, I really want pizza right now. Do you want to get Dominoes?" "\n")
    if pizza_place == "Yes":
        points += GOOD_CHOICE
    else:
        points += BAD_CHOICE
    miles: int = random.randint(1, 50)
    driving: str = input(f"Ight bet, I only have {miles} miles in my gas tank, could you drive over there?" "\n")
    if driving == "Yes":
        points += GOOD_CHOICE
        print(f"Thank you.")
    else:
        points += BAD_CHOICE
        print(f"Wowwww ok, you are defintely reimbursing my gas then." "\n")
    cheese_pizza: str = input("Remember I am a vegetarian, so do you want to split a large cheese pizza to save money?" "\n")
    if cheese_pizza == "Yes":
        points += GOOD_CHOICE
    else:
        points += BAD_CHOICE
    print("\n" "*Both of you get in the car*" "\n")
    artist = input(f"{player}, you want to listen to Playboi Carti?" "\n")
    if artist == "Yes":
        points += GOOD_CHOICE
        print("Say that. I'm throwing on 'New N3on' right now. " "\n")
    else:
        points += BAD_CHOICE
        print("Really? Ok then." "\n")


def lover(points_in_lover: int) -> int:
    print("\n" "*answer perfectly or else this segment might abruptly end*")
    if points_in_lover > 0:
        friends: str = input(f"Hey {player}, did you hang out with your friends earlier?" "\n")
        if friends == "Yes":
            print("Looks like you care about them more than me" "\n")
            points_in_lover += BAD_CHOICE
        else:
            print("Oh ok, I was just wondering." "\n")
            points_in_lover += GOOD_CHOICE
    other_people: int = random.randint(2, 10)
    cheating: str = input(f"So, my friends were telling me you were talking to {other_people} love interests. Is this true?" "\n")
    if cheating == "Yes":
        print("Get out of my house.")
        points_in_lover += BAD_CHOICE
        return points_in_lover
    else:
        print(f"Sorry {player}, I just wanted to make sure." "\n")
        points_in_lover += GOOD_CHOICE
    date: str = input("Do you have a date planned for us tonight? I'm so excited." "\n")
    if date == "Yes":
        print("Ahh, you are the best.")
        points_in_lover += GOOD_CHOICE
    else:
        print(f"I knew you weren't serious about us {ROFL}{ROFL}{ROFL}{ROFL}{ROFL}{ROFL}." "\n")
        points_in_lover += BAD_CHOICE
        return points_in_lover
    parents = str = input("Before we go, I know we have been talking about meeting each other's parents, and my mom is downstairs right now. Are you ready for that?" "\n")
    if parents == "Yes":
        print("Yayyy, I will go get her." "\n")
        points_in_lover += GOOD_CHOICE
    else:
        print("I don't think this is going to work out")
        points_in_lover += BAD_CHOICE
        return points_in_lover
    return points_in_lover


    
    


        

def main() -> None:
    continue_playing: bool = True
    global points
    global player
    points = 0
    greet()
    print(f"Well {player}, now that you know about this game, what path would you like to take?" "\n")
    choice: int = input("Enter 1 if you would like to go hang out with your friends. " "\n" "Enter 2 if you would like to hang out with your significant other. " "\n" "Enter 3 if you would like to quit the game. " "\n")
    if int(choice) == 1:
        friends()
    if int(choice) == 2:
        points += lover(points)
    if int(choice) == 3:            
        quit()
    play_again: bool = True
    while play_again:
        print(f"Points: {points}")
        choice: int = input("You have just finished one of the paths, but you may keep playing" "\n" "Enter 1 if you would like to go hang out with your friends. " "\n" "Enter 2 if you would like to hang out with your significant other. " "\n" "Enter 3 if you would like to quit the game. " "\n")
        if int(choice) == 1:
            friends()
        if int(choice) == 2:
            points += lover(points)
        if int(choice) == 3:            
            quit()

    


if __name__ == "__main__":
    main()