#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pandas as pd
import os



questoes_path = os.path.abspath("../src/questoes.csv")

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
    print("""
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
            """)
    input()
    print("""
    Ao final do teste você recebará uma nota e o seu resultado irá falar se você passou ou não.
    Você também encontrará tópicos que errou para estudar mais e melhorar no assunto.
    Ao final de cada questão você poderá 
    """)

if __name__ == "__main__":
    introducao()