import time
from colourwheel import colourwheel

def topLeftToBottomRight(pixels) :
    animationOrder = [[]]
    animationOrder.append([12])
    animationOrder.append([8, 13])
    animationOrder.append([4, 9, 14])
    animationOrder.append([0, 5, 10, 15])
    animationOrder.append([1, 6, 11])
    animationOrder.append([2, 7])
    animationOrder.append([3])

    animate(pixels, animationOrder)

def clockwiseSpiral(pixels) :
    animationOrder = [
        3, 7, 11, 15,
        14, 13, 12,
        8, 4, 0,
        1, 2,
        6, 10,
        9, 5
    ]

    for pixel in animationOrder :
        pixels[pixel] = colourwheel(24)
        time.sleep(0.2)

def animate(pixels, animationOrder) :
    previousRow = None

    for row in animationOrder:
        if not previousRow == None :
            for previousPixel in previousRow :
                pixels[previousPixel] = (0, 0, 0)
        for pixel in row :
            pixels[pixel] = colourwheel(24)
        previousRow = row
        time.sleep(0.2)
