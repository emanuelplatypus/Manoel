# Lembrar de tirar as funcoes wait() ou dimunuir seus tempos
Settings.MinSimilarity = 0.9

def ControlCommmands(letra):
    type(letra, KeyModifier.CTRL)
    type(letra, KeyModifier.CTRL)
    type(letra, KeyModifier.CTRL)  

def EscreverOqueFoiEncontrado(x):
    click(Location(386, 46))
    type(x)
    type(' encontrad(a)o no documento em tela e batendo com o CADASTRO. Vou pressionar F2 para esse item.')
    wait(5)

def EscreverOqueNaoFoiEncontrado(x):
    click(Location(386, 46))
    type(x)
    wait(5)
def vereAlinharTodaImagem():
    while not exists("1489149778907.png"):
        ControlCommmands('-')
        
def funcao1():
    #popup('Numero da Agencia na FAA')
    dragDrop(Location(434, 122), Location(1224, 738))        
    type(Key.F6)
    ControlCommmands('c')
    myString = Env.getClipboard().strip()
    myString = ''.join(e for e in myString if e.isalnum())
    print (myString)
    if '2003' in myString:
        EscreverOqueFoiEncontrado('Numero da agencia')
    elif '20898903' not in myString:
        EscreverOqueNaoFoiEncontrado('Numero da agencia nao encontrado.')

def funcao2():
    #popup('Numero da Operacao na FAA')
    dragDrop(Location(434, 122), Location(1224, 738))
    ControlCommmands('c')
    myString = Env.getClipboard().strip()
    print (myString)
    if 'Michael' in myString:
        EscreverOqueFoiEncontrado('Operacao')
    elif 'Michael5s4df54' not in myString:
        EscreverOqueNaoFoiEncontrado('Operacao nao encontrada')
        
def funcao3():
    #popup('Numero da conta na FAA')
    dragDrop(Location(434, 122), Location(1224, 738))
    ControlCommmands('c')
    myString = Env.getClipboard().strip()
    print (myString)
    if 'purchase' in myString:
        EscreverOqueFoiEncontrado('Numero da conta')
    elif 'purchase1516515' not in myString:
        EscreverOqueNaoFoiEncontrado('Numero da conta nao encontrado.')
        
def funcao4():
    #popup('Nome do titular na FAA')
    dragDrop(Location(434, 122), Location(1224, 738))
    ControlCommmands('c')
    myString = Env.getClipboard().strip()
    print (myString)
    if 'luck' in myString:
        EscreverOqueFoiEncontrado('Nome do titular em FAA')
    elif 'luck649841' not in myString:
        EscreverOqueNaoFoiEncontrado('Nome do titular em FAA nao encontrado.')

def funcao5():
    #popup('CEP do endereco do titular na FAA')
    dragDrop(Location(434, 122), Location(1224, 738))
    ControlCommmands('c')
    myString = Env.getClipboard().strip()
    print (myString)
    if 'money' in myString:
        EscreverOqueFoiEncontrado(' CEP do endereco do titular em FAA')
    elif 'money65sad545' not in myString:
        EscreverOqueNaoFoiEncontrado('CEP do endereco do titular em FAA nao encontrado.')

def funcao6():
    #popup('CPF do titular na FAA')
    dragDrop(Location(434, 122), Location(1224, 738))
    ControlCommmands('c')
    myString = Env.getClipboard().strip()
    print (myString)
    if 'happening' in myString:
        EscreverOqueFoiEncontrado(' CPF do titular em FAA')
    elif 'happening45466f6' not in myString:
        EscreverOqueNaoFoiEncontrado('CPF do titular em FAA nao encontrado.')

def funcao7():
    #popup('Data de Nascimento do titular na FAA')
    dragDrop(Location(434, 122), Location(1224, 738))
    ControlCommmands('c')
    myString = Env.getClipboard().strip()
    print (myString)
    if 'equipment' in myString:
        EscreverOqueFoiEncontrado(' Data de Nascimento do titular em FAA')
    elif 'equipment45466f6' not in myString:
        EscreverOqueNaoFoiEncontrado('Data de Nascimento  do titular em FAA nao encontrado.')

def funcao8():
    #popup('Rua do endereco do titular na FAA')
    dragDrop(Location(434, 122), Location(1224, 738))
    ControlCommmands('c')
    myString = Env.getClipboard().strip()
    print (myString)
    if 'Danny' in myString:
        EscreverOqueFoiEncontrado(' Rua do endereco do titular em FAA')
    elif 'Danny669871' not in myString:
        EscreverOqueNaoFoiEncontrado('Rua do endereco do titular em FAA nao encontrado.')

def funcao9():
    #popup('Rua do endereco do titular na FAA')
    dragDrop(Location(434, 122), Location(1224, 738))
    ControlCommmands('c')
    myString = Env.getClipboard().strip()
    print (myString)
    if 'internships' in myString:
        EscreverOqueFoiEncontrado(' Rua do endereco do titular em FAA')
    elif 'internships' not in myString:
        EscreverOqueNaoFoiEncontrado('Rua do endereco do titular em FAA nao encontrado.')


def funcao10():
    #popup('Nome do titular no CPF')
    dragDrop(Location(434, 122), Location(1224, 738))
    ControlCommmands('c')
    myString = Env.getClipboard().strip()
    print (myString)
    if 'luxury' in myString:
        EscreverOqueFoiEncontrado(' Nome do titular no CPF')
    elif 'luxury456rgre' not in myString:
        EscreverOqueNaoFoiEncontrado('Nome do titular no CPF nao encontrado.')

def funcao11():
    #popup('Data de Nascimento do titular no CPF')
    dragDrop(Location(434, 122), Location(1224, 738))
    ControlCommmands('c')
    myString = Env.getClipboard().strip()
    print (myString)
    if 'antenna' in myString:
        EscreverOqueFoiEncontrado(' Data de Nascimento do titular na Identidade encontrada')
    elif 'antenna65rgre' not in myString:
        EscreverOqueNaoFoiEncontrado('Data de Nascimento do titular na Identidade nao encontrada')

def funcao12():
    #popup('Numero do titular no RG ou documento equivalente')
    dragDrop(Location(434, 122), Location(1224, 738))
    ControlCommmands('c')
    myString = Env.getClipboard().strip()
    print (myString)
    if 'Copyright' in myString:
        EscreverOqueFoiEncontrado(' Numero DO documento De Identidade no RG ou equivalente')
    elif 'Copyright654894' not in myString:
        EscreverOqueNaoFoiEncontrado('Numero DO documento De Identidade ou equivalente nao encontrado.')

def funcao13():
    #popup('Nome do titular NO documento De Identidade')
    dragDrop(Location(434, 122), Location(1224, 738))
    ControlCommmands('c')
    myString = Env.getClipboard().strip()
    print (myString)
    if 'Donkey' in myString:
        EscreverOqueFoiEncontrado(' Nome DO titular no doc de identidade (RG ou equivalente)')
    elif 'Donkey6548941' not in myString:
        EscreverOqueNaoFoiEncontrado('Nome DO titular no doc de identidade (RG ou equivalente) nao encontrado.')

def funcao14():
    #popup('Data de Nascimento do titular no RG ou documento equivalente')
    dragDrop(Location(434, 122), Location(1224, 738))
    ControlCommmands('c')
    myString = Env.getClipboard().strip()
    print (myString)
    if 'gbayliss' in myString:
        EscreverOqueFoiEncontrado(' Data de Nascimento do titular no RG ou doc equivalente')
    elif 'gbayliss65w44sd' not in myString:
        EscreverOqueNaoFoiEncontrado('Data de Nascimento do titular no RG ou doc nao encontrado.')

for letter in 'oi':# Para cada letra da palavra 'oi'
    click(Location(1431, 106))

#Para analise da  /////FAA///// => Vai da linha 140 ateh a 180 mais ou menos
click(Location(149, 159))
itensFAA = 'agenciacontaoperacaonumerodacontanometitularRUAdoEnderecoNaFAAcepFAACPFnaFAAdataNascimento'
if '2agencia' in itensFAA:
    click(Location(37, 195))
    wait(1)
    funcao1()

if '2operacao' in itensFAA:
    click(Location(42, 282))
    wait(1)
    funcao2()

if '2numerodaconta' in itensFAA:
    click(Location(56, 418))
    wait(1)
    funcao3()

if '6nometitular' in itensFAA:
    click(Location(59, 574))
    wait(1)
    funcao4()

if '5cepFAA' in itensFAA:
    click(Location(85, 739))
    wait(1)
    funcao5()

if '6CPFnaFAA' in itensFAA:
    click(Location(71, 822))
    wait(1)
    funcao6()

if '9dataNascimento' in itensFAA:
    click(Location(76, 638))
    wait(1)
    funcao7()

if '9RUAdoEnderecoNaFAA' in itensFAA:
    click(Location(102, 854))
    wait(1)
    funcao8()

#Para analise do  /////CPF///// => Vai da linha 158 ateh a linha 168 mais ou menos
click(Location(46, 116))   
itensCPF = 'numerodoCPFnoCPFNomeNoCPFDataNascNOCPF'
if '5numerodoCPF' in itensCPF:
    click("1489145586255.png")
    wait(1)
    funcao9()

if '5NomeNoCPF' in itensCPF:
    click("1489145606565.png")
    wait(1)
    funcao10()

if '7DataNascNOCPF' in itensCPF:
    click("1489147321014.png")
    wait(1)
    funcao11()


#Para analise do  /////DOCUMENTO DE IDENTIDADE///// => Vai da linha 197 ateh a linha 207 mais ou menos
click(Location(46, 116))   
itensRGouEquivalente = 'numeroDOdocumentoDeIdentidadeNomeNoDocumentoDeIdentidadeDataNascNORG'
if '4numeroDOdocumentoDeIdentidade' in itensRGouEquivalente:
    click("1489146623652.png")
    wait(1)
    funcao12()

if '8NomeNoDocumentoDeIdentidade' in itensRGouEquivalente:
    click("1489146648091.png")
    wait(1)
    funcao13()

if 'DataNascNORG' in itensRGouEquivalente:
    click("1489147653761.png")
    wait(1)
    funcao14()