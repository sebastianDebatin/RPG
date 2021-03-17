"""
This class describes the playable player object

"""



class player():
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.velocity = 16


    def move_left(self): # todo: find out how WIDTH and HEIGHT can be sent to this class without heving to create a gamsetate object
        if self.posx > 0 + self.velocity:
            self.posx -= self.velocity

    def move_right(self):
        if self.posx < 800 - self.velocity:
            self.posx += self.velocity

    def move_up(self):
        if self.posy > 0 + self.velocity:
            self.posy -= self.velocity

    def move_down(self):
        if self.posy < 800 - self.velocity:
            self.posy += self.velocity