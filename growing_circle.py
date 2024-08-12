import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill("white")
pygame.display.update()

class Circle():
    def __init__(self, color, pos, radius, width):
        self.circle_color = color
        self.circle_pos = pos
        self.circle_radius = radius
        self.circle_width = width
        self.circle_surf = screen
    def draw(self):
        self.Draw_Circle = pygame.draw.circle(self.circle_surf, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)
    def grow(self, r):
        self.circle_radius = self.circle_radius + r
        self.Draw_Circle = pygame.draw.circle(self.circle_surf, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)
c = Circle("green", (300,300), 25, 0)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            c.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill("white")
            c.grow(20)
            pygame.display.update()
        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            c2 = Circle("red", pos, 5, 0)
            c2.draw()
            pygame.display.update()
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()