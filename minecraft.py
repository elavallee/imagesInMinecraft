from PIL import Image
import math

# world height - 251

colorLookup = {(222, 79, 222) : 'Magenta Wool',
               (123, 26, 165) : 'Purple Wool',
               (202, 16, 16)  : 'Red Wool',
               (150, 57, 20)  : 'Brown Wool',
               (251, 127, 4)  : 'Orange Wool',
               (251, 236, 4)  : 'Yellow Wool',
               (255, 255, 255): 'White Wool',
               (160, 160, 160): 'Light Gray Wool',
               (96, 96, 96)   : 'Gray Wool',
               (0, 0, 0)      : 'Black Wool',
               (34, 28, 138)  : 'Blue Wool',
               (64, 192, 192) : 'Light Blue Wool',
               (38, 159, 93)  : 'Cyan Wool',
               (28, 126, 28)  : 'Green Wool',
               (99, 210, 36)  : 'Lime Wool',
               (247, 110, 145): 'Pink Wool'}

colorNumberings = {'Magenta Wool'   : 1,
                   'Purple Wool'    : 2,
                   'Red Wool'       : 3,
                   'Brown Wool'     : 4,
                   'Orange Wool'    : 5,
                   'Yellow Wool'    : 6,
                   'White Wool'     : 7,
                   'Light Gray Wool': 8,
                   'Gray Wool'      : 9,
                   'Black Wool'     : 10,
                   'Blue Wool'      : 11,
                   'Light Blue Wool': 12,
                   'Cyan Wool'      : 13,
                   'Green Wool'     : 14,
                   'Lime Wool'      : 15,
                   'Pink Wool'      : 16}

def resize(im, maxBlocks=50.0):
    "Resize an image to be Minecraftable."
    maxDim = max(im.width, im.height)
    ratio = maxBlocks/maxDim
    newWidth = int(ratio*im.width)
    newHeight = int(ratio*im.height)
    return im.resize((newWidth, newHeight))

def rgbDistance(RGB1, RGB2):
    "Calculate the distance between two RGB values."
    r1, g1, b1 = RGB1
    r2, g2, b2 = RGB2
    return math.sqrt((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2)

def convertColor(RGB):
    "Convert the color of a pixel to the closest Minecraft color."
    minDistance = 450
    newColor = min(colorLookup.keys(), key=lambda x: rgbDistance(RGB, x))
    return newColor
    
def mapPixels(im):
    "Create a list of lists for mapping a picture to Mincraft blocks."
    minecraftMap = []
    for y in range(im.height):
        xVals = []
        for x in range(im.width):
            newColor = convertColor(im.getpixel((x, y)))
            xVals.append(colorNumberings[colorLookup[newColor]])
        minecraftMap.append(xVals)
    return minecraftMap

def showImage(im):
    "Display a picture as it would look in Minecraft."
    for y in range(im.height):
        for x in range(im.width):
            newColor = convertColor(im.getpixel((x, y)))
            im.putpixel((x, y), newColor)
    im.show()

def printMap(minecraftMap):
    for y in minecraftMap:
        horzText = '|'.join(["{:>2}".format(x) for x in y])
        print('-'*len(horzText))
        print(horzText)
    print('-'*len(horzText))
    items = colorNumberings.iteritems()
    items = [(b, a) for a, b in items]
    items = sorted(items)
    for number, color in items:
        print('{} - {}'.format(number, color))

def printMapCondensed(minecraftMap):
    for line, y in enumerate(minecraftMap):
        currentNum = y[0]
        cnt = 0
        txtList = []
        for x in y:
            if x != currentNum:
                txtList.append('{}x-{}'.format(cnt, currentNum))
                currentNum = x
                cnt = 1
            else:
                cnt += 1
        txtList.append('{}x-{}'.format(cnt, currentNum))
        print('{}: '.format(len(minecraftMap)-line) + '; '.join(txtList))

def convertPNG(im):
    "convert the alpha to a white background."
    im.load()
    background = Image.new("RGB", im.size, (255, 255, 255))
    background.paste(im, mask=im.split()[3]) # 3 is the alpha channel
    return background

def cropIm(im, width=500, height=250):
    "crop an image to some dims."
    newIm = Image.new("RGB", (width, height), (255, 255, 255))
    for ynew, y in enumerate(range(int(im.height/2 - height/2), int(im.height/2 + height/2))):
        for xnew, x in enumerate(range(int(im.width/2 - width/2), int(im.width/2 + width/2))):
            newIm.putpixel((xnew, ynew), im.getpixel((x, y)))
    return newIm
            

def doAnImage(filename, maxBlocks=200.0, cropIt=False):
    im = Image.open(filename)
    if filename.lower().endswith('.png'):
        im = convertPNG(im)
    if cropIt:
        im = cropIm(im)
    imMine = resize(im, maxBlocks)
    print('Width: {}, Height: {}, Total Blocks: {}'.format(imMine.width, imMine.height, imMine.width*imMine.height))
    minecraftMap = mapPixels(imMine)
    printMapCondensed(minecraftMap)

if __name__ == "__main__":
    doAnImage('Peter_Parker_(Earth-30847)_from_Marvel_vs._Capcom_Infinite_0001.png', 100.0)
