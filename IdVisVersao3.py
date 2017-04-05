from math import*
import csv

def square_rooted(x): 
    return round(sqrt(sum([a*a for a in x])),9)
 
def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),9)

def jaccard_similarity(x,y): 
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)
cantinho = "cantinho.png"
def usarFiji():
    type(Key.F6)
    click(Location(16, 40))#Click on menu (File)
    hover(Location(13, 64))#Hover on the 'New' option
    hover(Location(383, 67))#Hover on the 'Imagem' option
    click(Location(364, 168))#Click on 'System Clipboard' option
    click(Location(97, 39))#Click on Menu (Image)- First time
    hover(Location(91, 65))#Hover on the 'Type' option
    click(Location(380, 63))#Click on '8-bit' option
    click(Location(97, 39))#Click on Menu (Image)- Second time
    hover(Location(89, 101))#Hover on the 'Adjust' option
    hover(Location(468, 99))#Hover on the 'Brightness/Contranst' option
    click(Location(427, 177))#Click on 'Threshold...' option
    click(Location(696, 397))#Click on 'Apply' button
    click(Location(844, 157))#Close 'Threshold' dialog window
    click(Location(232, 42))#Click on menu (Analyze)
    click(Location(278, 91))#Click on menu 'Analyze Particles' option
    click(Location(709, 405))#Click on 'OK' button
    click(Location(591, 38))#Click on Menu (Files) on the 'Results' window
    click(Location(595, 64))#Click on 'Save-As' option
    click(Location(1385, 399))#Clica no botão Salvar
    click(Location(781, 446))#Clica no botão Sim (Arquivo Results.xls jah existe)
    click(Location(1363, 13))#Close 'Results' window
    if exists(cantinho):
        #Close 'Clipboard' window
        rightClick(cantinho)        
        click(Pattern(cantinho).targetOffset(16,129))
    click(Location(715, 280))#Confirming closing withous saving changes

#usarFiji()

def usarFijiMeasure():
    click(Location(167, 41))#Click on menu (Process)
    hover(Location(148,359))#Hover on 'Batch' option
    sleep(1)
    click(Location(457,360))#Hover on 'Measure' option
    type('C:\Users\manoe\Desktop\IdvisImagens')#Open folder
    click(Location(970, 590))#Confirm opening folder
    click(Location(591, 38))#Click on Menu (Files) on the 'Results' window
    click(Location(595, 64))#Click on 'Save-As' option
    sleep(2)
    type('C:\Users\manoe\Desktop\XLS')#Open save place folder
    click(Location(1374, 548))#Clica no botão Abrir
    sleep(2)
    click(Location(1374, 548))#Clica no botão Salvar
    click(Location(778, 446))#Clica no botão Sim (Arquivo Results.xls jah existe)
    click(Location(1412, 10))#Close 'Results' window

usarFijiMeasure()
baliza = []
currentList = []

fo = open('C:\Users\manoe\Desktop\XLS\Results.xls', 'r')
line = fo.readline()
baliza = line.split()
baliza.pop(3)
baliza.pop(3)
baliza.pop(3)
baliza.pop(3)
baliza.pop(0)

baliza = [float(i) for i in baliza]
print baliza
count = 1
fo.close()
fo = open('C:\Users\manoe\Desktop\XLS\Results.xls', 'r')
while line and count<4:
    line = fo.readline()
    currentList = line.split()
    currentList.pop(3)
    currentList.pop(3)
    currentList.pop(3)
    currentList.pop(3)
    currentList.pop(0)
    currentList = [float(i) for i in baliza]
    print currentList
    print cosine_similarity(currentList,baliza)
    count  = count + 1
fo.close()
