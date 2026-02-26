from enum import Enum

# enum = string value, pair enum with string 
# if you want to pair it with int, can change str to int in class name ()
# state Iowa can be put in the string value
# enum doesn't need you to make an input box, it generates a drop down for users to select from
class TeslaModel(str, Enum):
    model_3 = '3'
    model_s = 'S'
    model_x = 'X'
    model_y = 'Y'