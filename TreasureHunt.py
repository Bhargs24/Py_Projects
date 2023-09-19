# Function to get the user's choice of direction
def choose_direction():
    while True:
        choice = input("Enter your choice (L for left, R for right, S for straight, N for no, Y for yes): ").lower()
        if choice in ["l", "r", "s", "n", "y"]:
            return choice
        else:
            print("Invalid choice. Please enter L for left, R for right, S for straight, N for no, or Y for yes.")

# Initialize game variables
points = 0
treasure_found = False

# Start the loop for treasure hunt
while True:
    # Start
    print("\n" + "-" * 30)
    print('''
                  
____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
              
           
          ''')

    print("\nWelcome to the Treasure Hunt Game!")
    print("You are in the middle of a street.")
    print("Your goal is to find the treasure on the island.")
    print("You have", points, "points.")

    # Ask if the user wants to start a new game
    start_game = input("Start a new game? (Y/N): ").lower()
    if start_game != "y":
        print("Goodbye!")
        break

    # Start the game
    current_location = "street"

    while current_location != "island":
        if current_location == "street":
            print("\n" + "-" * 30)
            print("You are on the street. You can go left (L), right (R), or straight (S).")
            choice = choose_direction()
            if choice == "l":
                print("You took the left road and reached a dead end. Try another direction.")
            elif choice == "r":
                print("You turned right and found a bridge. Do you want to cross it? (Y/N)")
                cross_bridge = input().lower()
                if cross_bridge == "y":
                    print("The bridge collapsed, and you fell into the river. Game over.")
                    break
                else:
                    print("You decided not to cross the bridge.")
            elif choice == "s":
                print("You chose to go straight and entered a forest. Watch out for wild animals!")
                current_location = "forest"
            elif choice == "n":
                print("You decided not to start a new game. Goodbye!")
                break
        elif current_location == "forest":
            print("\n" + "-" * 30)
            print('''
      .. ........... .............  ........... . ..... ........ .......
 ......  ....................%.... .... ..... .........%............
 .@@@ ........ @@.... @@@@  . ............................  *  .....
 ....@@ ..... @ .... @ .............   ....... .....; .... *** .....
 .....\@\....@ .... @ ............................. #  .. *****  ...
  @@@.. @@@@@  @@@@@@___.. ....... ...%..... ...  {###}  *******
 ....@-@..@ ..@......@@@\...... %...... ....... <## ####>********
   @@@@\...@ @ ........\@@@@ ..... ...... ....... {###}***********
 ....%..@  @@ /@@@@@ . ....... ...............<###########> *******
 ...... .@-@@@@ ...V......     .... %.......... {#######}******* ***
 ...... .  @@ .. ..v.. .. . { } ............<###############>*******
 ......... @@ .... ........ {^^,     .......   {## ######}***** ****
 ..%..... @@ .. .%.... . .. (   `-;   ... <###################> ****
 . .... . @@ . .... .. _  .. `;;~~ ......... {#############}********
 .... ... @@ ... ..   /(______); .. ....<################  #####>***
 . .... ..@@@ ...... (         (  .........{##################}*****
 ......... @@@  ....  |:------( )  .. <##########################>**
  @@@@ ....@@@  ... _// ...... \\ ...... {###   ##############}*****
 @@@@@@@  @@@@@ .. / /@@@@@@@@@ vv  <##############################>
 @@@@@@@ @@@@@@@ @@@@@@@@@@@@@@@@@@@ ..... @@@@@@  @@@@@@@  @@@@
 @@@@@@###@@@@@### @@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@###@##@@ @@@@@@@@@@@@@@@@@@@@@ @@@@@   @@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@### @@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@
 -@@@@@@@@@#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



''')
            print("You are in the forest. You can go left (L), right (R), or straight (S).")
            choice = choose_direction()
            if choice == "l":
                print("You encountered a bear! Game over.")
                break
            elif choice == "r":
                print("You found a river, but there's no way to cross it. Go back or try another direction.")
            elif choice == "s":
                print("You reached the edge of the forest and found a boat.")
                print("You need to take the boat to reach the island. Do you want to take the boat? (Y/N)")
                take_boat = input().lower()
                if take_boat == "y":
                    print("\n" + "-" * 30)
                    print('''

     ~;
                  ,/|\,
                ,/' |\ \,
              ,/'   | |  \
            ,/'     | |   |
          ,/'       |/    |
        ,/__________|-----' ,
       ___.....-----''-----/
 jgs   \                  /
   ~~-~^~^~`~^~`~^^~^~-^~^~^~-~^~^
     ~-^~^-`~^~-^~^`^~^-^~^`^~^-~^
      
''')
                    print("You took the boat and found the hidden treasure!")
                    points += 5  # Award points for finding the treasure
                    treasure_found = True

                    # Determine the ending based on the number of points
                    ending = ""
                    if points < 3:
                        ending = "You found a small chest with some coins."
                    elif points < 5:
                        ending = "You found a valuable gemstone!"
                    else:
                        ending = "You discovered a chest filled with ancient artifacts!"
                    
                    print(f"Congratulations! {ending}")
                    current_location = "island"
                else:
                    print("You decided not to take the boat. Game over.")
                    break
            elif choice == "n":
                print("You decided not to start a new game. Goodbye!")
                break

    if current_location != "island":
        print("\n" + "-" * 30)
        print('''
                  

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

           
          ''')

    if not treasure_found:
        print("You didn't find the treasure this time. Better luck next time!")
        points -= 1  # Deduct points for not finding the treasure

    print("Total points:", points)
    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again != "y":
        print("Goodbye!")
        break
