def setup():
    size(350, 400)
    zombie = loadImage("zombie.jpg")
    image(zombie, 0, 0)
    loadPixels()
def draw():
    print(red(pixels[len(pixels)-1]), green(pixels[len(pixels)-1]), blue(pixels[len(pixels)-1]))
    for z in range (len(pixels)):
        currentPixel = pixels[z]
        pixelRed = red(currentPixel)
        pixelGreen = green(currentPixel)
        pixelBlue = blue(currentPixel)
        pixelRed = 255 - pixelRed
        pixelGreen = 255 - pixelGreen
        pixelBlue = 255 - pixelBlue
        newColor = color((pixelRed + pixelGreen + pixelBlue)/3)
        pixels[z] = newColor
    updatePixels()
