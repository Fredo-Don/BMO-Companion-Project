import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Button!")
#fonts can only be stretched to sizes they are multiples of. Grand9k is 8 px, so 40, 48, 56, etc. Minecraft is 16 px, so 32, 48, 64, etc.
mainFont = pygame.font.Font("BMO-Companion-Project/BMO/Graphics/Grand9K_Pixel.ttf", 40) #use custom font
#button surfaces. Load image -> stretch to desired size.
buttonSurface = pygame.image.load("BMO-Companion-Project/BMO/Graphics/buttonTemplate2.png").convert_alpha() #default button template.
buttonSurface = pygame.transform.scale(buttonSurface, (250, 50))

class Button():
    def __init__(self, image, xPos, yPos, textInput, paddingColor, borderColor, altBorderColor):
        self.image = image #button surface
        #positioning
        self.xPos = xPos
        self.yPos = yPos
        self.rect = self.image.get_rect(center=(self.xPos, self.yPos)) #button rect
        #button display text
        self.textInput = textInput
        self.text = mainFont.render(self.textInput, True, (0, 0, 0)) #black text
        self.textRect = self.text.get_rect(center=(self.xPos, self.yPos)) #text rect
        #layers
        self.middlePadding = 6
        self.borderPadding = 12
        self.paddingColor = paddingColor
        self.borderColor = borderColor
        self.altBorderColor = altBorderColor

    def update(self):
        #create rects for button layers. Values can be changed to get proper thickness.
        borderRect = self.rect.inflate(self.borderPadding*2-3, self.borderPadding*2)
        paddingRect = self.rect.inflate(self.middlePadding*2-3, self.middlePadding*2-2)
        
        #change button color to highlight it when hovered, draw button layers in correct order.
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, self.altBorderColor, borderRect) #altBorderColor
            pygame.draw.rect(screen, self.paddingColor, paddingRect)
            self.text = mainFont.render(self.textInput, True, (255, 179, 47)) #golden orange
        #display default black border when not hovered    
        else:
            pygame.draw.rect(screen, self.borderColor, borderRect) #borderColor
            pygame.draw.rect(screen, self.paddingColor, paddingRect)
            self.text = mainFont.render(self.textInput, True, (0, 0, 0)) #black 
        
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.textRect)

    def checkForInput(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            print("Button Pressed")
            #add functionality for button press here based on button subclasses.


class returnButton(Button):
    def __init__(self, image, xPos, yPos, textInput, paddingColor, borderColor, altBorderColor):
        super().__init__(image, xPos, yPos, textInput, paddingColor, borderColor, altBorderColor)

    def checkForInput(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            print("Return Button Pressed")
            #add functionality for return button press here.

class gpButton(Button):
    def __init__(self, image, xPos, yPos, textInput, paddingColor, borderColor, altBorderColor):
        super().__init__(image, xPos, yPos, textInput, paddingColor, borderColor, altBorderColor)
        self.pressed = False

    def checkForInput(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            print("GP Button Pressed")
            #add functionality for GP button press here.
            self.pressed = not self.pressed




if __name__ == "__main__":
    #small testing playground
    button = Button(buttonSurface, 400, 290, "Button", (240, 235, 210), (0, 0, 0), (255, 179, 47)) #white, black, alt golden orange
    button2 = returnButton(buttonSurface, 400, 90, "Return  ", (240, 235, 210), (0, 0, 0), (255, 179, 47))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                button.checkForInput()
                button2.checkForInput()

        screen.fill((201, 228, 195))
        button.update()
        button2.update()
        pygame.display.update()