from PIL import Image

print("-----------------------------------------Drapeau Français-----------------------------------------")


def creer_drapeau_francais():
    fond_bleu = Image.new("RGB", (450, 300), (0, 0, 255))
    for i in range(150, 300):
        for j in range(300):
           fond_bleu.putpixel((i, j), (255, 255, 255))
    for i in range(300, 450):
        for j in range(300):
           fond_bleu.putpixel((i, j), (255, 0, 0))
    return fond_bleu


#creer_drapeau_francais().show()


print("-----------------------------------------Dégradé de gris-----------------------------------------")


def creer_degrade_vertical() :
    degrade = Image.new("RGB",  (256, 256))
    for i in range(256):
        for j in range(256):
            degrade.putpixel((j, i), (i, i, i))
    return degrade


#creer_degrade_vertical().show()


print("--------------------------Chargement d'une image-------------------------")

lena = Image.open("lena.png")
#lena.show()


print("--------------------------Chargement d'une image-------------------------")

#print(lena.size)
r, g, b = lena.getpixel((0,0))
#print(r,g,b)


print("--------------------------Effet miroir-------------------------")

def miroir(image):
    Xmax,Ymax = image.size
    imageRet = Image.new("RGB", (Xmax, Ymax))
    for i in range(Xmax):
        for j in range(Ymax):
            r, g, b = image.getpixel((i, j))
            imageRet.putpixel((Xmax-i-1, j), (r, g, b))
    imageRet.save("lena_miroir.png")
    return imageRet


#miroir(lena).show()


def negatif(image):
    Xmax, Ymax = image.size
    imageReturn = Image.new("RGB", (Xmax, Ymax))
    for i in range(Xmax):
        for j in range(Ymax):
            r, g, b = image.getpixel((i, j))
            imageReturn.putpixel((i, j), (255-r, 255-g, 255-b))
    return imageReturn


lena_negatif = negatif(lena)
#lena_negatif.show()



def  niveaux_gris(image):
    Xmax, Ymax = image.size
    imageReturn = Image.new("RGB", (Xmax, Ymax))
    for i in range(Xmax):
        for j in range(Ymax):
            r, g, b = image.getpixel((i, j))
            l = int((r+g+b)/3)
            imageReturn.putpixel((i, j), (l, l, l))
    return imageReturn

lena_nb = niveaux_gris(lena)
#lena_nb.show()


def rotation(image, sens_Trigo):
    Xmax, Ymax = image.size
    imageReturn = Image.new("RGB", (Ymax, Xmax))
    if sens_Trigo:
        for i in range(Xmax):
            for j in range(Ymax):
                r, g, b = image.getpixel((i, j))
                imageReturn.putpixel((j,Xmax-i-1 ), (r, g, b))
    else:
        for i in range(Xmax):
            for j in range(Ymax):
                r, g, b = image.getpixel((i, j))
                imageReturn.putpixel((Ymax-j-1, i), (r, g, b))

    return imageReturn

lena90 = rotation(lena, True)
lena90.show()
