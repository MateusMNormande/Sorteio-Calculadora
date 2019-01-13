from random import shuffle

f_1 = ["Soma", "Subtração", "Multiplicação", "Divisão", "Exponencial"]
#funções que não precisam de import

f_2 = ["Log", "Seno", "Cosseno", "Tangente",
       "Arco-seno", "Arco-cosseno", "Arco-tangente"]
#funções que precisam de import

f_3 = ["Secante", "Cossecante", "Cotangente",
       "Arco-secante", "Arco-cossecante", "Arco-cotangente"]
#funções que precisam de import e manipulação algébrica

functions = []

turma = open('turma.txt','r')
n_alunos = len(turma.readlines())

i = 0
while i < n_alunos:
    shuffle(f_1)
    shuffle(f_2)
    shuffle(f_3)
    a = f_1[0], f_2[0], f_3[0]
    if a in functions:
        pass
    else:
        functions.append(a)
        i+=1
