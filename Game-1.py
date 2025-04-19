class Scenes:
    def __init__(self, person):
        self.person = person
        
    def Enter(self):
        SceneName = self.__class__.__name__
        print(f"{self.person} has entered {SceneName} scene")
        
class Death(Scenes):
    def __init__(self, person):
        super().__init__(person)
        
class Central_Corridoe(Scenes):
    def __init__(self, person):
        super().__init__(person)

class Laser_Armory(Scenes):
    def __init__(self, person):
        super().__init__(person)
        
class Engine:
    pass

    def play(self):
        pass

Hero = Laser_Armory("Mohamed")
Hero.Enter()