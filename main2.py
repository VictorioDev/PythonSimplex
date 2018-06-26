#coding: utf-8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Tela(BoxLayout):
    lines = 4
    columns = 8
    pivotColumn = 0
    pivotRow = 0

    def calc(self):
        for i in range(self.columns):
            self.matriz[self.lines - 1][i] = self.matriz[self.lines - 1][i] * -1 
        #Fluxo principal do programa
        self.showMatrix()
        while(not self.evaluateMatrix()):
            pivotColumn = self.findPivotColumn()
            print "Coluna Pivo: " + str(pivotColumn)
            pivotRow = self.findPivotRow(pivotColumn)
            print "Linha Pivo: " + str(pivotRow)
            print "Normalizando linha..."
            self.normalizeLine(pivotRow,pivotColumn)
            self.changeVarPos(pivotRow, pivotColumn)
            self.showMatrix()
            print "Aplicando Mudancas..."
            self.applyChanges(pivotRow,pivotColumn)
            self.showMatrix()
            print "\n"
        self.showResults()


    def getInputs(self):
        self.matriz = [
            [   int(self.ids.tabuaEscrivaninha.text),
                int(self.ids.tabuaMesa.text),
                int(self.ids.tabuaArmario.text),
                int(self.ids.tabuaPrateleira.text),
                1,0,0,
                int(self.ids.tabuaDisponibilidade.text)
            ],
            [
                int(self.ids.pranchaEscrivaninha.text),
                int(self.ids.pranchaMesa.text),
                int(self.ids.pranchaArmario.text),
                int(self.ids.pranchaPrateleira.text),
                0,1,0,
                int(self.ids.pranchaDisponibilidade.text)
            ],
            [
                int(self.ids.painelEscrivaninha.text),
                int(self.ids.painelMesa.text),
                int(self.ids.painelArmario.text),
                int(self.ids.painelPrateleira.text),
                0,0,1,
                int(self.ids.painelDisponibilidade.text)
            ],
            [
                int(self.ids.lucroEscrivaninha.text),
                int(self.ids.lucroMesa.text),
                int(self.ids.lucroArmario.text),
                int(self.ids.lucroPrateleira.text),
                0,0,0,0
            ]
        ]
        self.calc()

    #Encontra a coluna pivo
def findPivotColumn(self):
    #Pega a ulitma linha da self.matrizriz e assume que o menor valor está na posição 0.
    lastLine = self.matriz[self.lines - 1]
    leastValue = lastLine[0]

    column = 0
    #Problema de maximização, pegamos o valor mais negativo.
    for i in range(self.columns, self):
        if lastLine[i] <= leastValue:
            leastValue = lastLine[i]
            column = i 
    return column

#Multiplicaa linha pivo pelo valor necessário para tornar o valor 1.
def normalizeLine(pivotRow, pivotColumn, self):
    matrizValue = self.matriz[pivotRow][pivotColumn]
    if matrizValue > 0:
        multiplier = matrizValue ** -1
    else:
        multiplier = 0
    for i in range(self.columns):
        self.matriz[pivotRow][i] = self.matriz[pivotRow][i] * multiplier

#Mostra a self.matrizriz.
def showMatriz(self):
    for i in range(self.lines):
        print self.matriz[i]

#Realiza as modificações na self.matrizriz.
def applyChanges(pivotRow,pivotColumn, self):
    for i in range(self.lines):
        if i != pivotRow:
            value = self.matriz[i][pivotColumn]
            if value != 0:
                multiplier = value * -1
                #Realiza a soma de cada linha que o valor abaixo ou acima do pivo seja diferente de 0
                self.sumLines(multiplier, i, pivotRow)

#Realiza a soma da linha pivo multiplicada com a linha desejada.
def sumLines(multiplier, currentLine, pivotRow, self):
    for i in range(self.columns):
        self.matriz[currentLine][i] = self.matriz[currentLine][i] + (self.matriz[pivotRow][i] * multiplier)

#Verifica se existem só valores positivos ou zeros
def evaluateMatriz(self):
    for i in range(self.columns):
        if self.matriz[self.lines - 1][i] < 0:
            return False
    return True

#Troca as variáveis básicas e as variáveis normais de posição 
def changeVarPos(pivotRow, pivotColumn, self):
    self.bv[pivotRow] = self.nv[pivotColumn]

#Mostra os valores das variáveis que sobraram no vetor bv
def showResults(self):
    for i in range(self.lines):
        print self.bv[i] + ": " + str(self.matriz[i][self.columns - 1]) 

#Encontra a linha pivo
def findPivotRow(pivotColumn, self):
    #Procura pela primeira linha que o divisor seja maior que 0 (Para que não ocorra divisão por 0).
    firstPos = 0
    for i in range(self.lines - 1):
        if self.matriz[2][pivotColumn] > 0:
            firstPos = i
    
    divid = self.matriz[firstPos][self.columns - 1]
    divis = self.matriz[firstPos][self.pivotColumn]
    leastValue = divid / divis
    row = firstPos
    print str(divid) + "/" + str(divis) + " = " + str(leastValue)
    #Encontra o menor resultado dividindo o valor da coluna B pelo valor da coluna pivo para cada linha.
    for i in range(self.lines - 1):
        if i != firstPos:
            divid = self.matriz[i][self.columns - 1]
            divis = self.matriz[i][pivotColumn]
            if divis > 0:
                result = divid / divis
                print str(divid) + "/" + str(divis) + " = " + str(result)
                if result < leastValue:
                    leastValue = result
                    row = i
    return row

    
 
class Teste(App):
    def build(self):
        return Tela()

Teste().run()