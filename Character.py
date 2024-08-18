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
    
    #get the prompt for a character to feed into StoryCreator - this is a template function which will be overridden based on character type below
    def get_character_prompt(self):
        return ""


""" Main character in story - does not have to be good in nature (down to creativity of user - they could make anti-hero a trait for example)"""
class Protagonist(Character):
    def __init__(self):
        super().__init__("Protagonist", self.read_character_data)
        self.set_name()
        self.set_gender()
        self.set_attributes()

    def get_character_prompt(self):
        return f"The protagonist is called {self.name}, of the gender {self.gender}, and has the attributes {self.attributes}."

""" Side character type - could be antagonist or protagonist """
class SideCharacter(Character):
    def __init__(self, antagonist_set):
        #Set side character's type depending if antagonist is selected or not 
        super().__init__("Antagonist" if antagonist_set else "Supporting Character", self.read_character_data)

        self.set_name()
        self.set_gender()
        self.set_attributes()

    def get_character_prompt(self):
        return f"There is a character called {self.name}, of the gender {self.gender}, who is a(n) {self.type} and has the attributes {self.attributes}."
    