import pygame

#set up pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
clock = pygame.time.Clock()
#BMOs face color for screen fill
faceColor1 = (206, 255, 216) #modern desaturated screen color
faceColor2 = (201, 228, 195) #color from the sample BMO pictures, current go-to. 
faceColor3 = (192, 255, 204) #original green screen color
faceColor4 = (185, 243, 203) #slightly more saturated than OG, mid show run color

# fill the screen with a color to wipe away anything from last frame
screen.fill(faceColor2)

#add image of face to surface
testFace = pygame.image.load("BMO-Companion-Project/BMO/Graphics/Face1.png").convert_alpha()
#add the face to the screen (display surface)
facePosition = 450



#add text to the screen
font = pygame.font.Font(None, 70)
textSurface = font.render("Hello, I am BMO!", True, (0, 0, 0))


#main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    
    screen.blit(testFace, (facePosition, 250))
    screen.blit(textSurface, (500, 200))

    # update the display
    pygame.display.update()
    if facePosition > 1280: facePosition = -200
    else: facePosition += 4
    #limit to 60 fps
    clock.tick(60)


pygame.quit()