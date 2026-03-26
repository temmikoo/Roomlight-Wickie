# Domain Model for RoomLight

## Key Concepts

- Scene
- Room
- Light
- System
- User
- Brightness Slider
- User Input
- Button
- Room Control Panel
- Staff Interface
- Sleep Program
- Wake Up Program
- Synchronization

## Relationships

```text
System 1 ---- 1..* Room
System 1 ---- 1..* Room Control Panel
System 1 ---- 1 Staff Interface
System 1 ---- 1..* Scene
System --> Synchronization

Synchronization --> Scene
Synchronization --> Room

Room 1 ---- 1 Room Control Panel

User --> User Input
User Input --> Room Control Panel

Room Control Panel 1 ---- 0..* Button
Room Control Panel 1 ---- 1 Brightness Slider
Room Control Panel --> Scene
Room Control Panel --> Sleep Program
Room Control Panel --> Wake Up Program

Staff Interface --> Scene
Staff Interface --> Synchronization

Brightness Slider --> Light
Scene --> Light
```
