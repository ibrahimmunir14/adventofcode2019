from sys import maxsize
from math import atan2, pi

class Asteroid_Map():
    def __init__(self, str_map):
        str_rows = str_map.split("\n")[:-1]
        self.height = len(str_rows)
        self.width = len(str_rows[0])
        self.grid = [[None for j in range(self.height)] for i in range(self.width)]
        self.asteroids = []
        self.visibility_grid = [[None for j in range(self.height)] for i in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y] = int(str_rows[y][x] == '#')
                if (str_rows[y][x] == '#'): self.asteroids.append((x, y))

    def print(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                print("{:>2}".format(grid[x][y]), end='')
            print()

    def __count_visible_asteroids(self, start):
        visible_set = {bearing(start, end) for end in self.asteroids if not start == end}
        return len(visible_set)

    def make_visibility_grid(self):
        for y in range(self.height):
            for x in range(self.width):
                start = (x, y)
                count = self.__count_visible_asteroids(start)
                if start not in self.asteroids: count = '.'
                self.visibility_grid[x][y] = count

    def vaporisation_order(self, start):
        # asteroids[a] = list of asteroids at angle a from start
        asteroids = dict()
        for end in self.asteroids:
            ang = bearing(start, end)
            if ang not in asteroids:
                asteroids[ang] = []
            asteroids[ang].append(end)
            asteroids[ang] = sorted(asteroids[ang], key=lambda a: dist(start, a))
        # sorted_asteroids = list of asteroids in order of vaporisation
        sorted_asteroids = []
        while len(asteroids) > 0:
            for ang in sorted(asteroids):
                sorted_asteroids.append(asteroids[ang].pop(0))
                if len(asteroids[ang]) == 0: asteroids.pop(ang)
        return sorted_asteroids

def main():
    f = open("input10.txt", "r")
    str_map = f.read()
    ast_map = Asteroid_Map(str_map)

    # Part One
    print("---------------------------------------------\nPart One")
    print("---------------------------------------------")
    ast_map.make_visibility_grid()
    (station_x, station_y, count) = best_visibility(ast_map)
    station = (station_x, station_y)
    print
    print("Best visibility at (" + str(station_x) + ", " + str(station_y) + ").")
    print(count, "asteroids visible.")
    print("---------------------------------------------\n\n")

    # Part Two
    print("---------------------------------------------\nPart Two")
    print("---------------------------------------------")
    vap_order = ast_map.vaporisation_order(station)
    print("Vaporisations:")
    print("   1st:", vap_order[1-1])
    print("   2nd:", vap_order[2-1])
    print("   3rd:", vap_order[3-1])
    print("  10th:", vap_order[10-1])
    print("  20th:", vap_order[20-1])
    print("  50th:", vap_order[50-1])
    print(" 100th:", vap_order[100-1])
    print(" 199th:", vap_order[199-1])
    print(" 200th:", vap_order[200-1])
    print(" 201th:", vap_order[201-1])
    print(" 299th:", vap_order[299-1])
    print()
    (x, y) = vap_order[200-1]
    print("Answer:", 100 * x + y)
    print("---------------------------------------------")

# angle between two points, from North, going clockwise
def bearing(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    x = x2-x1
    y = y1-y2
    theta = atan2(y, x)
    if 0 <= theta and theta <= pi/2:
        theta = pi/2 - theta
    elif pi/2 < theta and theta <= pi:
        theta = 5*pi/2 - theta
    else:
        theta = pi/2 - theta
    return theta
        
# pythagorean distance between two points
def dist(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    x = x2-x1
    y = y2-y1
    return ((x**2) + (y**2)) ** (1/2)

# find asteroid which can see the most asteroids on ast_map
def best_visibility(ast_map):
    best_x = None
    best_y = None
    best_count = -1
    for (x, y) in ast_map.asteroids:
        count = ast_map.visibility_grid[x][y]
        if count > best_count:
            best_count = count
            best_x, best_y = x, y
    return best_x, best_y, best_count

main()
