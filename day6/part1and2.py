class Coordinate:
    def __init__(coordinate, string):
        coordinate.x = string[:string.find(',')].strip()
        coordinate.y = string[string.find(',') + 1:].strip()


#import the list of guard events from the file
input_file = open('input.txt', 'r')
location = input_file.readlines()

#create lists for x_coordinates, y_coordinates, and area of each coordinate
x_coordinate = [0 for index in range(len(location))]
y_coordinate = [0 for index in range(len(location))]
area         = [0 for index in range(len(location))]

#extract x and y coordinates from the list of locations
for index in range(len(location)):
    temp = location[index]
    x_coordinate[index] = int(temp[:temp.find(',')].strip())
    y_coordinate[index] = int(temp[temp.find(',') + 1:].strip())

#make a grid 1 frame bigger than the max x and y coordinates 
grid = [[0 for y in range(max(y_coordinate) + 1)] for x in range(max(x_coordinate) + 1)]
grid2 = [[False for y in range(max(y_coordinate) + 1)] for x in range(max(x_coordinate) + 1)]


#go trhough all x and y coordinates and calculate the closest location
for x in range(len(grid)):
    #calculate the distance from the x coordinates
    x_distance = [abs(x_loc - x) for x_loc in x_coordinate]
    
    for y in range(len(grid[0])):

        #calculate the distance from the y coordinate
        y_distance = [abs(y_loc - y) for y_loc in y_coordinate]

        #sum the x and y distances to find total distance
        distance = [(x_distance[a] + y_distance[a]) for a in range(len(x_distance))]

        #find the shortest distance
        shortest_distance = min(distance)

        #part1 calculation
        #if there are two points equidistant, mark as '.'
        #otherwise mark it with the closest coordinate number
        if distance.count(shortest_distance) != 1:
            grid[x][y] = '.'
        else:
            grid[x][y] = distance.index(shortest_distance)

        #part2 calcualtion
        #determine if the parameter is within 10000 distance from all points
        if (sum(distance) < 10000):
            grid2[x][y] = True

#determine the area of each coordinate entry
for index in range(len(x_coordinate)):

    #count how many instances there are in the grid
    area[index] = sum(row.count(index) for row in grid)

    #check if the coordinate is closest to one of the edges of the grid
    #any areas that are closest to an edge are infinite
    for x in range(len(grid)):
        if ((grid[x][0] == index) or ((grid[x][len(grid[0]) - 1]) == index)):
            #area to be ignored if it is infinite
            area[index] = 0
    for y in range(len(grid[0])):
        if ((grid[0][y] == index) or (grid[len(grid) - 1][y] == index)):
            #area to be ignored if it is infinite
            area[index] = 0

#determine the maximum finite area and which coordinate it was (part1)    
print(f'The maximum finite area is {max(area)} which is coordinate #{area.index(max(area))}')


#find the area that is within 1000 distance
safe_area = 0
for row in grid2:
    safe_area += row.count(True)

#print out the area that is within 10000 distance from all coordinates (part2)
print(f'The size of the region that is within 10000 distance from all locations is {safe_area}')

      
