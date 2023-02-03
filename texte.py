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




Classe = input('Você e um mago, arqueiro ou um cavaleiro? ')


Escolha2 = Classe.lower()

if Escolha2 == 'cavaleiro':
    print('Sua espada era tão afiada que tu se furou com ela')

elif Escolha2 == 'arqueiro':
    print('Você não sabia utilizar um arco e flecha, então voce acabou furando seu bucho e morreu de Hemorragia.')

elif Escolha2 == 'mago':
    magoPtx = input('Você acorda com uma carta na sua porta, voce pode "ler" ou'
                    ' "ignorar" o que voce faz? ').lower().strip()

if magoPtx == 'ignorar':
    print('Você voltou a dormir e nada depois disso aconteceu.')

elif magoPtx == 'ler':
    magoH1 = input('Você leu a carta, nela dizia que sua esposa(o) foi sequestrada(o), '
                   ' voce pode "ir" ou "ficar" o que voce faz? ').lower().strip()


if magoH1 == 'ficar':
    print('você ficou em sua casa, 3 dias depois você recebe a noticia da morte de sua esposa(o).')

elif magoH1 == 'ir':
    magoH2 = input('Você vai, depois de 3 minutos você encontra um org agressivo'
                   ' que esta tampando 3 caminhos, Você pode:"Lutar", "ignorar", "fugir". o que você faz: ')





