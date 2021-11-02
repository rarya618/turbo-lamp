from world import World


class Game() :
    """
    Set up the game.
    """
    def __init__(self, world_file: str) :
        self.world_file = world_file

    def process_world(self) :
        """
        Processes the world file
        """
        worlds: list[World] = []

        return worlds
    
    def run(self) :
        # state of game
        running = True

        # state of world
        current: World = None

        # list of commands
        commands = ["start", "stop", "new", "save", "list", "quit"]

        # list of worlds
        worlds: list[World] = self.process_world()

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
                    worlds.append(World(command[1], True))

                    print("World created...")

                # 'list' command
                elif command[0] == "list":
                    for world in worlds:
                        print(world.name)

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