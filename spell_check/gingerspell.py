import sys
from gingerit.gingerit import GingerIt

def correct(input_text):
    parser = GingerIt()
    result = parser.parse(input_text)
    return result
