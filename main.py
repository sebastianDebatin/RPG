import pygame


##environment variables
#WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("RPG")



## constants
FPS = 60









def main():

    clock = pygame.time.Clock()
    run = True

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




















if __name__ == "__main__":
    main()