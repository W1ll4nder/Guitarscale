notas = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']

def maior():
    esc1 = (notas[0:6:2])
    esc2 = (notas[5:12:2])
    print(esc1+esc2)

tom = input('digite o tom da escala que vc deseja: ').lower()

if tom in notas:
    if tom == notas[0]:
        maior()

    if tom == notas[1]:
        notas1 = notas[1:]
        notas2 = notas[0]
        esc = notas1 + notas2
        notas = esc
        maior()
    if tom == notas[2]:
        notas1 = notas[2:]
        notas2 = notas[0:2]
        esc = notas1 + notas2
        notas = esc
        maior()
    if tom == notas[3]:
        notas1 = notas[3:]
        notas2 = notas[0:3]
        esc = notas1 + notas2
        notas = esc
        maior()
    if tom == notas[4]:
        notas1 = notas[4:]
        notas2 = notas[0:4]
        esc = notas1 + notas2
        notas = esc
        maior()
    if tom == notas[5]:
        notas1 = notas[5:]
        notas2 = notas[0:5]
        esc = notas1 + notas2
        notas = esc
        maior()
    if tom == notas[6]:
        notas1 = notas[6:]
        notas2 = notas[0:6]
        esc = notas1 + notas2
        notas = esc
        maior()
    if tom == notas[7]:
        notas1 = notas[7:]
        notas2 = notas[0:7]
        esc = notas1 + notas2
        notas = esc
        maior()
    if tom == notas[8]:
        notas1 = notas[8:]
        notas2 = notas[0:8]
        esc = notas1 + notas2
        notas = esc
        maior()
    if tom == notas[9]:
        notas1 = notas[9:]
        notas2 = notas[0:9]
        esc = notas1 + notas2
        notas = esc
        maior()
    if tom == notas[10]:
        notas1 = notas[10:]
        notas2 = notas[0:10]
        esc = notas1 + notas2
        notas = esc
        maior()
    if tom == notas[11]:
        notas1 = notas[11:]
        notas2 = notas[0:11]
        esc = notas1 + notas2
        notas = esc
        maior()
else:
    print('digite uma nota válida')








