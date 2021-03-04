import pygame
import os


##environment variables
#WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("RPG")




## constants
FPS = 60



def load_assets(dir_assets):
    assets = {}
    for filename in os.listdir(dir_assets):
        if filename.endswith('.png'):
            path = os.path.join(dir_assets, filename)
            key = filename[:-4]
            assets[key] = pygame.image.load(path).convert()

    return assets


def draw_window(WIN,assets):
    WIN.fill((0,0,0))
    WIN.blit(assets["tile_rock"],(0,0))

    pygame.display.update()




def main():


    assets = load_assets("./assets")
    clock = pygame.time.Clock()
    run = True
    print(assets["tile_rock"])
    

    while run:
        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_a:
            #         run = False
            #         pygame.quit()




        draw_window(WIN,assets)




















if __name__ == "__main__":
    main()