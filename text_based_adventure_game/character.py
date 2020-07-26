class Character:
    # Create a character
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None

    # Describe the character
    def describe(self):
        print(self.name + " is here!!!")
        print(self.description)

    # Setting what this character has to say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Make the character speak
    def talk(self):
        if self.conversation is not None:
            print(self.name + " says " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True


# Character is the super class of Enemy and Enemy is the sub class of Character
# An object of the sub class is also considered to be an object of the super class
class Enemy(Character):
    def __init__(self, enemy_name, enemy_description):
        # Calling the parent class's constructor and passing the parameters.
        # To make an Enemy, first make a Character object and then we'll customise it.
        super().__init__(enemy_name, enemy_description)
        self.weakness = None

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with your " + combat_item)
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

