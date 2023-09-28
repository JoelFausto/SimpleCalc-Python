# Importando a biblioteca de interface
from tkinter import *

# Variáveis de controle globais
op, n1, n2, res = 0, 0, 0, 0
cliqueNum1, cliqueNum2 = 0, 0

def operations(n):
    global n1, n2, res, cliqueNum1, cliqueNum2
    n1 = int(n1)
    n2 = int(n2)

    if n == 1: # SOMA
        res = n1 + n2
        cleanText()
        text_resp = Label(janela, text=res)
        text_resp.grid(column=1, row=0, padx=0, pady=0)
        cliqueNum1, cliqueNum2 = 0, 0
    elif n == 2: # SUBTRAÇÂO
        res = n1 - n2
        cleanText()
        text_resp = Label(janela, text=res)
        text_resp.grid(column=1, row=0, padx=0, pady=0)
        cliqueNum1, cliqueNum2 = 0, 0
    elif n == 3: # MULTIPLICAÇÃO
        res = n1 * n2
        cleanText()
        text_resp = Label(janela, text=res)
        text_resp.grid(column=1, row=0, padx=0, pady=0)
        cliqueNum1, cliqueNum2 = 0, 0
    elif n == 4: # DIVISÃO
        res = n1 / n2
        cleanText()
        text_resp = Label(janela, text=res)
        text_resp.grid(column=1, row=0, padx=0, pady=0)
        cliqueNum1, cliqueNum2 = 0, 0
    elif n == 5: # EXPONENCIAÇÂO
        res = n1 ** n2
        cleanText()
        text_resp = Label(janela, text=res)
        text_resp.grid(column=1, row=0, padx=0, pady=0)
        cliqueNum1, cliqueNum2 = 0, 0

def cleanText():
    text_resp = Label(janela, text='')
    text_resp.grid(column=1, row=0, padx=0, pady=0)

def clean(use):
    if use == True:
        cleanText()
        global op, n1, n2, res, cliqueNum1, cliqueNum2
        op, n1, n2, res, cliqueNum1, cliqueNum2 = 0, 0, 0, 0, 0, 0
        text_resp = Label(janela, text=res)
        text_resp.grid(column=1, row=0, padx=0, pady=0)

def buttonNum(nome, valor, col, line, x, y):
    def save():
        global n1, n2, op, cliqueNum1, cliqueNum2
        if cliqueNum1 == 0:
            n1 = valor
            cliqueNum1 += 1
            text_resp = Label(janela, text=n1)
            text_resp.grid(column=1, row=0, padx=0, pady=0)

        elif cliqueNum1 > 0 and op == 0:
            n1 = n1 + valor
            cliqueNum1 += 1
            cleanText()
            text_resp = Label(janela, text=n1)
            text_resp.grid(column=1, row=0, padx=0, pady=0)

        elif op != 0 and cliqueNum2 == 0:
            n2 = valor
            cliqueNum2 += 1
            cleanText()
            text_resp = Label(janela, text=n2)
            text_resp.grid(column=1, row=0, padx=0, pady=0)

        elif op != 0 and cliqueNum2 > 0:
            n2 = n2 + valor
            cliqueNum2 += 1
            cleanText()
            text_resp = Label(janela, text=n2)
            text_resp.grid(column=1, row=0, padx=0, pady=0)

    botao = Button(janela, text=nome, command=save)
    botao.grid(column=col, row=line, padx=x, pady=y)

def buttonOperation(nome, operacao, col, line, x, y):
    botao = Button(janela, text=nome, command=lambda: whatOp(operacao))
    botao.grid(column=col, row=line, padx=x, pady=y)

def buttonClean(nome, comando, col, line, x, y):
    botao = Button(janela, text=nome, command=lambda: clean(comando))
    botao.grid(column=col, row=line, padx=x, pady=y)

def buttonResult(nome, col, line, x, y):
    global op
    botao = Button(janela, text=nome, command=lambda: operations(op))
    botao.grid(column=col, row=line, padx=x, pady=y)

def whatOp(n):
    global op
    if n == "soma":
        op = 1
    elif n == "subt":
        op = 2
    elif n == "mult":
        op = 3
    elif n == "div":
        op = 4
    elif n == "exp":
        op = 5

# Inicia a interface
janela = Tk()

# Título da janela 
janela.title("CALCULADORA")

# Tamanho da janela
janela.geometry("300x245")

# Label de texto
text_result = Label(janela, text='RESULTADO: ')
text_result.grid(column=0, row=0, padx=10, pady=10)

# Botões números
buttonNum("1".center(7), '1', 2, 2, 5, 5)
buttonNum("2".center(7), '2', 3, 2, 5, 5)
buttonNum("3".center(7), '3', 4, 2, 5, 5)
buttonNum("4".center(7), '4', 2, 3, 5, 5)
buttonNum("5".center(7), '5', 3, 3, 5, 5)
buttonNum("6".center(7), '6', 4, 3, 5, 5)
buttonNum("7".center(7), '7', 2, 4, 5, 5)
buttonNum("8".center(7), '8', 3, 4, 5, 5)
buttonNum("9".center(7), '9', 4, 4, 5, 5)
buttonNum("0".center(7), '0', 3, 5, 5, 5)

# Botões livres
buttonNum("".center(8), '', 2, 5, 5, 5)
buttonNum("".center(8), '', 2, 1, 5, 5)
buttonNum("".center(8), '', 3, 1, 4, 5)

# Botões operações
buttonOperation("+".center(7), "soma", 1, 1, 0, 5)
buttonOperation("-".center(7), "subt", 1, 2, 0, 5)
buttonOperation("x".center(7), "mult", 1, 3, 0, 5)
buttonOperation("/".center(7), "div", 1, 4, 0, 5)
buttonOperation("*".center(7), "exp", 1, 5, 0, 5)
buttonResult("=".center(7), 4, 5, 5, 5)
buttonClean("C".center(7), True, 4, 1, 5, 5)

# Mantém a tela aberta
janela.mainloop()