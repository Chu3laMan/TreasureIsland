print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''');
print("Welcome to Treasure Island");
print("Your mission is to find the treasure");
print("You're at the cross road. Where do you want tp go? Type ""left"" or ""right");
answer = input("");
if(answer=="left"):
    swimOrWait = input("You've come to a lake. There is an island in the middle of the lake. Type ""wait"" to wait for a boat. Type ""swim"" to swim accross.").lower();
    if(swimOrWait == "wait"):
        colorChosed = print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you prefer? ");
        if(colorChosed == "yellow"):
            print("You found the treasure! You win!");
        elif(colorChosed == "blue"):
            print("You entered a room of beasts! Game Over!");
        elif(colorChosed == "red"):
            print("You chose a door that does not exist. Game over!");

    else:
        print("You get attacked by an angry trout. Game Over!");

elif(answer=="right"):
    print("Game Over!");
