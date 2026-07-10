import pygame

axis_font = pygame.font.Font('freesansbold.ttf', 11)



class Graph:
    def __init__(self, surface, position, x_name, y_name):
        self.surface = surface
        self.position = position
        self.x_name = x_name
        self.y_name = y_name
        self.axis_offset = 14

        self.active = False


    def draw(self):
        surface = self.surface
        position = self.position 
        x_name = self.x_name
        y_name = self.y_name
        axis_offset = self.axis_offset

        if self.active:

            pygame.draw.rect(surface, "#FFFFFF", (position[0], position[1], position[2], position[3])) #Background

            pygame.draw.line(surface, "#000000", (position[0] + axis_offset, position[1] + position[3] - axis_offset), (position[0] + position[2],  position[1] + position[3] - axis_offset)) # X Axis
            pygame.draw.line(surface, "#000000", (position[0] + axis_offset, position[1]), (position[0] + axis_offset,  position[1] + position[3] - axis_offset)) # Y Axis

            x_aixs_text = axis_font.render(f"{x_name}", True, "#000000")
            x_axis_surface = x_aixs_text.get_rect()
            x_axis_surface.bottomright = (position[0] + position[2], position[1] + position[3])
            surface.blit(x_aixs_text, x_axis_surface)

            y_axis_text_horizontal = axis_font.render(f"{y_name}", True, "#000000")
            y_axis_text = pygame.transform.rotate(y_axis_text_horizontal, 90)
            y_axis_surface = y_axis_text.get_rect()
            y_axis_surface.topleft = (position[0] + 2, position[1])
            surface.blit(y_axis_text, y_axis_surface)
    
    def show(self):
        self.active = True
    def hide(self):
        self.active = False
        

