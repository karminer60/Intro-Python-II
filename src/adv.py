from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player(' ', 'outside')




name = input('What is your name?: ')
room = room[player.room]
print(f"You are currently here: {player.room},")

while True:

    choice = input("Where would you like to go?: ")

    breakpoint()

    if choice == 'south' and hasattr(room, "s_to"):
        room = room.s_to
        print(room)

    elif choice == 'north'and hasattr(room, "n_to"):
        room = room.n_to
        print(room)

    elif choice == 'west' and hasattr(room, "w_to"):
        room = room.w_to
        print(room)

    elif choice == 'east' and hasattr(room, "e_to"):
        room = room.e_to
        print(room)
    
    elif choice == 'quit':
        print('Thank you for playing')
        break

    else: 
        print('Does not exist')
    