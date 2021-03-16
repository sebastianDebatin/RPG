"""
This class defines the loops that run depending on the current level
load() serves as an init function that is called only the first time after initiating the class object
Each level contains its own draw_window() function and keyboard handling


"""



import os
import sys
import json
import csv
from pytmx.util_pygame import load_pygame
from files.player import player



class gamestate():
    def __init__(self,WIN,pygame):
        self.run = True
        self.state = "menu"
        self.last_state = ""
        self.WIN = WIN
        self.pygame = pygame
        self.tiles = ""        
        self.map_image = ""
        self.player = player()




    def gamestate_manager(self):
        if self.state == "quit":
            self.run = False
            self.pygame.quit()
        if self.state == "menu":
            if self.last_state != "menu": # reset map_image in case of changed level
                self.map_image = ""
            self.menu_loop()


    def menu_loop(self):
        #print("menu")
        def draw_window():
            self.WIN.fill((0,0,0))
            self.WIN.blit(self.map_image,(0,0))
            self.pygame.display.update()

        if not self.map_image: # load map if this loop is called the first time
            self.load_map("menu")
        
        self.handle_user_input()
        
        draw_window()
        self.last_state = "menu"

    def load(self):
        #print("load")
        def draw_window():
            self.WIN.fill((0,0,0))
            loading = self.pygame.draw.rect(self.WIN, (255,0,0), (175, 75, 200, 100), 2)
            self.pygame.display.update()

        draw_window()    
        self.tiles = self.load_tiles(os.path.normpath("./files/tiles.json"))
        print(self.tiles)
        #self.pygame.time.wait(1000) # test purpose

    def load_tiles(self, path):
        tiles = {}

        with open(path) as f:
            t = json.load(f)
            for tile in t:
                tile = t[tile]
                dic = {}
                dic["name"] = tile["name"]
                dic["identifier"] = tile["identifier"]
                dic["image"] = self.pygame.image.load(tile["path"]).convert()
                dic["transparent"] = tile["transparent"]
                dic["solid"] = tile["solid"]
                tiles[tile["identifier"]] = dic
        return tiles



    def load_map(self,name):

        DELTA = 16# width and height of the pixarts. # todo: move to global variables
        self.map_image = self.pygame.Surface(self.pygame.display.get_surface().get_size()) # init map with size of WIN
        tmxdata = load_pygame(os.path.normpath(os.path.join("files\maps" ,name + ".tmx")))

        for layer in tmxdata:
            for tile in layer.tiles():
                x = tile[0] * DELTA
                y = tile[1] * DELTA
                self.map_image.blit(tile[2],(x,y))

        # with open(os.path.normpath("./files/levels.json")) as f:
        #     m = json.load(f)
        #     map = m[name]["map"]

        #     y = 0    
        #     for row in map:
        #         x = 0    
        #         for column in row:                
        #             self.map_image.blit(self.tiles[map[y][x]]["image"],(x*delta,y*delta))
        #             x += 1
        #         y += 1


    def handle_user_input(self):

        for event in self.pygame.event.get():

            if event.type == self.pygame.QUIT:
                self.state = "quit"

            if event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_a:
                    self.state = "quit"

                if event.key == self.pygame.K_i:
                    self.open_inventory()

    
    def open_inventory(self):
        
        def draw_inventory():
            self.WIN.fill((0,0,0))
            self.WIN.blit(self.map_image,(0,0))
            
            self.pygame.draw.rect(self.WIN, (255,0,0), (175, 75, 200, 100), 2)


            self.pygame.display.update()

        draw_inventory()

        running = True

        while running:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.state = "quit"

                if event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_ESCAPE:
                        running = False



        






    def newlevel_loop(self):
        def draw_window():
            self.WIN.fill((0,0,0))
            #self.WIN.blit(self.assets["tile_rock"],(0,0))
            self.pygame.display.update()

        if not self.map_image: # load map if this loop is called the first time
            self.load_map("menu")

        for event in self.pygame.event.get():

            if event.type == self.pygame.QUIT:
                self.state = "quit"

        draw_window()
        self.last_state = "newlevel"



    # def load_assets(self,dir_assets):
    #     assets = {}
    #     for filename in os.listdir(dir_assets):
    #         if filename.endswith('.png'):
    #             path = os.path.join(dir_assets, filename)
    #             key = filename[:-4]
    #             assets[key] = self.pygame.image.load(path).convert()

    #     return assets






    