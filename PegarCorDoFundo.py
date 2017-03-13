from java.awt import Robot

fundoaSerAnalisado = Region(637,451,6,5).getTopLeft().offset(5,5)

def pegarCorDoFundo():
    banana = fundoaSerAnalisado
    r = Robot()
    c = r.getPixelColor(banana.x, banana.y) # get the color object
    crgb = ( c.getRed(), c.getGreen(), c.getBlue() ) # decode to RGB values
    print crgb
    return crgb==(255, 255, 255)

pegarCorDoFundo()

