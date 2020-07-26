from text_based_adventure_game.character import Character, Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation("I would like to be your friend")
dave.talk()
dave.set_weakness("cheese")

print("What do you want to fight with?")
fight_with = input()
dave.fight(fight_with)
