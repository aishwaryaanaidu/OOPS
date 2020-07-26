from text_based_adventure_game.room import Room
from text_based_adventure_game.item import Item
from text_based_adventure_game.character import Enemy, Friend
from text_based_adventure_game.game_info import GameInfo

# Displaying game related information
spooky_castle = GameInfo("Spooky Castle")
spooky_castle.welcome()
GameInfo.info()
GameInfo.author = "Aishwarya M S"

# Room class initializations
kitchen = Room("Kitchen")
study_room = Room("Study Room")
dining_hall = Room("Dining Hall")

# Setting Room class descriptions
kitchen.set_description("Place where you can cook yummy food")
study_room.set_description("Place where you study")
dining_hall.set_description("Place where you have food")

# Linking rooms
kitchen.link_room(study_room, "east")
study_room.link_room(kitchen, "west")
kitchen.link_room(dining_hall, "north")
dining_hall.link_room(kitchen, "south")

# Creating an Enemy
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("I'm gonna kill you")
dave.set_weakness("cheese")
study_room.set_character(dave)

# Creating a Friend
catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Hello there:D")
kitchen.set_character(catrina)

print("You have " + str(Room.number_of_rooms) + " rooms available to explore")

# Item class operations
sword = Item()
sword.set_name("Sword")
# print(sword.get_name())

directions = ['east', 'west', 'north', 'south']
# Game control
current_room = kitchen
dead = False

while dead is False:
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input(">")
    if command in directions:
        current_room = current_room.move(command)
    elif command == 'talk':
        if inhabitant is None:
            # Asking the inhabitant to speak
            inhabitant.talk()
    elif command == 'fight':
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print('What will you fight with?')
            fight_with = input()
            dead = inhabitant.fight(fight_with)
        else:
            print("There is no one in this room with whom you can fight")
    elif command == 'hug':
        if inhabitant is not None:
            if isinstance(inhabitant, Friend):
                inhabitant.hug()
            else:
                print("I wouldn't do that if I were you")
        else:
            print("There is nobody to hug in this room :(")

GameInfo.credits()

