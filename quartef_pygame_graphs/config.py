


LABEL_OFFSET = 14       #the distance betwen 2 labels

TOP_BORDER_SIZE = 16        #the size of the border around the graph
RIGHT_BORDER_SIZE = 16        #the size of the border around the graph
BOTTOM_BORDER_SIZE = 16        #the size of the border around the graph
LEFT_BORDER_SIZE = 32        #the size of the border around the graph

TOP_AXIS_NUMBER_PADDING = 8 #the space betwen the numbers from the axis to the axis itself
LEFT_AXIS_NUMBER_PADDING = 12


MAGNITUDE_LIMIT = 2
"""
Controls when the grid step changes magnitude.

Example:

largest value = 740
740 / 100 = 7.4 > 2
→ step = 100

largest value = 190
190 / 100 = 1.9 < 2
→ step = 10
"""