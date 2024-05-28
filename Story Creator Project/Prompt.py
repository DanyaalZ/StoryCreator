"""Prompt object will hold information from user story preferences json to use in StoryCreator"""
from typing import Optional

from Character import Character
from JsonReader import JsonReader

class Prompt:
    def __init__(self, character: Character):
        self.character = character

        #tools to overcome or aid problem (optional)
        self.tools: Optional[list] = []

        #story scenario, build, climax and conclusion
        self.scenario: str = ""
        self.build: str = ""
        self.climax: str = ""
        self.conclusion: str = ""

    
    
