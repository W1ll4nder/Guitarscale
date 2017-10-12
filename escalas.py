notas_original = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
notas = notas_original
def maior():
    if escala == 'maior':
        esc1 =notas[0]+notas[2]+notas[4]+notas[5]+notas[7]+notas[9]+notas[11]
        print(esc1)
    if escala == 'menor':
        esc1 = notas[0]+notas[2]+notas[3]+notas[5]+notas[7]+notas[8]+notas[10]
        print(esc1)
cont = 'sim'
while cont == 'sim':
    tom = input('digite o tom da escala que vc deseja: ').upper()
    escala = input('qual escala vc deseja saber? ').lower()
    if tom in notas:
        posição = notas_original.index(tom)
        notas = notas_original[posição:] + notas_original[:posição]
        maior()
        c = input('se deseja continuar digite sim ou não para sair: ').lower()
        cont = c
    else:
        print('digite uma nota válida')











