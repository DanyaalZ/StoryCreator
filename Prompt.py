"""Prompt object will hold information from user story preferences json to use in StoryCreator"""
from typing import Optional

from Character import Character
from JsonReader import JsonReader

class Prompt:
    def __init__(self, character: Character, story_profile: JsonReader):
        #running objects from backend.py
        self.character = character
        self.read_prompt_data = story_profile

        #story scenario, build, climax and conclusion
        self.scenario: str = self.get_scenario()
        self.build: str = self.get_build()
        self.climax: str = self.get_climax()
        self.conclusion: str = self.get_conclusion()

        #tools to overcome or aid problem (optional, defined by GetTools? column in json)
        self.decide_tools: bool = self.decide_tools(self.read_prompt_data("GetTools?"))
        #potential tools list
        self.tools: Optional[list] = []

        #the final prompt to be read
        self.final_prompt = ""

    def create_final_prompt(self) -> str:
        return f"Write a story where {self.scenario} occurs. {self.build} {self.climax} {self.conclusion} If this given list is not empty, the tools within it are used to amplify the resolve of the character in the story."

    #get given scenario data, if nothing is given default to 'surprise me' type story
    def get_scenario(self) -> str:
        scenario = self.read_prompt_data.get_column("Scenario")

        #make sure scenario is present else create random story
        if scenario == "":
            return "a random scenario - it could be positive or negative, but should be respectful"

        else:
            return scenario    

    #same for build of story (story builds up)
    def get_build(self) -> str:
        build = self.read_prompt_data.get_column("Build")

        #make sure build is present
        if build == "":
            return "This story builds up towards a climax,"

        else:
            return build
        
    #same for climax of story (story reaches max point of tension/suspense or positive infliction)
    def get_climax(self) -> str:
        climax = self.read_prompt_data.get_column("Climax")

        #make sure climax is present
        if climax == "":
            return "and it then reaches its peak - a surprising twist."

        else:
            return climax
        
    #same for conclusion of story (story concludes)
    def get_conclusion(self) -> str:
        conclusion = self.read_prompt_data.get_column("Conclusion")

        #make sure conclusion is present
        if conclusion == "":
            return "Finally, the story comes to a well-rounded conclusion."

        else:
            return conclusion
     
    #decide to use tools or not
    def decide_tools(self, tools_included: str) -> Optional[list]:
        if tools_included == "True":
            return True

    #if tools are decided to be used, use them
    def get_tools(self):
       if self.decide_tools:
           self.tools = lambda: self.read_prompt_data("Tools").split(", ") 