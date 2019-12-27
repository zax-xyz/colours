import re


def is_valid_colour(colour: str):
    preset = [
        'Red', 'Firebrick', 'Chocolate', 'OrangeRed', 'Coral',
        'GoldenRod', 'YellowGreen', 'Green', 'SeaGreen', 'SpringGreen',
        'DodgerBlue', 'Blue', 'BlueViolet', 'HotPink'
    ]
    
    if colour in preset or re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', colour):
        return True
    return False