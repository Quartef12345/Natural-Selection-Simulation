



def raw_data(self, data):
    x_data = data[self.x_name] #the data for the x axis, retrieved from the universal data dictionaiy, and uses the x axis name of the graph as key for the dictionary

    y_data_array = [] #the set of the diferent y datas, each elemnt is a diferent metric
    for y_name in self.y_name_array:
        y_data_array.append(data[y_name])

    mixed_y_data = [] #every raw number mixed in one array
    for y_data in y_data_array:
        for point in y_data:
            mixed_y_data.append(point)

    self.bigger_y = max(mixed_y_data)    #the biggest of all of the metrics, used to set the referencial on the graph
    self.bigger_x = max(x_data)          #the biggest of all of x data, used to set the referencial on the graph

    data_points_array = []          #the set of all of the points to be drawn on the graph, each element is an array of points, each element is a diferent metric

    for metric in y_data_array:
        data_points = []
        for i in range(len(x_data)):
            if len(metric) > i:
                data_points.append((x_data[i], metric[i])) #a single point, on one of the metrics
        data_points_array.append(data_points) #adds the data points of this metric to the data points array

    return data_points_array


def process_raw_data(self, data_array):

    processsed_points_array = []

    for data_set in data_array:
        beggining_point = [data_set[0][0],data_set[0][1]]

        processsed_points_set = []
        processsed_points_set.append(beggining_point)

        for nr in range(len(data_set)):
            data_point = data_set[nr]
            if data_point[1] != beggining_point[1]:
                new_point_1 = [data_set[nr - 1][0], beggining_point[1]]
                new_point_2 = [data_point[0], data_point[1]]
                processsed_points_set.append(new_point_1)
                processsed_points_set.append(new_point_2)
                beggining_point = new_point_2

        processsed_points_set.append(data_set[-1])

        processsed_points_array.append(processsed_points_set)

    return processsed_points_array