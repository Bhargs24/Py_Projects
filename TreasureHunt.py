# Function to get the user's choice

def choose_direction():
    while True:
        choice = input("Enter your choice: ").lower()
        if choice in ["l", "s", "r", "n", "y"]:
            return choice
        else:
            print("Invalid choice. Please enter L for left, R for right, S for straight, N for no, or Y for yes.")



treasure_found = False


# Start the loop for treasure hunt

while True:

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
    
    print("\n\n\n")
    print("Welcome to the Treasure Hunt Game!")
    print("You are at the starting point in the city.")



    # Ask if the user wants to start a new game

    start_game = input("Start a new game? (Y/N): ").lower()
    if start_game != "y":
        print("Goodbye!")
        break

    

    # Start the game
    current_location = "starting_point"

    while current_location != "island":
        
        
        if current_location == "starting_point":
            print("\n" + "-" * 30)
            print("You are at the starting point in the city. You can enter the city (S).")
            choice = choose_direction()
            
            
            if choice == "s":
                current_location = "intersection_1"
            
            
            elif choice == "n":
                print("You decided not to start a new game. Goodbye!")
                break
        
        
        elif current_location == "intersection_1":
            print("\n" + "-" * 30)
            print("You are at Intersection 1.")
            print("(L) - Take the left road.")
            print("(S) - Continue to Intersection 2.")
            print("(R) - Turn right into a dark alleyway.")


            choice = choose_direction()


            if choice == "l":
                print("You take the left road and suddenly hear gunshots! A gang attacks you. Game over.")
                break
            
           
            elif choice == "s":
                current_location = "intersection_2"
            
            
            elif choice == "r":
                print("You turn right and encounter a dark alleyway. It seems ominous.")
                print("(Y) - You cautiously explore the alley but find nothing valuable.")
                print("(N) - You decide it's too risky and return to the previous intersection.")
                explore_alley = choose_direction()
                
                
                if explore_alley == "y":
                    print("You explore the alley but find nothing valuable. Continue to Intersection 4.")
                    current_location = "intersection_4"
                
                
                elif explore_alley == "n":
                    print("You decide it's too risky and return to the previous intersection.")
                    current_location = "intersection_1"
        
        
        
        elif current_location == "intersection_2":
            print("\n" + "-" * 30)
            print("You are at Intersection 2.")
            print("(L) - Take the left road (dead-end).")
            print("(S) - Continue to Intersection 3.")
            print("(R) - Turn right and find a hidden message on a wall that says, 'Treasure this way.'")
            choice = choose_direction()
            
            
            if choice == "l":
                print("You head left, but the road leads to a dead-end. Game over.")
                break
            
            
            elif choice == "s":
                current_location = "intersection_3"
            
            
            elif choice == "r":
                print("You turn right and find a hidden message on a wall that says, 'Treasure this way.'")
                current_location = "intersection_5"
       
       
       
        elif current_location == "intersection_3":
            print("\n" + "-" * 30)
            print("You are at Intersection 3.")
            print("(L) - Dead-end. Game over.")
            print("(S) - Continue to Intersection 4.")
            print("(R) - Dead-end. Game over.")
            choice = choose_direction()
            
            
            if choice == "l":
                print("Dead-end. Game over.")
                break
           
           
            elif choice == "s":
                current_location = "intersection_4"
            
            
            elif choice == "r":
                print("Dead-end. Game over.")
                break
        
        
        
        elif current_location == "intersection_4":
            print("\n" + "-" * 30)
            print("You are at Intersection 4.")
            print("(L) - Follow a dimly lit path.")
            print("(R) - Continue down the road.")
            print("(S) - Backtrack and head to Intersection 5.")
            choice = choose_direction()
            
            
            if choice == "l":
                print("You follow a dimly lit path but trip and fall into a deep manhole. Game over.")
                break
            
            
            elif choice == "r":
                print("You continue down the road but accidentally step on a loose board, falling into a sewer. Game over.")
                break
            
            
            elif choice == "s":
                current_location = "intersection_5"
        
        
        
        elif current_location == "intersection_5":
            print("\n" + "-" * 30)
            print("You are at Intersection 5.")
            print("(L) - Take a shortcut through a narrow alley.")
            print("(R) - Turn right and find a hidden forest path.")
            choice = choose_direction()
            
            
            if choice == "l":
                print("You take a shortcut through a narrow alley.")
                print("(Y) - You get mugged and lose all your belongings. Game over.")
                print("(N) - You decide to avoid the alley and continue down the road.")
                mugger = choose_direction()
                
                
                if mugger == "y":
                    print("You get mugged and lose all your belongings. Game over.")
                    break
                
                
                elif mugger == "n":
                    print("You decide to avoid the alley and continue down the road.")
                    current_location = "intersection_5"
            
            
            
            elif choice == "r":
                print("You turn right and find a hidden forest path.")
                current_location = "forest"
        
        
        
        
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



            print("You are in the forest.")
            print("(L) - Come across a fork in the road with a warning sign about snakes.")
            print("(S) - Encounter a peaceful clearing with a serene pond.")
            print("(R) - Spot an old abandoned shack.")
            choice = choose_direction()
            
            
            if choice == "l":
                print("You come across a fork in the road with a warning sign about snakes.")
                print("(Y) - You proceed and encounter a venomous snake! Game over.")
                print("(N) - You choose the right path and continue forward.")
                snake_warning = choose_direction()
                
                
                if snake_warning == "y":
                    print("You proceed and encounter a venomous snake! Game over.")
                    break
               
               
                elif snake_warning == "n":
                    print("You choose the right path and continue forward.")
            
            
            
            elif choice == "s":
                print("You encounter a serene pond.")
                print("(L) - You sit by the pond for a while and enjoy the serenity.")
                print("(R) - You decide to take a refreshing dip in the pond.")
                pond_choice = choose_direction()
                
                
                if pond_choice == "l":
                    print("You sit by the pond for a while and enjoy the serenity. Continue on the main path.")
                    current_location = "forest"
                
                
                elif pond_choice == "r":
                    print("You decide to take a refreshing dip in the pond. Feeling rejuvenated, you continue along the path.")
                    current_location = "forest"
            
            
            
            elif choice == "r":
                print("You spot an old abandoned shack.")
                print("(L) - You cautiously approach the shack and peek inside, finding nothing of interest.")
                print("(R) - You explore the shack but find it empty. Disappointed, you continue along the path.")
                shack_choice = choose_direction()
                
                
                if shack_choice == "l":
                    print("You cautiously approach the shack and peek inside, finding nothing of interest. Continue on the main path.")
                    current_location = "forest"
               
               
                elif shack_choice == "r":
                    print("You explore the shack but find it empty. Disappointed, you continue along the path.")
                    current_location = "forest"
        
        
        
        
        elif current_location == "island":
            print("\n" + "-" * 30)
            print("You have reached the end of the forest.")
            print("(R) - You see a bridge that might lead you to an island near the shore.")
            print("(L) - There is a trail that leads downhill.")
            choice = choose_direction()
            
            
            if choice == "r":
                print("You see a bridge that might lead you to an island near the shore.")
                print("(Y) - The bridge collapses, and you fall into the river and die.")
                print("(N) - You decide not to take the bridge and continue.")
                bridge_choice = choose_direction()
               
               
                if bridge_choice == "y":
                    print("The bridge collapses, and you fall into the river and die.")
                    break
               
               
                elif bridge_choice == "n":
                    print("You decide not to take the bridge and continue.")
                    current_location = "lake"
           
           
           
            elif choice == "l":
                print("There is a trail that leads downhill.")
                print("(Y) - The trail leads you to a river bank with a boat that takes you to the lake and island.")
                print("(N) - You choose not to take the trail and return to the forest.")
                trail_choice = choose_direction()
              
              
                if trail_choice == "y":
                    print("The trail leads you to a river bank with a boat that takes you to the lake and island.")
                    current_location = "boat"
               
               
                elif trail_choice == "n":
                    print("You choose not to take the trail and return to the forest.")
                    current_location = "forest"
        
        
        
        elif current_location == "boat":
            print("\n" + "-" * 30)
            print("You have reached the river bank with a boat that takes you to the lake and island.")
            print("(Y) - You decide to take the boat. It's time to set sail for the island.")
            print("(N) - You choose not to start a new game. Goodbye!")
            boat_choice = choose_direction()
           
           
            if boat_choice == "y":
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

                print("You decide to take the boat. It's time to set sail for the island.")
                print("\n\n\n" + "-" * 30)

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





                print("\n\n\nAfter 2 days of sailing, you reach a tiny island and find a treasure hunter resting under a palm tree.")
                print("\n\n\n\Congratulations, you've completed your adventure and found the treasure! The game ends here.")
                treasure_found = True
                break
            
            
            elif boat_choice == "n":
                print("You choose not to start a new game. Goodbye!")
                break

    if not treasure_found:
        print("You didn't find the treasure this time. Better luck next time!")

    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again != "y":
        print("Goodbye!")
        break
