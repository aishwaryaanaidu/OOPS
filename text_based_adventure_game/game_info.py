class GameInfo:
    author = "Anonymous"

    def __init__(self, title):
        self.title = title

    def welcome(self):
        print("Welcome to " + self.title)

    @staticmethod
    def info():
        print("Made using OOPS")

    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print("Created by " + cls.author)
