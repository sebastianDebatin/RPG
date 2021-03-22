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
from files.object_classes import player



class gamestate():
    def __init__(self,WIN,pygame):
        self.run = True
        self.state = "level_1"
        self.last_state = ""
        self.WIN = WIN
        self.pygame = pygame
        self.tiles = ""        
        self.map_image = ""
        self.inventory_image = ""
        self.charactermenu_image = ""
        self.player = player()




    def gamestate_manager(self):
        if self.state == "quit":
            self.run = False
            self.pygame.quit()
        if self.state == "level_1":
            if self.last_state != self.state: # reset map_image in case of changed level
                self.map_image = ""
            self.level_1_loop()
        if self.state == "main_menu":
            if self.last_state != self.state:
                self.map_image = ""
            self.main_menu_loop()

    def main_menu_loop(self):
        def draw_window():
            pass

        if not self.map_image: # load map if this loop is called the first time
            self.load_map("main_menu")

        for event in self.pygame.event.get():

            if event.type == self.pygame.QUIT:
                self.state = "quit"

        draw_window()
        self.last_state = "main_menu"


    def level_1_loop(self):
        #print("level_1")
        def draw_window():
            self.WIN.fill((0,0,0))
            self.WIN.blit(self.map_image,(0,0))
            self.pygame.draw.rect(self.WIN,(255,0,0),(self.player.posx, self.player.posy, 16, 16))
            self.pygame.display.update()

        if not self.map_image: # load map if this loop is called the first time
            self.load_map("level_1")
        
        self.handle_user_input()
        
        draw_window()
        self.last_state = "level_1"

    def load(self):

        def draw_window():
            self.WIN.fill((0,0,0))
            loading = self.pygame.draw.rect(self.WIN, (255,0,0), (175, 75, 200, 100), 2)
            self.pygame.display.update()

        draw_window()    

        #load assets
        self.tiles = self.load_tiles(os.path.normpath("./files/tiles.json"))
        self.inventory_image = self.pygame.image.load(os.path.normpath(r"files\assets\inventory.png")).convert()
        self.charactermenu_image = self.pygame.image.load(os.path.normpath(r"files\assets\charactermenu.png")).convert()

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
                #player movement
                if event.key == self.pygame.K_w:
                    self.player.move_up()
                if event.key == self.pygame.K_a:
                    self.player.move_left()
                if event.key == self.pygame.K_s:
                    self.player.move_down()
                if event.key == self.pygame.K_d:
                    self.player.move_right()


                # keys for menus
                if event.key == self.pygame.K_i:
                    self.open_inventory()

                if event.key == self.pygame.K_c:
                    self.open_character_menu()

                if event.key == self.pygame.K_ESCAPE:
                    pass

    
    def open_inventory(self):
        
        def draw_inventory():
            self.WIN.fill((0,0,0))
            self.WIN.blit(self.map_image,(0,0))
            
            #self.pygame.draw.rect(self.WIN, (255,0,0), (200, 200, 400, 400), 2)
            #inventory
            self.WIN.blit(self.inventory_image,(200,200))


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



    def open_character_menu(self):

        def draw_character():
            self.WIN.fill((0,0,0))
            self.WIN.blit(self.map_image,(0,0))
            
            #self.pygame.draw.rect(self.WIN, (255,0,0), (200, 200, 400, 400), 2)

            self.WIN.blit(self.charactermenu_image,(200,200))


            self.pygame.display.update()

        draw_character()

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
            self.load_map("newlevel")

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






    