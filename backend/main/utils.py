import re
import colorsys


def is_valid_colour(colour: str):
    preset = [
        'Red', 'Firebrick', 'Chocolate', 'OrangeRed', 'Coral',
        'GoldenRod', 'YellowGreen', 'Green', 'SeaGreen', 'SpringGreen',
        'DodgerBlue', 'Blue', 'BlueViolet', 'HotPink'
    ]
    
    if colour in preset or re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', colour):
        return True
    return False


def get_colours(num):
    diff = 360 // num
    rgbs = [colorsys.hls_to_rgb(h / 360, 0.5, 1) for h in range(0, 360, diff)]
    hexes = ['#' + ''.join('%02X' % round(i * 255) for i in r) for r in rgbs]
    return hexes
