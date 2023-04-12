import time

from PIL import Image

def getHiddenTextWithDelimiter(image, delimiter="\0"):
    tuples = list(image.getdata())
    deli = ""
    pliste = 0
    ptuple = 0
    text = ""
    while deli != delimiter:
        text += deli
        temp = 0
        for j in range(6, -1, -1):
            a = tuples[pliste][ptuple] % 2
            temp += a*(2**j)
            if ptuple == 2:
                pliste += 1
                ptuple = 0
            else:
                ptuple += 1
        deli = chr(temp)
    return text


image = Image.open("hiddenText4.png")


#print(getHiddenTextWithDelimiter(image))


def getHiddenTextOfLength(image, nbBitsForLength):
    tuples = list(image.getdata())
    deli2 = ""
    pliste = 0
    ptuple = 0
    text = ""
    value = 0

    for j in range(nbBitsForLength-1, -1, -1):
        temp = 0
        a = tuples[pliste][ptuple] % 2
        temp += a * (2 ** j)
        if ptuple == 2:
            pliste += 1
            ptuple = 0
        else:
            ptuple += 1
        value += temp

    for k in range(nbBitsForLength, value + nbBitsForLength):
        text += deli2
        temp = 0
        for l in range(6, -1, -1):
            a = tuples[pliste][ptuple] % 2
            temp += a * (2 ** l)
            if ptuple == 2:
                pliste += 1
                ptuple = 0
            else:
                ptuple += 1
        deli2 = chr(temp)
    return text



image1 = Image.open("hiddenText4.png")

a = time.time()
#print(getHiddenTextOfLength(image1, 16))
b = time.time()
#print(b-a)


def getHiddenImage(image, nbBitsForSize):
    tuples = list(image.getdata())

    deli2 = ""
    pliste = 0
    ptuple = 0
    text = ""
    heigth = 0
    length = 0
    count = 0
    rgb = []
    for j in range(nbBitsForSize- 1, -1, -1):
        temp = 0
        a = tuples[pliste][ptuple] % 2
        temp += a * (2 ** j)
        if ptuple == 2:
            pliste += 1
            ptuple = 0
        else:
            ptuple += 1
        heigth += temp


    for j in range(nbBitsForSize - 1, -1, -1):
        temp = 0
        a = tuples[pliste][ptuple] % 2
        temp += a * (2 ** j)
        if ptuple == 2:
            pliste += 1
            ptuple = 0
        else:
            ptuple += 1
        length += temp
    image3 = Image.new("RGB", (heigth, length), (255, 255, 255))
    for i in range(heigth):
        for j in range(length):
            for k in range(nbBitsForSize - 1, -1, -1):
                temp = 0
                a = tuples[pliste][ptuple] % 2
                temp += a * (2 ** k)
                if ptuple == 2:
                    pliste += 1
                    ptuple = 0
                else:
                    ptuple += 1
                rgb[count] = temp
                if count != 2:
                    count += 1
                else:
                    image3.putpixel((i, j), (rgb[0], rgb[1], rgb[2]))
                    count = 0
                    rgb[0] = 0
                    rgb[1] = 0
                    rgb[2] = 0





image2 = Image.open('hiddenImage1.png')
print(getHiddenImage(image2, 8))
