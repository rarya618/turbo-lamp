from world import World


class Game() :
    """
    Set up the game.
    """
    def __init__(self, world_file: str) :
        self.worlds = self.process_world(world_file)
        self.current_world = None

    def process_world(self, file_name: str) :
        """
        Processes the world file
        """
        world_file = open(file_name, 'r')
        temp = world_file.readlines()
        worlds: list[World] = []

        for obj in temp :
            worlds.append(World(obj.strip()))

        return worlds

    def list_worlds(self):
        for world in self.worlds:
            print(world.name)        

    def add_world(self, name: str) :
        self.worlds.append(World(name))
    
    def run(self) :
        # state of game
        running = True

        # list of commands
        commands = ["start", "stop", "new", "save", "list", "quit"]

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

                    print("Initialising World...")
                    created = True

                # 'new' command
                elif command[0] == "new":
                    if len(command) == 1:
                        world_name = input("Enter World name: ").strip()

                    else :
                        world_name = command[1]

                    print("Creating World...")
                    self.add_world(world_name)

                    print(world_name, "created.")

                # 'list' command
                elif command[0] == "list":
                    print("List of Worlds:")
                    self.list_worlds()

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