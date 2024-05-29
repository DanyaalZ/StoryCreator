"""Character model containing gender, attributes of character"""
from JsonReader import JsonReader

class Character:
    def __init__(self, type: str, character_profile: JsonReader):
        #read character json file
        self.read_character_data = character_profile

        #type of character
        self.type = type
        
        #character's name
        self.name: str = ""

        #character's gender
        self.gender: str = ""

        #should be adjectives
        self.attributes : list[str] = []

    def set_name(self):
        pass

    def set_gender(self):
        pass

    def set_attributes(self):
        pass


class Protagonist(Character):
    def __init__(self, character_profile: JsonReader):
        super().__init__("Protagonist", character_profile)
        self.set_name()
        self.set_gender()
        self.set_attributes()