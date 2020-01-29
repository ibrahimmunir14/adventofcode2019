import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Matrix:
    def __init__(self, minX, maxX, minY, maxY):
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        self.grid = [[0]*(maxY-minY+1) for i in range(maxX-minX+1)]
        
    def print(self):
        for y in range(len(self.grid[0])-1, -1, -1):
            for x in range(len(self.grid)):
                print("*" if self.grid[x][y] else " ", end='')
            print()

    def get(self, point):
        return self.grid[point.x - self.minX][point.y - self.minY]

    def put(self, point, val):
        self.grid[point.x - self.minX][point.y - self.minY] = val



def main():
    f = open("input3.txt", "r")
    both = f.read().split("\n")[:-1]
    #both = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
    #        "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"] #410
    #both = ["R75,D30,R83,U83,L12,D49,R71,U7,L72",
    #        "U62,R66,U55,R34,D71,R55,D58,R83"] #610
    path_one = both[0].split(",")
    path_two = both[1].split(",")
    
    mat_one = get_matrix_from_path(path_one)
    print("mat_one calculated.")
    mat_two = get_matrix_from_path(path_two)
    print("mat_two calculated.")
    intersections = get_intersections(mat_one, mat_two)
    print("intersections calculated.")
    ans = dist_to_smallest_intersection(intersections, mat_one, mat_two)
    print("Distance to nearest intersection: " + str(ans))

def get_intersections(mat_one, mat_two):
    intersects = []
    minX = max(mat_one.minX, mat_two.minX)
    maxX = min(mat_one.maxX, mat_two.maxX)
    minY = max(mat_one.minY, mat_two.minY)
    maxY = min(mat_one.maxY, mat_two.maxY)
    for x in range(minX, maxX+1):
        for y in range(minY, maxY+1):
            point = Point(x, y)
            if (mat_one.get(point) and mat_two.get(point)):
                intersects.append(point)
        print(x - minX, "/", maxX+1-minX)
    return intersects

def dist_to_smallest_intersection(intersections, mat_one, mat_two):
    shortest_dist = sys.maxsize
    for point in intersections:
        dist = mat_one.get(point) + mat_two.get(point)
        shortest_dist = min(shortest_dist, dist)
    return shortest_dist
    
def get_matrix_from_path(path):
    cells = []
    (minX, maxX, minY, maxY) = (0,0,0,0)
    pos = Point(0,0)
    steps = 0
    for command in path:
        direction = command[0]
        movements = int(command[1:])
        for move in range(movements):
            pos = make_move(pos, direction)
            steps += 1
            cells.append((pos, steps))
        maxX = max(pos.x,maxX)
        maxY = max(pos.y,maxY)
        minX = min(pos.x,minX)
        minY = min(pos.y,minY)
                
    matrix = Matrix(minX, maxX, minY, maxY)
    for cell in cells:
        (pos, steps) = cell
        matrix.put(pos, steps)
    return matrix

def make_move(pos, direction):
    if (direction == "R"):
        return Point(pos.x+1, pos.y)
    elif (direction == "L"):
        return Point(pos.x-1, pos.y)
    elif (direction == "U"):
        return Point(pos.x, pos.y+1)
    elif (direction == "D"):
        return Point(pos.x, pos.y-1)
    else:
        print("ERROR")
        return "ERROR"


main()
