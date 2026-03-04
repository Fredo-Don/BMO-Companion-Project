import pygame

#set up pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
clock = pygame.time.Clock()
#BMOs face color for screen fill
faceColor1 = (206, 255, 216) #modern desaturated screen color, go with this one for now.
faceColor2 = (192, 255, 204) #original green screen color
faceColor3 = (185, 243, 203) #slightly more saturated than OG, mid show run color

#main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(faceColor1)

    # update the display
    pygame.display.flip()
    #limit to 60 fps
    clock.tick(60)


pygame.quit()