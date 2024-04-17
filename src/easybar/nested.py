from .utils import get_flatform
import os


class NestedBar(Wrapper):
    
    def __init__(self):
        _platform = get_flatform()

        if _platform == 'Windows':
            pass

    def __str__(self):
        
