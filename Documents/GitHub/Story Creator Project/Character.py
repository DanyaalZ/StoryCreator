"""Character model containing gender, attributes of character"""

class Character:
    def __init__(self):
        self.gender: str = ""
        self.attributes : list[str] = []

       
    def validate_gender(self) -> bool:
        #make lowercase so any combination of capital/lowercase accepted
        self.gender = self.gender.lower()

        #validate - for now only male and female, but can be extended in future for inclusivity
        if self.gender != "male" or "female":
            return False 


