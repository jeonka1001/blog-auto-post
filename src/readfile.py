import json

def read_conf(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data