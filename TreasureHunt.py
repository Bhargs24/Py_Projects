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

    while True:
        # Define the game logic based on the current location
        if current_location == "starting_point":
            print("Choose your direction:")
            print("(S) - Enter the city.")
            direction = choose_direction()
            
            
            if direction == "s":
                current_location = "intersection_1"
            else:
                print("Invalid choice. Please try again.")

        
        
        elif current_location == "intersection_1":
            print("You are at Intersection 1.")
            print("Choose your direction:")
            print("(L) - Take the left road.")
            print("(R) - Continue to Intersection 2.")
            print("(S) - Turn right into a dark alleyway.")
            direction = choose_direction()
            
            
            if direction == "l":
                print("You take the left road and suddenly hear gunshots! A gang attacks you. Game over.")
                current_location = "intersection_1"
            
            
            elif direction == "r":
                current_location = "intersection_2"
            
            
            elif direction == "s":
                print("You encounter a dark alleyway. It seems ominous.want to continue? (Y)(N) ")
                explore_alley = choose_direction()
                
                
                if explore_alley == "y":
                    print("You cautiously explore the alley but find nothing valuable.")
                    current_location = "intersection_1"
                
                
                elif explore_alley == "n":
                    print("You decide it's too risky and return to the previous intersection.")
                    current_location = "intersection_1"
                
                
                else:
                    print("Invalid choice. Please try again.")
            
            
            else:
                print("Invalid choice. Please try again.")

        
        
        elif current_location == "intersection_2":
            print("You are at Intersection 2.")
            print("Choose your direction:")
            print("(S) - Go straight")
            print("(L) - Take Left.")
            print("(R) - Turn right")
            direction = choose_direction()
            
            
            if direction == "l":
                print("You proceeded straight, but the road leads to a dead-end. go back.")
                current_location = "intersection_2"
            
            
            elif direction == "l":
                print("Towards Intersection 3.")
                current_location = "intersection_3"
            
            
            elif direction == "r":
                print("You find a hidden message on a wall that says, 'Treasure this way.'")
                current_location = "intersection_5"
            
            
            else:
                print("Invalid choice. Please try again.")

        elif current_location == "intersection_3":
            print("You are at Intersection 3.")
            print("Choose your direction:")
            print("(L)- Take Left ")
            print("(S)- Go straight ")
            print("(R)- Go right ")
            direction = choose_direction()
            
            
            if direction == "l":
                print("Dead-end. Game over.")
                current_location = "intersection_3"
            
            
            elif direction == "s":
                current_location = "intersection_4"
            
            
            elif direction == "r":
                print("Car accident. Game over.")
                current_location = "intersection_3"
            
            
            else:
                print("Invalid choice. Please try again.")
                
        
        
        elif current_location == "intersection_4":
           
            print("You are at Intersection 4.")
            print("Choose your direction:")
            print("(L) - Go Left")
            print("(R) - Go Right")
            print("(S) - Go straight")
            direction = choose_direction()
           
           
            if direction == "l":
                print("You follow a dimly lit path but trip and fall into a deep manhole. Game over.")
                current_location = "intersection_4"
           
           
            elif direction == "s":
                print("You continue down the road but accidentally step on a loose board, falling into a sewer. Game over.")
                current_location = "intersection_4"
            
            
            elif direction == "r":
                current_location = "intersection_5"
            
            
            else:
                print("Invalid choice. Please try again.")
                
        
        
        elif current_location == "intersection_5":
            print("You are at Intersection 5.")
            print("Choose your direction:")
            print("(L) - You take a shortcut through a narrow alley.")
            print("(R) - You turn right")
            direction = choose_direction()
           
           
            if direction == "l":
                print("You take a shortcut through a narrow alley.(Y)(N)")
                mugger = choose_direction()
               
               
                if mugger == "y":
                    print("You get mugged and lose all your belongings. Game over.")
                    current_location = "intersection_5"
              
              
                elif mugger == "n":
                    print("You decide to avoid the alley")
                    current_location = "intersection_5"
             
             
                else:
                    print("Invalid choice. Please try again.")
          
          
            elif direction == "r":
                current_location = "forest_1"
          
          
            else:
                print("Invalid choice. Please try again.")

     
     
        elif current_location == "forest_1":
        

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
            print("Choose your direction:")
            print("(L) -you hear growling sound on your left.Dare to explore?")
            print("(S) - Straight")
            print("(R) - You spot an old abandoned shack on the right.")
            direction = choose_direction()
        
        
            if direction == "l":
                print("You proceed and encounter a Bear which tries to attack you but luckly u have a fire torch that scares it away\n\n you see a mysterious tree infront of you with a hollow trunk and an entrance to it, Dare to explore?(Y)(N)")
                Hollow_tree=choose_direction()

                if Hollow_tree=="y":
                    print("You explored a mysterious tree which teleported you to the end of the forest")
                    current_location="lake"
                elif Hollow_tree=="n":
                    print("You played safe and chose not to explore the tree")
                    current_location="forest_1"    

                else:
                    print("Invalid choice")
                    current_location = "forest_1"

       
       
            elif direction == "s":
                print("You encounter a peaceful clearing with a serene pond.\n\n enter:\n (L) rest by the pond and continue \n (R) take a dip in the pond ")
                pond_choice = choose_direction()
          
          
                if pond_choice == "l":
                    print("You sit by the pond for a while and enjoy the serenity. Continue on the main path.")
                    current_location = "forest_2"
         
         
                elif pond_choice == "r":
                    print("You decide to take a refreshing dip in the pond. Encountered a mythical sea monster.GameOver")
                    current_location = "forest_1"
          
          
                else:
                    print("Invalid choice. Please try again.")
         
         
            elif direction == "r":
                print("You spot an old abandoned shack.")
                shack_choice = choose_direction()
          
          
                if shack_choice == "l":
                    print("You cautiously approach the shack and peek inside, finding nothing of interest. Continue on the main path.")
                    current_location = "forest_2"
          
          
                elif shack_choice == "r":
                    print("You explore the shack but fall into a trap. GameOver")
                    current_location = "forest_1"
         
         
                else:
                    print("Invalid choice. Please try again.")
        
        
            else:
                print("Invalid choice. Please try again.")

      
      
        elif current_location == "forest_2":
            print("You are now deeper into the forest.")
            print("Choose your direction:")
            print("(L) - You see a potential shortcut to the island but see a warning sign about snakes on ur left")
            print("(S) - Keep going straight")
            print("(R) - You can see something bright on your right")
            direction = choose_direction()
        
        
            if direction == "l":
                print("You proceed and encounter a venomous snake! Game over.")
                current_location = "forest_2"
       
       
            elif direction == "s":
                current_location="lake"


       
       
            elif direction == "r":
                print("You fall of a cliff. GameOver")
                current_location="forest_2"
      
            else:
                print("Invalid choice. Please try again.")
                
      
      
        elif current_location == "lake":
            print("You have reached the end of the forest.")
            print("Choose your direction:")
            print("(R) - You see a bridge that might lead you to an island near the shore.")
            print("(L) - There is a trail that leads downhill.")
            direction = choose_direction()
       
       
            if direction == "r":
                print("The bridge collapses, and you fall into the river and die.")
                current_location = "lake"
     
     
            elif direction == "l":
               




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
