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

# Tecnologias utilizadas

* Python
  * Pandas


# Autor

<a href="https://www.linkedin.com/in/mikeias-d-s-o/"><img src="https://github.com/xpcosmos/simulador-de-dados/blob/main/assets/linkedin.png" alt="linkedin" width="20"></a> <a href="mailto:mikeias.d.s.o@gmail.com"><img src="https://github.com/xpcosmos/simulador-de-dados/blob/main/assets/gmail.png" alt="gmail" width="20">

# Licença
  
MIT License

Copyright (c) 2022 Mikeias Oliveira

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
