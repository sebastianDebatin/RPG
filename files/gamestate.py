"""
This class defines the loops that run depending on the current level
load() serves as an init function that is called only the first time after initiating the class object
Each level contains its own draw_window() function and keyboard handling


"""



import os
import sys
import json



class gamestate():
    def __init__(self,WIN,pygame):
        self.run = True
        self.state = "menu"
        self.WIN = WIN
        self.pygame = pygame



    def gamestate_manager(self):
        if self.state == "quit":
            self.run = False
            self.pygame.quit()
        if self.state == "menu":
            self.menu_loop()
        

    def load(self):
        #print("load")
        def draw_window():
            self.WIN.fill((0,0,0))
            loading = self.pygame.draw.rect(self.WIN, (255,0,0), (175, 75, 200, 100), 2)
            self.pygame.display.update()

        draw_window()    
        self.tiles = self.load_tiles("./files/tiles.json")
        print(self.tiles)
        self.pygame.time.wait(5000) # test purpose



    def menu_loop(self):
        #print("menu")
        def draw_window():
            self.WIN.fill((0,0,0))
            self.WIN.blit(self.tiles["rock"]["image"],(0,0))
            self.pygame.display.update()

        
        for event in self.pygame.event.get():

            if event.type == self.pygame.QUIT:
                self.state = "quit"

            if event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_a:
                    self.state = "quit"
        
        draw_window()

    def load_tiles(self, path):
        tiles = {}

        with open(path) as f:
            t = json.load(f)
            for tile in t:
                tile = t[tile]
                dic = {}
                dic["identifier"] = tile["identifier"]
                dic["image"] = self.pygame.image.load(tile["path"]).convert()
                dic["transparent"] = tile["transparent"]
                dic["solid"] = tile["solid"]
                tiles[tile["name"]] = dic
        return tiles


    def newlevel_loop(self):
        def draw_window():
            self.WIN.fill((0,0,0))
            #self.WIN.blit(self.assets["tile_rock"],(0,0))
            self.pygame.display.update()

        for event in self.pygame.event.get():

            if event.type == self.pygame.QUIT:
                self.state = "quit"



    # def load_assets(self,dir_assets):
    #     assets = {}
    #     for filename in os.listdir(dir_assets):
    #         if filename.endswith('.png'):
    #             path = os.path.join(dir_assets, filename)
    #             key = filename[:-4]
    #             assets[key] = self.pygame.image.load(path).convert()

    #     return assets






    