from text_based_adventure_game.room import Room
from text_based_adventure_game.item import Item

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

# Item class operations
sword = Item()
sword.set_name("Sword")
print(sword.get_name())

# Game control
current_room = kitchen

while True:
    current_room.get_details()
    direction = input(">")
    current_room = current_room.move(direction)

