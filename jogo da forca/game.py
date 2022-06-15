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
arquivoPL = open('players.txt', 'w')
arquivoPL.write(f'DESAFIANTE > {desafiante}')
arquivoPL.write('\n')
arquivoPL.write(F'COMPETIDOR > {competidor}')
arquivoPL.write('\n')
arquivoPL.write(f'PALAVRA > {palavra}')
arquivoPL.write('\n')
arquivoPL.close()


def jogo():
   
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
                print('Competidor venceu!')
                break
            else:
                print(f'Palavra secreta: {secreto_temp}')
            
            if letra not in palavra:
                chance -= 1
            
            if chance <= 0:
                print('Desafiante venceu!')
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
                print('Competidor venceu!')  
                break 
            elif chuteR != palavra:
                print('Desafiante venceu!')
                break
jogo()






    
