import json
import os

def load_dataset1(path):
    """
    get the desired data, return type is dictionary of desired fields
    """
    json_dict_array = []
    with open(path, 'r') as file:
        for line in file:
            json_dict_array.append(json.loads(line))
    return json_dict_array

def eval_metrics():
    """
    
    """