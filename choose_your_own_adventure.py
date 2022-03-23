name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end. Would you go left or right (left/right)? ").lower()

if answer == "left":
    answer = input("You've come to a river. You can walk around it or swim accross. (walk/swim): ").lower()

    if answer == "swim":
        print("You swam accross and was eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You've come to a bridge, it looks wobbly. Do you want to cross it or head back (cross/back)? ").lower()

    if answer == "back":
        print("You go back and lose")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()

        if answer == "yes":
            print("You talk to the stanger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stanger and they are offended and you lose.")
        else:
            print("Not a valid option. You lose.")

    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for trying", name)