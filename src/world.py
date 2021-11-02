class World() :
    """
    Defines the player created world
    """
    def __init__(self, name: str) :
        self.name = name

    def update_name(self, new_name: str) :
        self.name = new_name