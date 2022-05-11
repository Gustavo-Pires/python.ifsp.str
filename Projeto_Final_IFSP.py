#Projeto Final IFSP SRT- Lancamento de notas 

#--------------------------------------------INICIO---------------------------------------------
print("Olá, bem vindo ao sitema de cadastro e tabelacao de notas.")
print("O programa ira pedir os dados do aluno, voce insira e aperte enter para avançar para os proximos dados.")
inicio = (int(input('Digite 0 para fazer cadastro, e 1 para ver os dados cadastrados ')))

#--------------------------------------VARIAVEIS INICIAIS--------------------------------------
nomes = []
notas = []
sexo = []
a = [] 
sexo_mas = [] 
sexo_fem = [] 
fem_apr = [] 
fem_exa = [] 
fem_rep = [] 
mas_apr = [] 
mas_exa = [] 
mas_rep = [] 

#-------------------------------------------LANCAMENTO DE NOTAS-------------------------------------------
while (inicio == 0):
    print("Vamos ao cadastro")
    nomes.append(str(input('Digite o nome do(a) aluno(a): ')))
    sexo.append(str(input('Digite o sexo do(a) aluno- M para masculino e F para femino:'[-1])))
    if input == 'M':
        notas.append(float(input(input("Digite aqui a 1º nota do(a)" +(nomes [-1]) + " COM DECIMAL "))))
        if (notas[-1]) >10:
            print('nota maxima permitia é 10')
        elif (notas[-1]) <0:
            print ('nota minima permitida é 0')    
        notas.append(float(input(input("Digite aqui a 2º nota do(a)" +(nomes [-1]) + " COM DECIMAL "))))
        if (notas[-1]) >10:
            print('nota maxima permitia é 10')
        elif (notas[-1]) <0:
            print ('nota minima permitida é 0')    
        notas.append(float(input(input("Digite aqui a 3º nota do(a)" +(nomes [-1]) + " COM DECIMAL "))))
        if (notas[-1]) >10:
            print('nota maxima permitia é 10')
        elif (notas[-1]) <0:
            print ('nota minima permitida é 0')   
        media = ((notas[-1] + notas[-2] + notas[-3])/3)
        if media >=7:
            mas_apr = +(media[-1])
        elif media >=4 <=6:
           mas_exa = +(media[-1])
        elif media <4:
            mas_rep = +(media[-1])    
    else:
        notas.append(float(input(input("Digite aqui a 1º nota do(a)" +(nomes [-1]) + " COM DECIMAL")))) 
        if (notas[-1] >10):
            print('nota maxima permitia é 10')
        elif (notas[-1]) <0:
            print ('nota minima permitida é 0')    
        notas.append(float(input(input("Digite aqui a 2º nota do(a)" +(nomes [-1]) + " COM DECIMAL"))))
        if (notas[-1]) >10:
            print('nota maxima permitia é 10')
        elif (notas[-1]) <0:
            print ('nota minima permitida é 0')   
        notas.append(float(input(input("Digite aqui a 3º nota do(a)" +(nomes [-1]) + " COM DECIMAL"))))
        if (notas[-1]) >10:
            print('nota maxima permitia é 10')
        elif (notas[-1]) <0:
            print ('nota minima permitida é 0')   
        media = ((notas[-1] + notas[-2] + notas[-3])/3)
        if media >=7:
            fem_apr = +(media[-1])
        elif media >=4 <=6:
           fem_exa = +(media[-1])
        elif media <4:
            fem_rep = +(media[-1])

    #-------------------------------------------SOMATORIA-------------------------------------------
    
else :
    aprovados = [((fem_apr) + (mas_apr)) ]
    exames = [fem_exa + mas_exa]
    reprovados = [fem_rep + mas_rep]
    total_alunos = ((len(aprovados) + len(exames) + len(reprovados)))#total de alunos cadaintados
    print("O total de alunos é de " + str(total_alunos))
    
    #-------------------------------------------PORCENTAGEM-------------------------------------------
    #print('A quantidade percentual de alunos aprovados é:'+ ((len(aprovados) * 100) // (len(aprovados) + len(exames) + len(reprovados)))) #quantidade percentual de alunos aprovados 
    #print('A quantidade percentual de alunos em exame é:' + ((len(exames) * 100) // (len(aprovados) + len(exames) + len(reprovados)))) #quantidade percentual de alunos em exame
    #print('A quantidade percentual de alunos reprovados é:' + ((len(reprovados) * 100) // (len(aprovados) + len(exames) + len(reprovados))))#quantidade percentual de alunos reprovados 
    print('A quantidade percentual de alunos aprovados é:'+ ((len(aprovados)) * 100) // (len(total_alunos))) #quantidade percentual de alunos aprovados 
    #erro na linha 87 object of type 'int' has no len()
    print('A quantidade percentual de alunos em exame é:' + ((len(exames) * 100) // (len(total_alunos)))) #quantidade percentual de alunos em exame
    print('A quantidade percentual de alunos reprovados é:' + ((len(reprovados) * 100) // (len(total_alunos))))#quantidade percentual de alunos reprovados 

    #--------------------------------------------Valores Absolutos-------------------------------------------
    print("quantidade de pessoas do sexo feminimo aprovadas é: "(len(fem_apr)) )#quantidade de pessoas do sexo feminino aprovadas
    print("quantidade de pessoas do sexo feminimo aprovadas é: "(len(mas_apr)) )#quantidade de pessoas do sexo masculinos aprovados

    print("quantidade de pessoas do sexo feminimo aprovadas é: "(len(fem_exa))) #quantidade de pessoas do sexo feminimo de exame
    print("quantidade de pessoas do sexo feminimo aprovadas é: "(len(mas_exa)))#quantidade de pessoas do sexo masculino de Exame

    print("quantidade de pessoas do sexo feminimo aprovadas é: "(len(fem_rep)))#quantidade de pessoas do sexo feminino reprovadas
    print("quantidade de pessoas do sexo feminimo aprovadas é: "(len(mas_rep)))#quantidade de pessoas do sexo masculino Reprovados
    
    #-------------------------------------------Calculo Extra-------------------------------------------
    print("A media da sala foi de " (sum(media)/(len(media)))) #media total da sala 
    #print("A media dos aprovados foi de " ((sum(fem_apr)+ sum(mas_apr))/((len(fem_apr)+ len(mas_apr))))) #media dos aprovados
    #print("A media dos em exame foi de " ((sum(fem_exa)+ sum(mas_exa))/((len(fem_exa)+ len(mas_exa))))) # media dos em exame 
    #print("A media dos reprovados foi de " ((sum(fem_rep)+ sum(mas_apr))/((len(fem_rep)+ len(mas_rep))))) # media dos reprovados
    print("A media dos aprovados foi de " ((sum(aprovados))/((len(aprovados))))) # media dos aprovados
    print("A media dos em exame foi de " ((sum(exames))/((len(exames))))) # media dos em exame 
    print("A media dos reprovados foi de " ((sum(reprovados))/(len(reprovados)))) # media dos reprovados
    
    
