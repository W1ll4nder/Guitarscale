notas_original = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
notas = notas_original
def maior():
    esc1 = (notas[0:6:2])
    esc2 = (notas[5:12:2])
    print(esc1 + esc2)
cont = 'sim'
while cont == 'sim':
    tom = input('digite o tom da escala que vc deseja: ').upper()

    if tom in notas:
        posição = notas_original.index(tom)
        notas = notas_original[posição:] + notas_original[:posição]
        maior()
        c = input('se deseja continuar digite sim ou não para sair: ').lower()
        cont = c
    else:
        print('digite uma nota válida')











