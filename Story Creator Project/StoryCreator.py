import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from typing import Optional

from Character import Character
from Prompt import Prompt

""" Story structure: A character with specified attributes, a scenario occurs, optionally tools are used
to either amplify or aid in scenario which could be a problem or benign, the scenario builds, has a climax
and finally concludes

Character -> Scenario (problem or benign) -> (Tools?) -> Build scenario -> Climax of scenario -> Conclusion """

""" Define NLP model, tokenizer to use """
class NaturalLanguageProcessor:
    def __init__(self):
        #model to use for story
        model_name = "gpt2-medium"

        #load model and tokenizer on initialisation
        self.model = GPT2LMHeadModel.from_pretrained(model_name) 
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)



"""This class is responsible for creating the story the user sees, and for building the prompt with information given by the user
to start and then further the story """
class StoryCreator(NaturalLanguageProcessor):
    def __init__(self, prompt: Prompt):
        super().__init__(self)

        """ Story to process """
        self.story: str = ""

        """ Prompt model  - taken from what is generated in user preferences (stored in json), including character data"""
        self.prompt: Prompt = prompt

        

    #TO GENERATE STORY - CHANGE WHEN READY
    def generate_story(self, prompt: str) -> str:
        inputs = self.tokenizer.encode(prompt, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=500, num_return_sequences=1, pad_token_id=self.tokenizer.eos_token_id)
        story = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return story

    
    

