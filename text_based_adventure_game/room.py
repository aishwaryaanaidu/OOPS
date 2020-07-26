class Room:
    # class variable declared outside the constructor
    number_of_rooms = 0

    def __init__(self, room_name):
        # instance variables declared inside the constructor
        self.name = room_name
        # Protected attribute description
        self._description = None
        self.linked_rooms = {}
        self.character = None
        Room.number_of_rooms += 1

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    # def show_description(self):
    #     print(self.description)
    #
    # def set_name(self, room_name):
    #     self.name = room_name
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    def get_name(self):
        return self.name

    # Room object has Character object inside it - Aggregation
    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print("Name: " + self.get_name() + '\n' + "Description: " + self.get_description())
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is towards the " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
