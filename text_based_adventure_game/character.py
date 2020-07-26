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
