#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pandas as pd
import os




def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def introducao():
    print('''
Ola! Esse é um teste para você treinar questões do AZ-900!
Se você deseja dar uma olhada nas instruções:

(1) Sim, desejo olhar as instruções (recomendado para primeiro uso)
(2) Não desejo olhar as introduções

Digite o número correspondente a instrução desejada.



        ''')
    user_reponse = input()
    clear()
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
    clear()
    print('''
> Ao final do teste você recebará uma nota e o seu resultado irá falar se você passou ou não.
> Você também encontrará tópicos que errou para estudar mais e melhorar no assunto.
> Ao final de cada questão você poderá ler um pouco da explicação da questão

    Pressione "Enter" para proseguir
    ''')
    input()
    clear()

def carregar_questoes(questoes_path):
    return pd.read_csv(questoes_path)

def selecionar_questoes_user(questoes):
    questoes_user_list = []

    for i, j in zip(questoes.tema.unique(), [15, 20,15,10]):
        questoes_user_list.append(questoes.loc[questoes.tema == i].sample(j))
    return pd.concat(questoes_user_list)

def exibir_questoes(questoes):
    questoes.reset_index(drop=True, inplace=True)
    for i in questoes.index:
        multipla_escolha = str(questoes.iloc[i, 7])

        
        clear()
        if len(multipla_escolha) == 1:
            print('[Questão de única escolha]\n\n')
        else:
            print('[Questão de múltipla escolha]\n\n')
        
        # Print de enunciado:

        print(questoes.iloc[i, 1])
        print('\n\n\n')
        opcoes = []
        for opcao in questoes.iloc[i, 2:7]:
            try:
                if opcao[0] != "NaN":
                    opcoes.append(opcao)
            except:
                pass
        
        tamanho_opcoes = len(opcoes)
        
        alternativas = ['A', 'B', 'C', 'D', 'E']
        alternativas = alternativas[0:tamanho_opcoes] 
        
        for opcao, alternativa in zip(opcoes, alternativas):
            print(f'{alternativa} - {opcao}')
        
        print('\n\n\nEscolha a(s) alternativa(s) correta(s):')
        opcao_usuario =  input()
        clear()
        
        if opcao_usuario.capitalize() == questoes.iloc[i, 7].strip():
            print('''
Parabéns, você acertou! Deseja verificar a explicação para a questão?

(1) Sim
(2) Não, próxima questão
                ''')
            
            resultados.append(1)
        if opcao_usuario.capitalize() != questoes.iloc[i, 7].strip():
            print('''
Que pena, você errou! Deseja verificar a explicação para a questão?

(1) Sim
(2) Não, próxima questão
                ''')
            
            resultados.append(0)
        
        passar_questao = input()
        clear()
        if passar_questao == "1":
    
            explicacao = questoes.iloc[i, 8]
            
            print(explicacao)
            input('\n\nPressione "Enter" para acessar a próxima questão:\n')
            clear()
    return resultados

def exibir_resultado(questoes, resultados):
    temas = questoes.iloc[:,9].reset_index(drop=True)
    resultado = pd.DataFrame({'acertos_binarios':resultados})
    resultado = pd.concat([temas, resultado], ignore_index=True, axis=1)
    resultado.columns = ['tema','acertou']

    for i in resultado['tema'].unique():
        questoes_acertadas = resultado.loc[resultado['tema'] == i]['acertou'].sum()
        n_questoes_totais = resultado.loc[resultado['tema'] == i]['tema'].value_counts()[0]
        per_questoes_acertadas = round((questoes_acertadas/n_questoes_totais),3) * 100
        print('Resultados:\n')
        print(f'{i}\n{per_questoes_acertadas}%')
    questoes_totais_corretas = resultado['acertou'].sum()
    questoes_totais_corretas = round((questoes_totais_corretas / 60),3) * 100 
    print(f'\n')
    print('\n\nSugestão: É preferível que você estude os conteúdos que teve mais difuldade antes de realizar uma nova tentativa')
    input('\nPressione "Enter" para sair:\n')
    exit()



if __name__ == "__main__":
    resultados = []
    questoes_path = os.path.abspath("src/questoes.csv")
    introducao() # Seguirá para instruções caso o usuário queira
    questoes = selecionar_questoes_user(carregar_questoes(questoes_path))
    resultados = exibir_questoes(questoes)
    exibir_resultado(questoes, resultados)