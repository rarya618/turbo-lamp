# 'World' class
class World() :
    """
    Defines the player created world
    """
    def __init__(self, name: str, created: bool) :
        self.name = name
        self.created = created

    def update_name(self, new_name: str) :
        self.name = new_name

# state of game
running = True

# state of world
current: World = None

# list of commands
commands = ["start", "stop", "new", "save", "quit"]

# list of worlds
worlds = []

# starting game
print("Starting game...")
print("Welcome to Turbo Lamp! An interactive fiction game.\n")
print("Available commands:")
print(commands)

# command processing
while running:
    # input command
    command = input("> ").strip().split(" ")

    if command[0] in commands:
        # 'start' command
        if command[0] == "start":

            print("Initialising world...")
            created = True

        # 'new' command
        elif command[0] == "new":
            print("Creating world...")

        # 'quit' command
        elif command[0] == "quit":
            print("Exiting game...")

            running = False

        # undefined commands
        else:
            if not created:
                print("World does not exist.")

            print("Command undefined")

    else:
        print("Unknown command")
    
    print("")