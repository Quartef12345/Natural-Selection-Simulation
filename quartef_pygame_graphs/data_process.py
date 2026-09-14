



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


def process_raw_data(data_array): 
# Removes repeated points,
# for example, if population is 130 for 5 seconds,
# the data doesnt have 300 consecutive points of the same value(assuming 60 fps),
#  instead it has a beginning point, and the end point of the value chain

    processsed_points_array = []

    for data_set in data_array: #For each metric
        beggining_point = [data_set[0][0],data_set[0][1]]   #The first point of the data, its mandatory to have it

        processsed_points_set = []
        processsed_points_set.append(beggining_point)

        for nr in range(len(data_set)):
            data_point = data_set[nr]
            if data_point[1] != beggining_point[1]: #If the value chain is broken

                new_point_1 = [data_set[nr - 1][0], beggining_point[1]] #The new data point being added has a abscissa of the point exaclty before the change, and the y value of the chain
                new_point_2 = [data_point[0], data_point[1]] #Is the new point for the new chain
                processsed_points_set.append(new_point_1)#Adds the points to the data
                processsed_points_set.append(new_point_2)
                beggining_point = new_point_2   #Sets the new beggining point for the new chain

        processsed_points_set.append(data_set[-1]) #Adds the last point of the set, its mandatory and it cant be detected by the previous segment of code, because it doesnt have a next to be diferent

        processsed_points_array.append(processsed_points_set) #adds the new data set, to the metrics array

    return processsed_points_array

def compress_points_data(data, density, compression_method = "index_jump"):   #Density = Maximum ammount of visible points

    #   Planned methods:
    #   - Average Value, displays the average of all values withing jump_distance

    compressed_data = [] #The final result


    if compression_method == "index_jump":  
        for metric in data:     # Repeats the compression method for each metric
            compressed_metric_set = []  #The sub final result
            total_points = len(metric)

            if total_points <= density:         #If there are less points than density, skips the compression at all
                compressed_metric_set = metric
            else:
                jump_distance = int(total_points/density)   #The ammount of points you jump over
                for n in range(0, len(metric), jump_distance):        #Goes trough each point in the metric
                    compressed_metric_set.append(metric[n]) #Adds them to the sub final result
            compressed_data.append(compressed_metric_set)   #Adds the sub final result to the final result


    elif compression_method == "x_axis_value_jump":
        for metric in data:     # Repeats the compression method for each metric
            compressed_metric_set = []  #The sub final result
            max_x_value = metric[-1][0]
            total_points = len(metric)

            if total_points <= density:         #If there are less points than density
                compressed_metric_set = metric
            else:
                jump_distance = max_x_value/density   #The ammount of points you jump over
                compressed_metric_set.append(metric[0])
                last_point_x = metric[0][0]
                for n in range(len(metric)):
                    if metric[n][0] - last_point_x >= jump_distance:
                        compressed_metric_set.append(metric[n])
                        last_point_x = metric[n][0]
                if compressed_metric_set[-1] != metric[-1]:
                    compressed_metric_set.append(metric[-1])
            compressed_data.append(compressed_metric_set)   #Adds the sub final result to the final result
    else:
        print("Invalid Compression Method")
        quit()

    return compressed_data


def compress_data(data, density, compression_method = "x_axis_value_jump"):   #Density = Maximum ammount of visible points

    #   Planned methods:
    #   - Average Value, displays the average of all values withing jump_distance

    compressed_data = {} #The final result

    if compression_method == "index_jump":  
        for metric, values in data.items():     # Repeats the compression method for each metric
            compressed_values = []  #The sub final result
            total_data = len(values)

            if total_data <= density:         #If there are less points than density, skips the compression at all
                compressed_values = values
            else:
                jump_distance = int(total_points/density)   #The ammount of points you jump over
                for n in range(len(values)):        #Goes trough each point in the metric
                    if n % jump_distance == 0:      #Checks the eligible ones
                        compressed_values.append(values[n]) #Adds them to the sub final result
            compressed_data[metric] = compressed_values    #Adds the sub final result to the final result


    if compression_method == "value_jump":
        for metric, values in data.items():     # Repeats the compression method for each metric
            compressed_values = []  #The sub final result
            max_value = values[-1]
            total_points = len(values)

            if total_points <= density:         #If there are less points than density
                compressed_values = values
            else:
                jump_distance = max_value/density   #The ammount you jump over
                compressed_values.append(values[0])
                last_point = values[0]
                for n in range(len(values)):
                    if values[n] - last_point >= jump_distance:
                        compressed_values.append(values[n])
                        last_point = values[n]
                if compressed_values[-1] != values[-1]:
                    compressed_values.append(values[-1])
            compressed_data[metric] = compressed_values   #Adds the sub final result to the final result
    else:
        print("Invalid Compression Method")
        quit()

    return compressed_data

def formatting_data(data, labels):
    data_dic = {}

    x_array = []
    x_formated = False

    for n in range(len(data)):
        metric = data[n]
        metric_array = []
        for point in metric:
            metric_array.append(point[1])
            if not x_formated:
                x_array.append(point[0])
        x_formated = True
        if n+1 < len(labels):
            data_dic[labels[n+1]] = metric_array
    data_dic[labels[0]] = x_array


    return data_dic