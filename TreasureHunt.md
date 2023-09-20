###################################################################################################################################################

                                                                  1. TreasureHunt


This is a text-based treasure hunt game where the player starts in a city and must make choices at various intersections and locations to ultimately find the hidden treasure on an island. The game uses a while loop to keep the player engaged until they either find the treasure or choose to quit.

Answer Roadmap to Find the Treasure:

// Starting Point:

Choose to enter the city by selecting "S" (Straight).
You will arrive at Intersection 1.

// Intersection 1:

You have three options:
Choose "L" (Left): You encounter a gang and the game ends.
Choose "R" (Right): You proceed to Intersection 2.
Choose "S" (Straight): You enter a dark alleyway and have the option to explore it further.

// Dark Alleyway (Intersection 1, S):

You can choose to explore the alleyway by selecting "Y" (Yes) or "N" (No).
If you choose "Y," you find nothing valuable, and you return to Intersection 1.
If you choose "N," you decide it's too risky and return to Intersection 1.

// Intersection 2:

You have three options:
Choose "L" (Left): You reach a dead-end and return to Intersection 2.
Choose "R" (Right): You find a hidden message about the treasure and proceed to Intersection 5.
Choose "S" (Straight): You proceed to Intersection 3.

// Intersection 3:

You have three options:
Choose "L" (Left): You reach a dead-end, and the game ends.
Choose "R" (Right): You encounter a car accident, and the game ends.
Choose "S" (Straight): You proceed to Intersection 4.

// Intersection 4:

You have three options:
Choose "L" (Left): You follow a dimly lit path and fall into a manhole, ending the game.
Choose "R" (Right): You proceed to Intersection 5.
Choose "S" (Straight): You continue down the road and fall into a sewer, ending the game.

// Intersection 5:

You have two options:
Choose "L" (Left): You take a shortcut through a narrow alley and may encounter a mugger.
If you encounter a mugger and choose "Y" (Yes), you get mugged and lose your belongings, ending the game.
If you choose "N" (No), you avoid the alley.
Choose "R" (Right): You proceed to the forest (Forest 1).

// Forest 1:

You have three options:
Choose "L" (Left): You explore further, encounter a bear, but scare it away with a torch.
You find a mysterious tree and can choose to explore it.
If you explore the tree, you're teleported to the end of the forest (Lake).
If you choose not to explore, you stay in Forest 1.
Choose "S" (Straight): You find a pond and have two options:
Choose "L" (Left) to rest by the pond and continue (leads to Forest 2).
Choose "R" (Right) to take a dip in the pond and encounter a sea monster, ending the game.
Choose "R" (Right): You find an old abandoned shack with two options:
Choose "L" (Left) to cautiously approach the shack and find nothing interesting (leads to Forest 2).
Choose "R" (Right) to explore the shack and fall into a trap, ending the game.

// Forest 2:

You have three options:
Choose "L" (Left): You encounter a venomous snake and the game ends.
Choose "S" (Straight): You reach the end of the forest (Lake).
Choose "R" (Right): You fall off a cliff, and the game ends.
Lake:

You have two options:
Choose "R" (Right): The bridge collapses, and you fall into the river, ending the game.
Choose "L" (Left) to reach the river bank with a boat.
Choose "Y" (Yes) to take the boat to the island, where you find the treasure and win the game.
Choose "N" (No) to end the game.

Note: The game loop allows you to play again if you didn't find the treasure.

End
###################################################################################################################################################