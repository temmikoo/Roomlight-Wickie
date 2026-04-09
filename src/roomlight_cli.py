# RoomLight CLI prototype
# Hotel lighting control system (command-line version)

# Core idea:
# - Create lighting scenes
# - Synchronize scenes to rooms

##################################################################

# Classes

class Scene:
    def __init__(self, mode, active_lights):
        self.mode = mode
        self.active_lights = active_lights

class Room:
    def __init__(self, room_id, room_type, current_scene, available_scenes):
        self.room_id = room_id
        self.room_type = room_type
        self.current_scene = current_scene
        self.available_scenes = available_scenes

class Light:
    def __init__(self, light_id, is_on, brightness, color_temperature):
        self.light_id = light_id
        self.is_on = is_on
        self.brightness = brightness
        self.color_temperature = color_temperature


# Stored system data

scenes = []

rooms = []
for room_id in range(1, 51):
    if room_id <= 40:
        room_type = "standard"
    else:
        room_type = "suite"

    room = Room(room_id, room_type, None, [])
    rooms.append(room)

# Functions

def createScene():
    # REQ-003: The system has scenes for different situations
    # REQ-004: Scenes can be adjusted without an electrician

    print("Select a scene to create")
    print("1: Welcome")
    print("2: Relax")
    print("3: Work")
    print("4: Night")

    choice = input("Select scene: ")
    print()

    if choice == "1":
        mode = "Welcome"
        print("Started to create Welcome scene")
        print()
    elif choice == "2":
        mode = "Relax"
        print("Started to create Relax scene")
        print()
    elif choice == "3":
        mode = "Work"
        print("Started to create Work scene")
        print()
    elif choice == "4":
        mode = "Night"
        print("Started to create Night scene")
        print()

    active_lights = []
    light_names = ["main", "corners", "bathroom", "reading"]

    for light in light_names:
            is_on_input = input(f"Turn on {light}? (y/n): ")
            if is_on_input == "y":
                is_on = True
                brightness = int(input(f"{light} brightness (0-100): "))
                color_temperature = input(f"{light} color temperature (cold/medium/warm): ")
                print()
            else:
                is_on = False
                brightness = 0
                color_temperature = "off"
                print()
    
            light = Light(light, is_on, brightness, color_temperature)
            active_lights.append(light)

    scene = Scene(mode, active_lights)
    scenes.append(scene)
    print(f"Scene '{scene.mode}' created")
    print()

    return scene


def syncSceneToRooms():
    # REQ-001 Scenes can be synchronized automatically to all rooms

    print("Available scenes:")
    for scene in scenes:
        print(scene.mode)    

    print()
    sceneChoice = input("Select scene to synchronize: ")
    selected_scene = None
    for scene in scenes:
        if scene.mode == sceneChoice:
            selected_scene = scene
    if selected_scene == None:
        print("Scene not found.")
        return

    roomTypeChoice = input("Select room type (standard/suite/all): ")
    print()

    for room in rooms:
        if roomTypeChoice == "all" or room.room_type == roomTypeChoice:
            room.current_scene = selected_scene
            if selected_scene not in room.available_scenes:
                room.available_scenes.append(selected_scene)
    
    print(f"Scene '{sceneChoice}' synchronized to {roomTypeChoice} rooms.")
    print()

    return None


def show_available_scenes(rooms):
    for room in rooms:
        scene_names = []
        for scene in room.available_scenes:
            scene_names.append(scene.mode)
        print(f"Huone {room.room_id}: {', '.join(scene_names)}")


def showOptions():
    print("Options:")
    print("1: Create a new scene")
    print("2: Synchronize a scene to rooms")
    print("3: Show synchronized scenes")
    print("0: Exit")


def staffMenu():
    while True:
        showOptions()
        choice = input("Select option: ")
        print()
        if choice == "1":
            createScene()
        elif choice == "2":
            syncSceneToRooms()
        elif choice == "3":
            show_available_scenes(rooms)
        elif choice == "0":
            break

staffMenu()

