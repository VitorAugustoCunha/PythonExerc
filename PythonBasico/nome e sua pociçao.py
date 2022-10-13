aluno=[]
cont=0
quantidade=int(input('digite a quandidade de alunos:'))
for loop in range(quantidade):
    aluno.append(str(input('digite o nome dos alunos')))
    cont+=1
for liip in range(quantidade):
    print (aluno[liip],liip)
