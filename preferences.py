import json
from types import SimpleNamespace
class Init:

    def __init__(self) -> None:
        self.temp_preferences=any

    def open_json(self):
        return open('data/data.json', "r")
        
    def get_preferences(self):
        ruta = self.open_json()
        self.temp_preferences = json.loads(
        ruta.read(), object_hook=lambda d: SimpleNamespace(**d))
        ruta.close()
        return self.temp_preferences
