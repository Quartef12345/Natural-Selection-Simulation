import pygame
import math
from . import config
from .utils import adjust_color, format_number, render_text
from .data_process import raw_data, process_raw_data

axis_font = pygame.font.Font('freesansbold.ttf', 11)
graph_array = []



def update_graphs(data):
    for graph in graph_array:
        if graph.auto_update:
            graph.update_data(data)
        if graph.active:
            graph.draw()


class Graph:
    def __init__(self, surface, position, x_name, y_name_array, color_array, config_settings = None):
        self.surface = surface
        self.position = position


        if config_settings != None and config_settings["LEFT_BORDER_SIZE"] != None:
            self.left_border_size = config_settings["LEFT_BORDER_SIZE"]
        else:
            self.left_border_size = config.LEFT_BORDER_SIZE

        if config_settings != None and config_settings["TOP_BORDER_SIZE"] != None:
            self.top_border_size = config_settings["TOP_BORDER_SIZE"]
        else:
            self.top_border_size = config.TOP_BORDER_SIZE


        if config_settings != None and config_settings["RIGHT_BORDER_SIZE"] != None:
            self.right_border_size = config_settings["RIGHT_BORDER_SIZE"]
        else:
            self.right_border_size = config.RIGHT_BORDER_SIZE


        if config_settings != None and config_settings["BOTTOM_BORDER_SIZE"] != None:
            self.bottom_border_size = config_settings["BOTTOM_BORDER_SIZE"]
        else:
            self.bottom_border_size = config.BOTTOM_BORDER_SIZE


        self.grid_position = [self.position[0] + self.left_border_size, self.position[1] + self.top_border_size, self.position[2] - self.left_border_size - self.right_border_size, self.position[3] - self.top_border_size - self.bottom_border_size ]
        self.x_name = x_name
        self.y_name_array = y_name_array
        self.nr_of_variables = len(y_name_array)
        self.color_array = color_array

        if config_settings != None and config_settings["LABEL_OFFSET"] != None:
            self.label_offset = config_settings["LABEL_OFFSET"]
        else:
            self.label_offset = config.LABEL_OFFSET

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
            pygame.draw.rect(surface, adjust_color(color_array[0], 0.1), (position[0], position[1], position[2], position[3]))
            pygame.draw.rect(surface, color_array[0], (grid_position[0], grid_position[1], grid_position[2], grid_position[3])) #Background

            self.draw_grid()

            pygame.draw.line(surface, color_array[1], (grid_position[0], grid_position[1] + grid_position[3] ), (grid_position[0] + grid_position[2],  grid_position[1] + grid_position[3] )) # X Axis
            pygame.draw.line(surface, color_array[1], (grid_position[0] , grid_position[1]), (grid_position[0],  grid_position[1] + grid_position[3])) # Y Axis


            #the caption for the x axis
            render_text(axis_font, f"{x_name}", color_array[1], grid_position[0] + grid_position[2], grid_position[1] + grid_position[3], surface)

            for i in range(self.nr_of_variables):

                y_axis_text = axis_font.render(f"{y_name[i]}", True, color_array[1])
                y_axis_surface = y_axis_text.get_rect()
                y_axis_surface.bottomright = (grid_position[0] + grid_position[2] - label_offset, grid_position[1] + label_offset * (1 + i))
                surface.blit(y_axis_text, y_axis_surface) #the caption for the current metric

                square_label_size = y_axis_surface.height   #a professionaly looking square to serve has a colored label
                pygame.draw.rect(surface, adjust_color(color_array[2+i], 0.5), (y_axis_surface.x - square_label_size - 3, y_axis_surface.y, square_label_size, square_label_size))
                pygame.draw.rect(surface, color_array[2+i], (y_axis_surface.x - square_label_size - 3 + square_label_size*0.1, y_axis_surface.y + square_label_size*0.1, square_label_size*0.8, square_label_size*0.8))

            self.draw_data()

    def update_data(self, data):

        raw_points_array = raw_data(self, data)

        data_points_array = process_raw_data(self, raw_points_array)
        
        self.data_points_array = data_points_array

    def calculate_grid(self, biggest_value, usable_distance):

        exponent = math.floor(math.log10(biggest_value))
        axis_magnitude = 10 ** exponent   #the closest number of base 10, used to set the referencial
        
        # If the magnitude is too large for the step scale (e.g. 1000 for 2500), lower it by one order
        if biggest_value / axis_magnitude < config.MAGNITUDE_LIMIT and axis_magnitude >= 10:
            grid_step = axis_magnitude // 10
        else:
            grid_step = axis_magnitude
        
        pixel_per_unit = usable_distance / biggest_value

        virtual_step = grid_step//10  #a "fake" step, one magnitude lower than the real step, used to draw the auiliar lines
        if virtual_step <= 0: #for example, if magnitude is 100, then the virtual step is 10, each real step will be divided into 10 virtual steps
            virtual_step = 1
        return grid_step, virtual_step, pixel_per_unit

    def draw_grid(self):
        color_array = self.color_array

        base_x = self.grid_position[0]    #base grid_position of the graph
        base_y = self.grid_position[1] + self.grid_position[3]
        origin_y = self.grid_position[1]

        width = self.grid_position[2]
        height = self.grid_position[3]

        bigger_x = self.bigger_x
        bigger_y = self.bigger_y

        if bigger_x <= 0:
            bigger_x = 1

        if bigger_y <= 0:
            bigger_y = 1

        #Values to draw the x grid-lines
        x_grid_values = self.calculate_grid(bigger_x, width)

        #values to draw the y grid-lines
        exponent = math.floor(math.log10(bigger_y))
        y_axis_magnitude = 10 ** exponent   #the closest number of base 10, used to set the referencial

        max_y = int(y_axis_magnitude * ((bigger_y + y_axis_magnitude)//y_axis_magnitude)) #the biggest value the graph shows - not necesserly included in the data set
        if max_y <= 0:
            max_y = 1

        y_grid_values = self.calculate_grid(max_y, height)



        #sub x grid-lines
        for grid_value in range(x_grid_values[1], int(bigger_x) + 1, x_grid_values[1]):
            grid_pixel_x = base_x + (grid_value * x_grid_values[2])
            if grid_value % x_grid_values[0] != 0:
                pygame.draw.line(self.surface, adjust_color(color_array[1], -0.8), (grid_pixel_x, base_y), (grid_pixel_x, origin_y))

        # y grid-lines
        for grid_value in range(y_grid_values[1], max_y + 1, y_grid_values[1]):
            grid_pixel_y = base_y - (grid_value * y_grid_values[2])
            if grid_value % y_grid_values[0] == 0:
                pygame.draw.line(self.surface, adjust_color(color_array[1], -0.2), (base_x, grid_pixel_y), (base_x + width, grid_pixel_y))
                render_text(axis_font, f"{format_number(grid_value)}", color_array[1], base_x - config.LEFT_AXIS_NUMBER_PADDING, grid_pixel_y, self.surface)
            else:
                pygame.draw.line(self.surface, adjust_color(color_array[1], -0.8), (base_x, grid_pixel_y), (base_x + width, grid_pixel_y))    


        #redraws the main x-grid because the sub y-grid was being drawn on top of the main x-grid
        for grid_value in range(x_grid_values[1], int(bigger_x) + 1, x_grid_values[1]):
            grid_pixel_x = base_x + (grid_value * x_grid_values[2])
            if grid_value % x_grid_values[0] == 0:
                pygame.draw.line(self.surface, adjust_color(color_array[1], -0.2), (grid_pixel_x, base_y), (grid_pixel_x, origin_y))
                render_text(axis_font, f"{format_number(grid_value)}", color_array[1], grid_pixel_x, origin_y + height + config.TOP_AXIS_NUMBER_PADDING, self.surface)

        grid_value = bigger_x                       #the last line is a one of a kind, because is not in the magnitude of the steps, so it needs to be drawn seperatly
        grid_pixel_x = base_x + (grid_value * x_grid_values[2])
        pygame.draw.line(self.surface, adjust_color(color_array[1], -0.2), (grid_pixel_x, base_y), (grid_pixel_x, origin_y))
        
        render_text(axis_font, f"{grid_value:.1f}", color_array[1], grid_pixel_x, origin_y + height + config.TOP_AXIS_NUMBER_PADDING, self.surface)


    def draw_data(self):
        data_points_array = self.data_points_array

        graph_origin_x = self.grid_position[0]
        graph_origin_y = self.grid_position[1] + self.grid_position[3]

        bigger_y = self.bigger_y

        exponent = math.floor(math.log10(bigger_y))
        y_axis_magnitude = 10 ** exponent   #the closest number of base 10, used to set the referencial

        max_y = int(y_axis_magnitude * ((bigger_y + y_axis_magnitude)//y_axis_magnitude)) #the biggest value the graph shows - not necesserly included in the data set
        if max_y <= 0:
            max_y = 1

        pixel_per_unit_x = self.calculate_grid(self.bigger_x, self.grid_position[2])[2]
        pixel_per_unit_y = self.calculate_grid(max_y, self.grid_position[3])[2]

        for data_set in data_points_array:
            for i in range(len(data_set)):
                point_x_2 = data_set[i][0]
                point_y_2 = data_set[i][1]

                if i <= 0:
                    continue
                
                point_x_1 = data_set[i - 1][0]
                point_y_1 = data_set[i - 1][1]

                coordinates_x_2 = pixel_per_unit_x * point_x_2 + graph_origin_x
                coordinates_y_2 = graph_origin_y - pixel_per_unit_y * point_y_2 

                coordinates_x_1 = pixel_per_unit_x * point_x_1 + graph_origin_x
                coordinates_y_1 = graph_origin_y - pixel_per_unit_y * point_y_1

                pygame.draw.line(self.surface, self.color_array[2 + data_points_array.index(data_set)], (coordinates_x_1, coordinates_y_1), (coordinates_x_2, coordinates_y_2))
