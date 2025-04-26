from sys import exit
from random import randint
from Gothons Conv.txt import DIALOGUE

class Scenes:
    print("This scene is not yet configured!! ")
    print("This scene is not yet configured!! ")

class Central_Corridor(Scenes):
    def enter(self):
        print(DIALOGUE["CentralCorridor_enter"])
        action = input("> ")
        if action == "shoot!":
            print(DIALOGUE["CentralCorridor_shoot"])
        elif:
            
class Bridge(Scenes):
    pass
class Laser_Armory(Scenes):
    pass
class Escape_Pod(Scenes):
    pass
    
class Death(Scenes):
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]
    def enter(self):
        print (Death.quips[randint(0, len(self.quips)- 1)])
        exit(1) #ends the game with a non-zero code, signaling failure, It fits the logic of the game because the Death scene means you lose.

class Map:    
    scenes = 
    {"Central_Corridor":Central_Corridor(),
     "Bridge": Bridge(),
     "Laser_Armory": Laser_Armory(),
     "Escape_Pod": Escape_Pod(),
     "Death" : Death()}
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
class Engine:
    
    def __init__(self, Scene_Map):
        self.Scene_Map = Scene_Map

    def NavigateTheMap(self): #Engine to run the map!
        current_scene = self.Scene_Map.opening_scene()
        last_scene = self.Scene_Map.next_scene("Finished")
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()
    
            
            