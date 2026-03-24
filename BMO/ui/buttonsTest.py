import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Button!")
#fonts can only be stretched to sizes they are multiples of. Grand9k is 8 px, so 40, 48, 56, etc. Minecraft is 16 px, so 32, 48, 64, etc.
main_font = pygame.font.Font("BMO-Companion-Project/BMO/Graphics/Grand9K_Pixel.ttf", 40) #use custom font
button_surface = pygame.image.load("BMO-Companion-Project/BMO/Graphics/buttonTemplate2.png").convert_alpha()
button_surface = pygame.transform.scale(button_surface, (250, 50))

class Button():
	def __init__(self, image, x_pos, y_pos, text_input, paddingColor, borderColor, altBorderColor):
		self.image = image
		#positioning
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, (0, 0, 0)) #black
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
		#layers
		self.middlePadding = 6
		self.borderPadding = 12
		self.paddingColor = paddingColor
		self.borderColor = borderColor
		self.altBorderColor = altBorderColor

	def update(self):
		borderRect = self.rect.inflate(self.borderPadding*2-3, self.borderPadding*2)
		paddingRect = self.rect.inflate(self.middlePadding*2-3, self.middlePadding*2-2)
		
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			pygame.draw.rect(screen, self.altBorderColor, borderRect) #altBorderColor
			pygame.draw.rect(screen, self.paddingColor, paddingRect)
			
		else:
			pygame.draw.rect(screen, self.borderColor, borderRect) #borderColor
			pygame.draw.rect(screen, self.paddingColor, paddingRect) 
		
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if self.rect.collidepoint(position):
			print("Button Press!")
			#try to move the position of the button when it's clicked, just to see if I can do it.
			self.x_pos += 20
			self.y_pos += 20
			self.rect.center = (self.x_pos, self.y_pos)
			self.text_rect.center = self.rect.center
			button.text_rect.center = button.rect.center #keep text centered on button



	def changeColor(self, position):
		if self.rect.collidepoint(position):
			self.text = main_font.render(self.text_input, True, (255, 179, 47)) #golden orange
		else:
			self.text = main_font.render(self.text_input, True, (0, 0, 0)) #black



button = Button(button_surface, 400, 290, "Button", (240, 235, 210), (0, 0, 0), (255, 179, 47)) #white, black, alt golden orange
button2 = Button(button_surface, 400, 90, "Play Games", (240, 235, 210), (0, 0, 0), (255, 179, 47))
button3 = Button(button_surface, 400, 190, "Settings", (240, 235, 210), (0, 0, 0), (255, 179, 47))
button4 = Button(button_surface, 400, 390, "Exit", (240, 235, 210), (0, 0, 0), (255, 179, 47))
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			button.checkForInput(pygame.mouse.get_pos())

	

	screen.fill((201, 228, 195)) #faceColor2

	button.update()
	button2.update()
	button3.update()
	button4.update()
	button.changeColor(pygame.mouse.get_pos())

	pygame.display.update()