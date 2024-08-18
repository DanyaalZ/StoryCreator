from Character import Character
from JsonReader import JsonReader
from Prompt import Prompt

"""Backend process which takes information given in frontend to process (e.g. prompts, characters, etc.)"""

#Get required information for story from respective json files

#Character builder
character_profile = JsonReader("Character.json")

#Story builder
story_profile = JsonReader("Story.json")

#Build the character
character = Character()

#Build the prompt
prompt = Prompt(character, story_profile)