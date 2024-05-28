"""Read Json Files to access user preferences"""
import json
import pandas as pd 

class JsonReader:
    def __init__(self, file_name: str):
        self.file_name: str = ""

        if ".json" not in file_name:
            self.file_name = file_name + ".json"

        else:
            self.file_name = file_name

        self.json_text:dict = self.read_file()
    
    #read a json file
    def read_file(self) -> json:
        with open(self.file_name, "r") as file:
            return json.load(file)
    
    #get a result for a particular column
    def get_column(self, column_name:str) -> str:
        return self.json_text["column_name"]