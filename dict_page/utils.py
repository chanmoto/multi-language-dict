import json
from .models import Dictionary

def fill_model(filedir):
    data = json.load(open(filedir))
    for key, value in data.items():
        Dictionary = Dictionary(word=key, definition=value[0])
        Dictionary.save()


