import random

lista_de_palavras = ['Amarelo','Amiga','Amor','Ave','Bolo','Branco','Cama','Caneca','Celular','Céu','Clube','Copo','Doce','Elefante','Escola','Estojo','Faca','Foto','Garfo','Geleia','Girafa','Janela','Limonada','Meia','Noite','ônibus','Ovo','Pai','Parque','Passarinho','Peixe','Pijama','Rato','Umbigo']

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def jogar():
    jogando = True
    letras_digitadas = []
    i = 0


    while jogando is True:
        if i == 0:
            palavra_da_rodada = random.choice(lista_de_palavras).upper()

            palavra_da_rodada_oculta = inicializa_letras_acertadas(palavra_da_rodada)
        i = 1


        print(f'A palavra da rodada tem {len(palavra_da_rodada)} letras:', palavra_da_rodada_oculta,'\n')


        letra_da_rodada = str(input('Digite a letra que você acha que têm na palavra:')).upper()
        print()
        letras_digitadas.append(letra_da_rodada)


        marca_chute_correto(letra_da_rodada, palavra_da_rodada_oculta, palavra_da_rodada)


        if palavra_da_rodada_oculta == list(palavra_da_rodada):
            print(f'PARABÊNS! VOCÊ VENCEU O JOGO\nA PALAVRA ERA {palavra_da_rodada}')
            jogando = False


        if jogando != False:
            print(f'Lestras digitadas: {letras_digitadas}')


