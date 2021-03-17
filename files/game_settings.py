"""
Defines game settigns. This class should be saved as pickle file in case of leaving the game
"""

import pickle
import os



class settings():

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.game_title = "RPG"

    
    def save_settings(self):
        with open(os.path.normpath('./save.pkl'), 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def load_settings(self):
        with open(os.path.normpath('./save.pkl'), 'rb') as f:
            self = pickle.load(f)