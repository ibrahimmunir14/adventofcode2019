from sys import maxsize

WHITE = 0
BLACK = 1
TRANSPARENT = 2
colours = (WHITE, BLACK, TRANSPARENT)

class Layer:
    def __init__(self, data, width, height):
        # pixels[w][h] = pixel at width=w height=h
        self.pixels = [[None for i in range(height)] for j in range(width)]
        # numberOf[x] = number of digit x
        self.numberOf = [0 for i in colours]

        for y in range(height):
            for x in range(width):
                p = int(data.pop(0))
                self.pixels[x][y] = p
                self.numberOf[p] += 1
        if (len(data) > 0): print("Error: Missing Data!")
        
class SpaceImage:
    def __init__(self, data, width, height):
        self.width = width
        self.height = height
        self.layers = []
        self.image = [[None for i in range(height)] for j in range(width)]
        self.__make_layers(data)
        self.__stack_layers()
        
    def __make_layers(self, data):
        pos = 0
        while (pos < len(data)):
            sub_data = data[pos : pos + self.width*self.height]
            layer = Layer(sub_data, self.width, self.height)
            pos += self.width*self.height
            self.layers.append(layer)

    def __stack_layers(self):
        for x in range(self.width):
            for y in range(self.height):
                layer_no = 0
                pixel = 2
                while (layer_no < len(self.layers) and pixel == TRANSPARENT):
                    pixel = self.layers[layer_no].pixels[x][y]
                    layer_no += 1
                self.image[x][y] = pixel
                
    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                p = self.image[x][y]
                p = "Ӝ" if p == BLACK else " "
                print(p, end='')
            print()
        

def main():
    f = open("input8.txt", "r")
    data = list(f.read())[:-1]
    
    image = SpaceImage(data, width=25, height=6)
    
    print("\nImage has", len(image.layers), "layers\n")

    # Part One
    print("---------------------------------------------\nPart One")
    print("---------------------------------------------")
    minLayer = layerWithLeastZeroes(image.layers)
    print("Layer with least zeroes:")
    for i in range(3): print("# of " + str(i) + "s:", minLayer.numberOf[i])
    print()
    result = minLayer.numberOf[1] * minLayer.numberOf[2]
    print("Result =", result)
    print("---------------------------------------------\n\n")

    # Part Two
    print("---------------------------------------------\nPart Two")
    print("---------------------------------------------")
    image.print()
    print("---------------------------------------------")

def layerWithLeastZeroes(layers):
    min_zeroes = maxsize
    min_layer = None
    for layer in layers:
        if layer.numberOf[0] < min_zeroes:
            min_zeroes = layer.numberOf[0]
            min_layer = layer
    return min_layer
        
main()
