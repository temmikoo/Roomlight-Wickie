from rich import print
from rich.panel import Panel
from rich.prompt import Prompt

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
for room_id in range(1, 16):
    if room_id <= 10:
        room_type = "standard"
    else:
        room_type = "suite"

    room = Room(room_id, room_type, None, [])
    rooms.append(room)

# Functions

def createScene():
    # REQ-003: The system has scenes for different situations
    # REQ-004: Scenes can be adjusted without an electrician

    print(Panel(
        "[bold white]Select a scene to create[/bold white]\n\n"
        "[bold cyan]1:[/bold cyan] Welcome\n"
        "[bold cyan]2:[/bold cyan] Relax\n"
        "[bold cyan]3:[/bold cyan] Work\n"
        "[bold cyan]4:[/bold cyan] Night",
        title="[bold white]Create Scene[/bold white]",
        width=60,
        padding=(1, 2)
    ))

    choice = input("Select scene: ")
    print()

    if choice == "1":
        mode = "Welcome"
    elif choice == "2":
        mode = "Relax"
    elif choice == "3":
        mode = "Work"
    elif choice == "4":
        mode = "Night"

    active_lights = []
    light_names = ["main", "corners", "bathroom", "reading"]

    print(Panel(
        f"Started to create {mode} scene",
        title="[bold white]Light Configuration[/bold white]",
        width=60,
        padding=(1, 2)
    ))

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

    print(Panel(
        "[bold white]Available scenes[/bold white]\n\n" +
        "\n".join(f"[bold cyan]{i}:[/bold cyan] {scene.mode}" for i, scene in enumerate(scenes, start=1)),
        title="[bold white]Synchronize Scene[/bold white]",
         width=60,
         padding=(1, 2)
    ))
    print()

    sceneChoice = int(input("Select scene to synchronize: "))
    if sceneChoice < 1 or sceneChoice > len(scenes):
        print("Invalid scene selection.")
        return

    selected_scene = scenes[sceneChoice - 1]

    roomTypeChoice = input("Select room type (standard/suite/all): ")
    print()

    for room in rooms:
        if roomTypeChoice == "all" or room.room_type == roomTypeChoice:
            room.current_scene = selected_scene
            if selected_scene not in room.available_scenes:
                room.available_scenes.append(selected_scene)
    
    print(f"Scene '{selected_scene.mode}' synchronized to {roomTypeChoice} rooms.")
    print()

    return None


def show_available_scenes(rooms):
    lines = []

    for room in rooms:
        scene_names = []
        for scene in room.available_scenes:
            scene_names.append(scene.mode)

        label = f"{room.room_type.capitalize()} {room.room_id}"
        lines.append(f"{label:<12} | {', '.join(scene_names)}")

    content = "\n".join(lines)

    print(Panel(
        content,
        title="[bold white]Available scenes by room[/bold white]",
        width=60,
        padding=(1, 2)
    ))


def showOptions():
    print(Panel(
        "[bold cyan]1:[/bold cyan] Create a new scene\n"
        "[bold cyan]2:[/bold cyan] Synchronize a scene to rooms\n"
        "[bold cyan]3:[/bold cyan] Show synchronized scenes\n"
        "[bold red]0:[/bold red] Exit",
        title="[bold white]Main Menu[/bold white]",
        width=60,
        padding=(1, 2),
    ))


def staffMenu():
    print()
    print("[bold white on blue] RoomLight CLI Prototype [/bold white on blue]")
    print()
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
