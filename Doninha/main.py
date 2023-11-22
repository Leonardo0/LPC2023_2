import random
import string
from time import sleep
# Determina qual o nosso objetivo
alvo = ''
# Tamanho do nosso objetivo
tamanho_alvo = 0
# TODAS AS LETRAS QUE PODEM SER SELECIONADAS
letras_escolha = (string.ascii_uppercase + ' ' + string.punctuation +
                  'ÁÉÍÓÚÀÈÌÒÙÃẼĨÕŨÂÊÎÔÛÇ')
# Tem a função de receber o melhor
melhor = {
    'palavra': '',
    'ponto': 0,
    'base_para_nova_geracao': ''
}
populacao_geracao = 10
backup_dicionario = melhor.copy()
backup_lista = []

todas_geracoes = []

def atualizar_pontos(palavra, pontos):
    melhor['palavra'] = palavra
    melhor['ponto'] = pontos


def contador_pontos(palavra):
    score = 0
    # Para cada letra na minha palavra
    for i in range(tamanho_alvo):
        # Vou checar se a letra da posiçao x
        # é igual a letra posicao x do meu alvo
        if alvo[i] == palavra[i]:
            # Se for meu score é incrementado mais 1
            score = score+1
    return score


def criador_base_para_nova_geracao(melhor_palavra):
    base_nova_geracao = ''
    # Para cada letra
    for i in range(tamanho_alvo):
        # Se o meu caractere for igual ao caractere da palavra
        if alvo[i] == melhor_palavra[i]:
            # Palavra recebe o caractere
            base_nova_geracao = base_nova_geracao + melhor_palavra[i]
        # Senao recebe *
        else:
            base_nova_geracao = base_nova_geracao + '*'
    melhor['base_para_nova_geracao'] = base_nova_geracao


def mudar_caractere(palavra, posicao, caractere_novo):
    # Escreve a palavra muda o caractere e reescreve o resto
    return palavra[:posicao] + caractere_novo + palavra[posicao+1:]


def mudar_nao_match():
    palavra_temporaria = melhor['base_para_nova_geracao']
    # Aqui a palavra tera as letras dividas, com
    # cada uma das letras com uma posicao dada pelo enumerate
    for posicao, letra in enumerate(palavra_temporaria):
        # Se a minha letra nao tiver dado march
        if letra == '*':
            # Minha palavra vai mudar o caractere sem match para um aleatorio
            palavra_temporaria = mudar_caractere(
                palavra_temporaria, posicao, random.choice(letras_escolha))
    return palavra_temporaria


def criar_nova_geracao():
    # Contruir nova base para geração
    criador_base_para_nova_geracao(melhor['palavra'])
    todas_geracoes.append([mudar_nao_match()
                           for i in range(populacao_geracao)])


def checar_match():
    ultima_geracao = todas_geracoes[-1]
    # Para cada letra na ultima geracao eu vou jogar na função de pontos

    for palavra in ultima_geracao:
        pontos = contador_pontos(palavra)
        if pontos > melhor['ponto']:
            atualizar_pontos(palavra, pontos)


def criar_letras_aleatorias(tamanho_alvo):
    # Cada vez que essa função é chamada ela retorna muitas
    # Letras aleatorias, ela para quando chega no tamanho maximo
    return ''.join(random.choice(letras_escolha) for i in range(tamanho_alvo))


def print_melhor_string():
    # Todas as geracoes tem varias strings mas apenas 1 lista por vez
    print('Geração '+str(len(todas_geracoes)),
          'Melhor Pontuação ' + str(melhor['ponto']))
    print('Melhor palavra: ' + melhor['palavra'])

    backup_lista.append([(str(len(todas_geracoes))),
                         (str(melhor['ponto'])),
                         melhor['palavra']])


def monkeys(palavra_chave, tamanho_recebido):
    # Muda o valor do alvo para a palavra chave
    global alvo
    alvo = palavra_chave
    global populacao_geracao
    populacao_geracao = tamanho_recebido

    # Tamanho do meu alvo vai ser do mesmo tamanho da palavra chave
    global tamanho_alvo
    tamanho_alvo = len(palavra_chave)

    # Minha geração lista vai receber varias strings
    # Aleatorias, no caso 100 delas mas poderia ser modificado para 2 etc
    # IMPORTANTE DIZER QUE ELA RECEBE 1 LISTA COM VARIAS PALAVRAS
    todas_geracoes.append([criar_letras_aleatorias
                           (tamanho_alvo) for i in range(populacao_geracao)])

    checar_match()
    print_melhor_string()
    while True:
        if alvo == melhor['palavra']:
            print('cabou')
            backup_dicionario = melhor.copy()
            alvo = ''
            populacao_geracao = 10
            melhor['ponto'] = 0
            melhor['base_para_nova_geracao'] = ''
            todas_geracoes.clear()
            sleep(0.1)
            return backup_dicionario, backup_lista
        else:
            criar_nova_geracao()
            checar_match()
            print_melhor_string()
            