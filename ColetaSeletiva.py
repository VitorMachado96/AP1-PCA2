# -*- coding: utf-8 -*-

#Iniciando os pontos do usuario
SCORE = 0
# Lista de perguntas
lista_de_perguntas = [
   {
       "title": "A alternativa que pareia corretamente o material com a cor do cesto é:", # titulo
       "right_answer": "B", #resposta certa
       "answers": [ #mais uma lista de objetos com as possiveis respostas
           {
               "value": "A", 
               "description": "Plástico - Verde; Metal - Amarelo; Papel - Vermelho; Vidro - Azul; Orgânico - Marrom." 
           },
           {
               "value": "B",
               "description": "Plástico - Azul; Metal - Amarelo; Papel - Vermelho; Vidro - Verde; Orgânico - Marrom."
           },
           {
               "value": "C",
               "description": "Plástico - Amarelo; Metal - Marrom; Papel - Verde; Vidro - Vermelho; Orgânico - Azul."
           }
       ]
   },
   {
       "title": "Quanto tempo o vidro leva para se decompor na natureza?",
       "right_answer": "C",
       "answers": [
           {
               "value": "A",
               "description": "300 anos."
           },
           {
               "value": "B",
               "description": "1000 anos."
           },
           {
               "value": "C",
               "description": "O vidro não é biodegradável."
           }
       ]
   },
   {
       "title": "Assinale a alternativa que aponta corretamente os objetos que NÃO podem ser reciclados.",
       "right_answer": "A",
       "answers": [
           {
               "value": "A",
               "description": "Embalagem de salgadinho (plástico); papel celofane; prato Duralex (vidro); esponja de aço."
           },
           {
               "value": "B",
               "description": "Prato de isopor (plástico); papelão; frasco de perfume; papel alumínio."
           },
           {
               "value": "C",
               "description": "Embalagem de xampu; jornal; copo de requeijão (vidro); lacre."
           }
       ]
   },
   {
       "title": "Qual é o cuidado a ser tomado antes de enviar um determinado material para a reciclagem?",
       "right_answer": "C",
       "answers": [
           {
               "value": "A",
               "description": "Cortá-lo em pedaços pequenos."
           },
           {
               "value": "B",
               "description": "Misturá-lo com materiais do mesmo gênero."
           },
           {
               "value": "C",
               "description": "Limpá-lo."
           }
       ]
   },
   {
       "title": "Quais são as consequências mais diretas do despejo inadequado do lixo?",
       "right_answer": "A",
       "answers": [
           {
               "value": "A",
               "description": "Enchentes e doenças."
           },
           {
               "value": "B",
               "description": "Chuvas ácidas e o buraco na camada de ozônio."
           },
           {
               "value": "C",
               "description": "Extinção de algumas espécies de animais, plantas e bactérias."
           }
       ]
   },
   {
       "title": "Qual é a porcentagem do lixo que é reciclado no Brasil?",
       "right_answer": "A",
       "answers": [
           {
               "value": "A",
               "description": "2%"
           },
           {
               "value": "B",
               "description": "40%"
           },
           {
               "value": "C",
               "description": "4%"
           }
       ]
   },
   {
       "title": "Qual é a cidade que mais produz lixo diariamente no Brasil?",
       "right_answer": "B",
       "answers": [
           {
               "value": "A",
               "description": "Santos."
           },
           {
               "value": "B",
               "description": "São Paulo."
           },
           {
               "value": "C",
               "description": "Vitória."
           }
       ]
   },
   {
       "title": "Qual é o país número 1 em reciclagem de alumínio?",
       "right_answer": "A",
       "answers": [
           {
               "value": "A",
               "description": "Brasil."
           },
           {
               "value": "B",
               "description": "Estados Unidos."
           },
           {
               "value": "C",
               "description": "Itália."
           }
       ]
   },
   {
       "title": "Que tipo de material gera mais resíduos no Brasil, com 52%?",
       "right_answer": "A",
       "answers": [
           {
               "value": "A",
               "description": "Matéria orgânica."
           },
           {
               "value": "B",
               "description": "Papel."
           },
           {
               "value": "C",
               "description": "Plástico."
           }
       ]
   },
   {
       "title": "Quais dos materiais abaixo podem gerar algum tipo de combustível?",
       "right_answer": "B",
       "answers": [
           {
               "value": "A",
               "description": "Óleo e metal."
           },
           {
               "value": "B",
               "description": "Plástico e óleo de cozinha."
           },
           {
               "value": "C",
               "description": "Apenas papel."
           }
       ]
   },
   
]

"""
   No looping vamos fazer a pergunta, aguardar o input do usuarios
   conferir se a resposta esta certa ou nao e anotar o score.
"""
print("# PERGUNTAS SOBRE COLETA SELETIVA #\n\n")

#Primeiro looping para obter as perguntas
for pergunta in lista_de_perguntas:
   print("Pergunta) %s \n\n" % pergunta['title'])
   
   #Segundo looping para obter as respostas
   for resposta in pergunta['answers']:
       print( "%s) %s\n" % (resposta['value'], resposta['description']) )
       
   # para obter o que o usuario escreve, use o input.
   answer_selected = input("\nResposta: ")
   
   # Isso eé uma condição. Se a resposta selecionada e a certa, aumenta o ponto, se nao, subtrai.
   if answer_selected.lower() == pergunta['right_answer'].lower(): #.lower() para forcar tudo letra minuscula
       SCORE = SCORE + 1 # ou SCORE += 1 (resposta certa, aumentar pontos)
   
if SCORE >=7:
    print('\033[32m'+'MUITO BOM, VOCÊ PASSOU !'+'\033[0;0m')
else:
    print ('\033[31m'+'VOCÊ FOI RUIM, VAMOS FAZER DNV ?!'+'\033[0;0m')
       
print("Perguntas finalizadas. Sua pontuação é: %s" % SCORE)