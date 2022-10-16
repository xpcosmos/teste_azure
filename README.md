# Simulador de teste do Azure

Essa aplicação visa criar um simulador da prova AZ900. Todas as questões foram extraídas de questões reais do teste e simuladas dentro do aplicativo do Python.
## Requeriments


pandas|1.4.3|
------|-----|

## Como usar?

Primeiro você deve instalar os requerimentos do aplicativo.

> pip install pandas==1.4.3

Após instalar, baixe esse repositório em seu computador e execute o arquivo _teste.py_. 

O teste será iniciado.

## Pontos importantes...

O teste conta com perguntas de múltipla e única escolha. Caso a pergunta seja de múltipla escolha, você deverá digitar as duas opções sem espaço. Por convenção, caso uma das alternativas estejam incorretas, o computador irá considerar toda a questão com inválida. 

Algumas questões apresentam alguns erros de formatação que serão corrigidos em breve em novas atualizações do projeto.

Ao fim do teste, você receberá um parâmetro geral do número de questões corretas e o tema a qual elas se referem. O teste será finalizado **não** dando a opção de realização de um novo teste, sendo necessário abrir novamento o aplicativo caso assim seja desejado pelo usuário.

## Próximos objetivos:

* Criar uma especificação mais detalhada dos temas das questões;
* Anular todo e qualquer erro de formatação de enunciado de questões;
* Criar meio-ponto para questões de múltipla escolhas

## Ideias ainda mais distantes:

* Mostrar um relatório de progresso de conhecimento
* Expandir catálogo de questões
* Criar alternativas mais sofisticadas para enunciados
