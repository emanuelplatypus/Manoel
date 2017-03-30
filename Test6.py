from java.awt import Robot

Reg1 = Region(401,316,642,258)

def pegarCorDoFundo(banana):
    r = Robot()
    c = r.getPixelColor(banana.x, banana.y) # get the color object
    crgb = ( c.getRed(), c.getGreen(), c.getBlue() ) # decode to RGB values
    return crgb==(0, 0, 0)

ind = 0 
indice = 0
count = 0
hover(Location(942, 142))
for x in xrange(200):    
    if (x==1) or (x==199):
        hover(Location(401+indice,316+ind))
        wait(1)
    if pegarCorDoFundo(Location(401+indice,316+ind)):
        count = count + 1
        
    ind = ind + 1
    indice = indice + 3

print count
    