import time, os
from assets.funcoes import clean

while True:
    desafiante = input('Desafiante: ')
    if len(desafiante)<3:
        print("Nome inválido!")
    else:
        break

competidor = input('Competidor: ')
clean()
palavra = input('digite a palavra: ')
   
dica1 = input('Digite a dica 1: ')
dica2 = input('Digite a dica 2: ')
dica3 = input('Digite a dica 3: ')
digitados = []
chance = 5

while True:
    print('(1) JOGAR')
    print('(2) DICA')
    print('(3) CHUTAR PALAVRA')
    lol = input()
    if lol =='1':
        letra = input('Competidor, digite uma letra: ')
        
        if len(letra) > 1:
            print('Não digite mais que uma letra!')
            continue
        
        digitados.append(letra)
        secreto_temp = ''
        for letra_secre in palavra:
            if letra_secre in digitados:
                secreto_temp += letra_secre
            else:
                secreto_temp += '*'

        if secreto_temp == palavra:
            vencedor = (f"Desafiante perdedor {desafiante}. Comepetidor vencedor {competidor}.\n")
            break
        else:
            print(f'Palavra secreta: {secreto_temp}')
        
        if letra not in palavra:
            chance -= 1
        
        if chance <= 0:
            vencedor = (f"Desafiante vencedor {desafiante}. Comepetidor perdedor {competidor}.\n")
            break
        print(f'O competidor ainda tem {chance} chances. ')
        print()
    elif lol == '2':
        print('Escolha qual dica você quer:')
        print('(1) DICA 01')
        print('(2) DICA 02')
        print('(3) DICA 03')
        dicaEscolida = input()
        if dicaEscolida == '1':
            print(dica1)
        elif dicaEscolida == '2':
            print(dica2)
        elif dicaEscolida == '3':
            print(dica3)
        time.sleep(4)
    elif lol == '3':
        chuteR = input('Digite seu chute: ')
        if chuteR == palavra:
            vencedor = (f"Desafiante perdedor {desafiante}. Comepetidor vencedor {competidor}.\n")  
            break 
        elif chuteR != palavra:
            chance -= 1
            continue  
while True:
     clean()
     try:
        print ("\n")
        arquivo = open("arquivo.txt", "a")
        arquivo.write(vencedor + "\n")
        arquivo.close()

        arquivo = open("arquivo.txt", "r")
        clean()
        print("Histórico de partidas:\n")
        for linha in arquivo:
            linha = linha.rstrip()
            print(linha)
        arquivo.close()
        print()
        break
     except:
        arquivo = open("arquivo.txt", "w")
        arquivo.close()
