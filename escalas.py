notas = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']

def maior():
    esc1 = (notas[0:6:2])
    esc2 = (notas[5:12:2])
    print(esc1+esc2)

tom = input('digite o tom da escala que vc deseja: ')

if tom in notas:
    if tom == notas[0]:
        maior()
    if tom == notas[1]:
        notas1 = notas[1:]
        notas2 = notas[0]
        notas2+= str(notas2)
        esc = notas1 + notas2
        notas = esc
        maior()

    if tom == notas[2]:
        notas1 = notas[2:]
        notas2 = notas[0:2]
        esc = notas1 + notas2
        notas = esc
        maior()


