#coding: utf-8
lines = 4
columns = 8
pivotColumn = 0
pivotRow = 0

#Matriz que representa a tabela
mat = [[1,1,1,4,1,0,0,250], 
       [0,1,1,2,0,1,0,600],
       [3,2,4,0,0,0,1,500],
       [-100,-80,-120,-20,0,0,0,0]]

bv = ["x5","x6","x7","Z"]
nv = ["x1","x2","x3","x4","x5","x6","x7","B"]

#Encontra a coluna pivo
def findPivotColumn():
    #Pega a ulitma linha da matriz e assume que o menor valor está na posição 0.
    lastLine = mat[lines - 1]
    leastValue = lastLine[0]

    column = 0
    #Problema de maximização, pegamos o valor mais negativo.
    for i in range(columns):
        if lastLine[i] <= leastValue:
            leastValue = lastLine[i]
            column = i 
    return column

#Multiplicaa linha pivo pelo valor necessário para tornar o valor 1.
def normalizeLine(pivotRow, pivotColumn):
    matValue = mat[pivotRow][pivotColumn]
    if matValue > 0:
        multiplier = matValue ** -1
    else:
        multiplier = 0
    for i in range(columns):
        mat[pivotRow][i] = mat[pivotRow][i] * multiplier

#Mostra a matriz.
def showMatrix():
    for i in range(lines):
        print mat[i]

#Realiza as modificações na matriz.
def applyChanges(pivotRow,pivotColumn):
    for i in range(lines):
        if i != pivotRow:
            value = mat[i][pivotColumn]
            if value != 0:
                multiplier = value * -1
                #Realiza a soma de cada linha que o valor abaixo ou acima do pivo seja diferente de 0
                sumLines(multiplier, i, pivotRow)

#Realiza a soma da linha pivo multiplicada com a linha desejada.
def sumLines(multiplier, currentLine, pivotRow):
    for i in range(columns):
        mat[currentLine][i] = mat[currentLine][i] + (mat[pivotRow][i] * multiplier)

#Verifica se existem só valores positivos ou zeros
def evaluateMatrix():
    for i in range(columns):
        if mat[lines - 1][i] < 0:
            return False
    return True

#Troca as variáveis básicas e as variáveis normais de posição 
def changeVarPos(pivotRow, pivotColumn):
    bv[pivotRow] = nv[pivotColumn]

#Mostra os valores das variáveis que sobraram no vetor bv
def showResults():
    for i in range(lines):
        print bv[i] + ": " + str(mat[i][columns - 1]) 

#Encontra a linha pivo
def findPivotRow(pivotColumn):
    #Procura pela primeira linha que o divisor seja maior que 0 (Para que não ocorra divisão por 0).
    firstPos = 0
    for i in range(lines - 1):
        if mat[2][pivotColumn] > 0:
            firstPos = i
    
    divid = mat[firstPos][columns - 1]
    divis = mat[firstPos][pivotColumn]
    leastValue = divid / divis
    row = firstPos
    print str(divid) + "/" + str(divis) + " = " + str(leastValue)
    #Encontra o menor resultado dividindo o valor da coluna B pelo valor da coluna pivo para cada linha.
    for i in range(lines - 1):
        if i != firstPos:
            divid = mat[i][columns - 1]
            divis = mat[i][pivotColumn]
            if divis > 0:
                result = divid / divis
                print str(divid) + "/" + str(divis) + " = " + str(result)
                if result < leastValue:
                    leastValue = result
                    row = i
    return row

#Fluxo principal do programa
showMatrix()
while(not evaluateMatrix()):
    pivotColumn = findPivotColumn()
    print "Coluna Pivo: " + str(pivotColumn)
    pivotRow = findPivotRow(pivotColumn)
    print "Linha Pivo: " + str(pivotRow)
    print "Normalizando linha..."
    normalizeLine(pivotRow,pivotColumn)
    changeVarPos(pivotRow, pivotColumn)
    showMatrix()
    print "Aplicando Mudancas..."
    applyChanges(pivotRow,pivotColumn)
    showMatrix()
    print "\n"
showResults()
