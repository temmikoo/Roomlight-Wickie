# RoomLight CLI prototype
# Hotel lighting control system (command-line version)

# Core idea:
# - Create lighting scenes
# - Assign scenes to rooms
# - Sync scenes across rooms

##################################################################

# Classes

class Scene:
    def __init__(self, mode, active_lights):
        self.mode = mode
        self.active_lights = active_lights

class Room:
    def __init__(self, room_id, current_scene):
        self.room_id = room_id
        self.current_scene = current_scene

class Light:
    def __init__(self, id, is_on, brightness, color_temperature):
        self.id = id
        self.is_on = is_on
        self.brightness = brightness
        self.color_temperature = color_temperature

class System:
    def __init__(self, rooms, scenes, room_groups):
        self.rooms = rooms
        self.scenes = scenes
        self.room_groups = room_groups

class Synchronization:
    def __init__(self, scene, room_groups, rooms):
        self.scene = scene
        self.room_groups = room_groups
        self.rooms = rooms

# Functions

def createScene():
    # REQ-003: The system has scenes for different situations
    # REQ-004: Scenes can be adjusted without an electrician

    active_lights = []
    light_names = ["main", "corners", "bathroom", "reading"]

    for light in light_names:
            is_on_input = input(f"Turn on {light}? (y/n): ")
            if is_on_input == "y":
                is_on = True
                brightness = int(input(f"{light} brightness (0-100): "))
                color_temperature = input(f"{light} color temperature (cold/medium/warm): ")
            else:
                is_on = False
    


            light = Light(light, is_on, brightness, color_temperature)
            active_lights.append(light)


    print("Select mode: ")
    print("1: Welcome")
    print("1: Relax")
    print("1: Work")
    print("1: Night")

    choice = input("Choose mode: ")

    if choice == "1":
        mode = "Welcome"
    elif choice == "2":
        mode = "Relax"
    elif choice == "3":
        mode = "Work"
    elif choice == "4":
        mode = "Night"

    scene = Scene(mode, active_lights)
    return scene

def showOptions():
    print("Options:")
    print("1: Create new scene")
    print("2. Assign scene to rooms")
    choice = input("Select option 1 or 2: ")
    if choice == "1":
        createScene()
    elif choice == "2":
        assignScene()
    

def staffMenu():
    while True:
        showOptions()

createScene()