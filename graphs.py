import pygame
import math

axis_font = pygame.font.Font('freesansbold.ttf', 11)
graph_array = []

data = {
    "Ticks": [1],
    "Population": [0]
}

def adjust_color(hex_color, factor=0.2):
    hex_color = hex_color.lstrip('#')
    
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    if factor >= 0:
        # Darken (approach 0)
        r = max(0, int(r * (1 - factor)))
        g = max(0, int(g * (1 - factor)))
        b = max(0, int(b * (1 - factor)))
    else:
        # Lighten (approach 255) using positive target factor
        abs_factor = abs(factor)
        r = min(255, int(r + (255 - r) * abs_factor))
        g = min(255, int(g + (255 - g) * abs_factor))
        b = min(255, int(b + (255 - b) * abs_factor))
    
    return f"#{r:02X}{g:02X}{b:02X}"

def update_graphs():
    for graph in graph_array:
        if graph.auto_update:
            graph.update_data(data)
        if graph.active:
            graph.draw()


class Graph:
    def __init__(self, surface, position, x_name, y_name_array, color_array):
        self.surface = surface
        self.position = position
        self.axis_offset = 8
        self.grid_position = [self.position[0] + self.axis_offset, self.position[1] + self.axis_offset, self.position[2] - 2*self.axis_offset, self.position[3] - 2*self.axis_offset ]
        self.x_name = x_name
        self.y_name_array = y_name_array
        self.nr_of_variables = len(y_name_array)
        self.color_array = color_array
        self.label_offset = 14

        self.active = False
        self.auto_update = True
        self.auto_scroll = True

        self.data_points_array = []
        self.bigger_x = 0
        self.bigger_y = 0

        graph_array.append(self)

    def draw(self):
        surface = self.surface
        position = self.position
        grid_position = self.grid_position
        x_name = self.x_name
        y_name = self.y_name_array
        label_offset = self.label_offset
        color_array = self.color_array

        if self.active:
            pygame.draw.rect(surface, adjust_color(color_array[0], 0.4), (position[0], position[1], position[2], position[3]))
            pygame.draw.rect(surface, color_array[0], (grid_position[0], grid_position[1], grid_position[2], grid_position[3])) #Background

            pygame.draw.line(surface, color_array[1], (grid_position[0], grid_position[1] + grid_position[3] ), (grid_position[0] + grid_position[2],  grid_position[1] + grid_position[3] )) # X Axis
            pygame.draw.line(surface, color_array[1], (grid_position[0] , grid_position[1]), (grid_position[0],  grid_position[1] + grid_position[3])) # Y Axis

            self.draw_grid()

            x_aixs_text = axis_font.render(f"{x_name}", True, color_array[1])
            x_axis_surface = x_aixs_text.get_rect()
            x_axis_surface.bottomright = (grid_position[0] + grid_position[2], grid_position[1] + grid_position[3])
            surface.blit(x_aixs_text, x_axis_surface) #the caption for the x axis

            for i in range(self.nr_of_variables):

                y_axis_text = axis_font.render(f"{y_name[i]}", True, color_array[1])
                y_axis_surface = y_axis_text.get_rect()
                y_axis_surface.bottomright = (grid_position[0] + grid_position[2] - label_offset, grid_position[1] + grid_position[3] - label_offset * (1 + i) - 2)
                surface.blit(y_axis_text, y_axis_surface) #the caption for the current metric

                square_label_size = y_axis_surface.height   #a professionaly looking square to serve has a colored label
                pygame.draw.rect(surface, adjust_color(color_array[2+i], 0.5), (y_axis_surface.x - square_label_size - 3, y_axis_surface.y, square_label_size, square_label_size))
                pygame.draw.rect(surface, color_array[2+i], (y_axis_surface.x - square_label_size - 3 + square_label_size*0.1, y_axis_surface.y + square_label_size*0.1, square_label_size*0.8, square_label_size*0.8))

    def update_data(self, data):

        x_data = data[self.x_name] #the data for the x axis, retrieved from the universal data dictionaiy, and uses the x axis name of the graph as key for the dictionary

        y_data_array = [] #the set of the diferent y datas, each elemnt is a diferent metric
        for y_name in self.y_name_array:
            y_data_array.append(data[y_name])

        mixed_y_data = [] #every raw number mixed in one array
        for y_data in y_data_array:
            for data in y_data:
                mixed_y_data.append(data)

        self.bigger_y = max(mixed_y_data)    #the biggest of all of the metrics, used to set the referencial on the graph
        self.bigger_x = max(x_data)          #the biggest of all of x data, used to set the referencial on the graph

        data_points_array = []          #the set of all of the points to be drawn on the graph, each element is an array of points, each element is a diferent metric

        for metric in y_data_array:
            data_points = []
            for i in range(len(x_data)):
                if len(metric) > i:
                    data_points.append((x_data[i], metric[i])) #a single point, on one of the metrics
            data_points_array.append(data_points) #adds the data points of this metric to the data points array
        
        self.data_points_array = data_points_array

    def draw_grid(self):
            base_x = self.grid_position[0]    #base grid_position of the graph
            base_y = self.grid_position[1] + self.grid_position[3]

            bigger_x = self.bigger_x
            bigger_y = self.bigger_y
          
            usable_width = self.grid_position[2]
            usable_heigth = self.grid_position[3]

            if bigger_x <= 0:
                bigger_x = 1
            exponent = math.floor(math.log10(bigger_x))
            x_axis_magnitude = 10 ** exponent   #the closest number of base 10, used to set the referencial
            
            # If the magnitude is too large for the step scale (e.g. 1000 for 2500), lower it by one order
            if bigger_x / x_axis_magnitude < 3.5 and x_axis_magnitude >= 10:
                grid_step_x = x_axis_magnitude // 10
            else:
                grid_step_x = x_axis_magnitude
            
            pixel_per_unit_x = usable_width / bigger_x

            virtual_step = grid_step_x//10  #a "fake" step, one magnitude lower than the real step, used to draw the auiliar lines
            if virtual_step <= 0: #for example, if magnitude is 100, then the virtual step is 10, each real step will be divided into 10 virtual steps
                virtual_step = 1
            for grid_value in range(virtual_step, int(bigger_x) + 1, virtual_step):
                grid_pixel_x = base_x + (grid_value * pixel_per_unit_x)
                if grid_value%grid_step_x == 0:
                    pygame.draw.line(self.surface, adjust_color(self.color_array[1], -0.2), (grid_pixel_x, base_y), (grid_pixel_x, self.grid_position[1]))
                else:
                    pygame.draw.line(self.surface, adjust_color(self.color_array[1], -0.8), (grid_pixel_x, base_y), (grid_pixel_x, self.grid_position[1]))



            if bigger_y <= 0:
                bigger_y = 1
            exponent = math.floor(math.log10(bigger_y))
            y_axis_magnitude = 10 ** exponent   #the closest number of base 10, used to set the referencial

            max_y = int(y_axis_magnitude * ((bigger_y + y_axis_magnitude)//y_axis_magnitude))
            if max_y <= 0:
                max_y = 1
            # If the magnitude is too large for the step scale (e.g. 1000 for 2500), lower it by one order
            if bigger_y / y_axis_magnitude < 3.5 and y_axis_magnitude >= 10:
                grid_step_y = y_axis_magnitude // 10
            else:
                grid_step_y = y_axis_magnitude
            
            pixel_per_unit_y = usable_heigth / max_y

            virtual_step = grid_step_y//10  #a "fake" step, one magnitude lower than the real step, used to draw the auiliar lines
            if virtual_step <= 0: #for example, if magnitude is 100, then the virtual step is 10, each real step will be divided into 10 virtual steps
                virtual_step = 1
            for grid_value in range(virtual_step, max_y, virtual_step):
                grid_pixel_y = base_y - (grid_value * pixel_per_unit_y)
                if grid_value%grid_step_y == 0:
                    pygame.draw.line(self.surface, adjust_color(self.color_array[1], -0.2), (base_x, grid_pixel_y), (base_x + self.grid_position[2], grid_pixel_y))
                else:
                    pygame.draw.line(self.surface, adjust_color(self.color_array[1], -0.8), (base_x, grid_pixel_y), (base_x + self.grid_position[2], grid_pixel_y))    








        

