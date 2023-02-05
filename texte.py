import random

input('Atenção, o codigo esta em desenvolvimento e pode conter bugs,'
      'peço que entenda, \ntente digitar so o que for pedido, "Sim", "Não", "ir", "ficar", etc...'
      'Bom jogo :D (aperte enter para continuar')


nomeDoPersonagem = input('Digite Seu nome: ')
Confirm = input('Seu nome e {} Correto? ' .format(nomeDoPersonagem.lower()))

while Confirm == 'nao':
    pão = input('Digite novamente o seu nome: ')
    Refirm = input('Seu nome e {}? ' .format(pão.lower()))
    Redimin = ('{}' .format(Refirm.lower()))
    if Redimin == 'sim':
        break;

    else:
        print('Tente digitar "SIM" ou "NAO" para confirmar')




Classe = input('Você e um mago, arqueiro ou um cavaleiro? ').lower()



if Classe == 'cavaleiro':
    print('Sua espada era tão afiada que tu se furou com ela')

elif Classe == 'arqueiro':
    print('Você Colocou a bunda na janela e foi de gg.')

elif Classe == 'mago':
    magoPtx = input('Você acorda em mais um dia normal, Você e um dos magos mais renomados do universo' 
                    '\n Voce levanta e vê uma carta na sua porta, voce pode "ler" ou "ignorar" o que voce faz? ').lower().strip()

else:
    print('{} Não e uma opção existente, tente novamente....'.format(Classe))
    exit()

if magoPtx == 'ignorar':
    print('Você voltou a dormir e nada depois disso aconteceu.')

elif magoPtx == 'ler':
    magoH1 = input('Você leu a carta, nela dizia que sua esposa(o) foi sequestrada(o), '
                   ' voce pode "ir" ou "ficar" o que voce faz? ').lower().strip()

else:
    print('{} Não e uma opção existente, tente novamente....'.format(magoPtx))
    exit()


if magoH1 == 'ficar':
    print('você ficou em sua casa, 3 dias depois você recebe a noticia da morte de sua esposa(o).')

elif magoH1 == 'ir':
    magoH2 = input('Você vai, depois de 3 minutos você encontra um org agressivo'
                   ' que esta Impedindo sua passagem por 3 caminhos, Você pode:' 
                   '\n"Lutar","ignorar", "fugir". o que você faz: ').lower()


if magoH2 == 'ignorar':
    print('Você apenas ignorou o Org que se passou de amigavel, quando voce estava de costas ele'
          'O matou.')

elif magoH2 == 'fugir':
    print('Mano, ea tua esposa?, Voce decide fugir, então passam 3 dias,' 
          'e você recebe a noticia da morte de sua esposa')

elif magoH2 == 'lutar':
    print('Rolando dados...')

    y = random.randint(1, 12)
    x = random.randint(1, 20)

    if y > x:
        print('O Org tirou {} e voce tirou {} portanto Org Foi para cima de você'
              '\n e te pegou desprevenidamente, voce acabou morrendo e voltou para o inicio do jogo'.format(y,x))
        exit()



    else:
        Cont = input('Tu tirou {} e o org {}, porntanto voce acabou soltando um feitiço no org e o matou, voce' 
        '\npode escolher entre 3 caminhos "Matagal", "Deserto" ou "Oceano", qual voce escolhe? '.format(x,y)).lower()

    if Cont == 'estrada de pedra':
        print('Tu morreu')

print('Depois Tera continuação')


