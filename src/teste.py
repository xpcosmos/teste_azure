#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pandas as pd
import os



questoes_path = os.path.abspath("src/questoes.csv")

def introducao():
    print('''
        Ola! Esse é um teste para você treinar questões do AZ-900!
        Se você deseja dar uma olhada nas instruções:

        (1) Sim, desejo olhar as instruções (recomendado para primeiro uso)
        (2) Não desejo olhar as introduções

        Digite o número correspondente a instrução desejada.



        ''')
    user_reponse = input()

    if user_reponse == "1":
        instrucoes()

def instrucoes():
    print('''
        Vamos lá! Agora você verá alguns conceitos básicos sobre as questões:

        - Temos 3 tipo de questões:
            > Múltipla escolha;
            > Escolha única;
            > Substituir a frase .
        
        Cada questão será identificada em seu começo. Você deve escolhar a opção que achar correta e apertar enter

        - Questões de múltipla escolhas:
            > Nessas questões você precisará escolhar mais de uma opção. Vamos supor que você acredita que a opção B e C estão corretas. Na sua reposta você deverá digitar "BC" sem espaços.
            > Não importará das questões.
        
        - Substituir a frase:
            > A frase a ser avaliada estará envolta de "_", por exemplo:
                "A frase a ser avaliada é a _seguinte frase_."
        
        Pressione "Enter" para proseguir
            ''')
    input()
    print('''
    > Ao final do teste você recebará uma nota e o seu resultado irá falar se você passou ou não.
    > Você também encontrará tópicos que errou para estudar mais e melhorar no assunto.
    > Ao final de cada questão você poderá ler um pouco da explicação da questão

    Pressione "Enter" para proseguir
    ''')

def carregar_questoes():
    return pd.read_csv(questoes_path)

def selecionar_questoes_user(questoes):
    questoes_user_list = []

    for i, j in zip(questoes.tema.unique(), [15, 20,15,10]):
        questoes_user_list.append(questoes.loc[questoes.tema == i].sample(j))
    return pd.concat(questoes_user_list)

def exibir_questoes(questoes):
    for i in questoes.index:
        if len(questoes.iloc[i, 7]) >= 2:
            print('[Questão de múltipla escolha]\n\n')
        else:
            print('[Questão de única escolha]\n\n')
        # Print de enunciado:

        print(questoes.iloc[i, 1])

        opcoes = []
        for opcao in questoes.iloc[i, 2:6]:
            try:
                if opcao[0] != "NaN":
                    opcoes.append(opcao)
            except:
                pass
        tamanho_opcoes = len(opcoes)
        alternativas = ['A', 'B', 'C', 'D', 'E']
        
        for opcao, alternativa in zip(opcoes, alternativas[0, tamanho_opcoes]):
            print(f'{alternativa} - {opcao}')
        
        print('\n\n\nEscolha a(s) alternativa(s) correta(s):')
        opcao_usuario =  input()
        if opcao_usuario == questoes.iloc[i, 7]:
            print('''
                    Parabéns, você acertou! Deseja verificar a explicação para a questão?

                    (1) Sim
                    (2) Não, próxima questão
                    ''')
        if opcao_usuario != questoes.iloc[i, 7]:
            print('''
                    Que pena, você errou! Deseja verificar a explicação para a questão?

                    (1) Sim
                    (2) Não, próxima questão
                    ''')
        
        passar_questao = input()
        if passar_questao == 1:
            print(questoes.iloc[i, 8])
            print('Pressione "Enter" para acessar a próxima questão:')
        
        input()
        
        



if __name__ == "__main__":
    introducao() # Seguirá para instruções caso o usuário queira
    selecionar_questoes_user(carregar_questoes())
