import numpy as np

class Component:

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.array = np.full((length, width), height)

    def getArrayAt(self, x, y):
        return self.array[x][y]

    def remove(self, x, y, z):
        offset = self.length / 2
        if x >= -35 and x <= 34 and y >= -35 and y <= 34:
            self.array[int(x + offset)][int(y + offset)] = z

    def removeTopRight(self, startX, endX, y, z):
        end = startX + endX
        for i in range(startX, end + 1):
            self.remove(i, y, z)

    def removeTopLeft(self, startX, endX, y, z):
        end = startX + endX
        k = startX
        for i in range(startX, end + 1):
            self.remove(k, y, z)
            k = k - 1

    def removeBotRight(self, startX, endX, y, initY, z):
        tmp = y - initY - 1
        end = startX + endX
        for i in range(startX, end + 1):
            self.remove(i, initY - tmp, z)

    def removeBotLeft(self, startX, endX, y, initY, z):
        tmp = y - initY - 1
        end = startX + endX
        k = startX
        for i in range(startX, end + 1):
            self.remove(k, initY - tmp, z)
            k = k - 1

    def removeCircle(self, startX, endX, y, initY, z):
        self.removeTopRight(startX, endX, y, z)
        self.removeTopLeft(startX, endX, y, z)
        self.removeBotRight(startX, endX, y, initY, z)
        self.removeBotLeft(startX, endX, y, initY, z)

    def printArray(self):
        print(self.array)