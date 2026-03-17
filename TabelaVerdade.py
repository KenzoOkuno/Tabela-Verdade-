import tkinter as tk
# Importa a biblioteca Tkinter com apelido 'tk' para criar interfaces gráficas

from itertools import product
# Importa 'product' do módulo itertools para gerar todas as combinações possíveis de True/False

# Lista de variáveis lógicas do usuário
variaveis = ['A', 'B', 'C']

# Função para calcular resultados de todas as operações lógicas
def calcular_resultados(valores):
    A, B, C = valores
    # Desempacota a lista de valores em A, B e C
    return {
        '¬A': not A,                 # Negação de A
        '¬B': not B,                 # Negação de B
        '¬C': not C,                 # Negação de C
        'A ∧ B ∧ C': A and B and C,  # Conjunção (AND) das três variáveis
        'A ∨ B ∨ C': A or B or C,    # Disjunção (OR) das três variáveis
        'A ⊕ B ⊕ C': (A != B) != C,  # XOR: True se número ímpar de True
        '↑(A,B,C)': not (A and B and C), # NAND: negação da conjunção
        '↓(A,B,C)': not (A or B or C),   # NOR: negação da disjunção
        'A ⇒ B': (not A) or B,       # Implicação A->B
        'B ⇒ C': (not B) or C,       # Implicação B->C
        'C ⇒ A': (not C) or A        # Implicação C->A
    }

# Função chamada quando um checkbox muda
def atualizar_linha(linha_index):
    # Pega os valores atuais de cada variável na linha correspondente
    valores = [vars_checkbox[var_name][linha_index].get() for var_name in variaveis]
    resultados = calcular_resultados(valores)
    # Atualiza cada Label da linha com os resultados calculados
    for op, label in labels_resultados[linha_index].items():
        label.config(text=str(resultados[op]))

# Criando a janela principal
root = tk.Tk()
root.title("Tabela Verdade Interativa (3 variáveis)")

# Gerando todas as combinações possíveis de True/False para as variáveis
combinacoes = list(product([True, False], repeat=len(variaveis)))

# Dicionários para armazenar os checkboxes e labels
vars_checkbox = {var: [] for var in variaveis}  # Guarda BooleanVars de cada checkbox
labels_resultados = []                           # Guarda Labels de cada operação por linha

# Cabeçalhos da tabela
tk.Label(root, text="Variáveis").grid(row=0, column=0, columnspan=len(variaveis), padx=10)
tk.Label(root, text="Operações").grid(row=0, column=len(variaveis)+1, columnspan=11, padx=10)

# Criando linhas da tabela para cada combinação
for i, valores in enumerate(combinacoes):
    linha_resultados = {}  # Guarda Labels desta linha
    
    # Criando checkboxes para cada variável
    for j, var_name in enumerate(variaveis):
        var = tk.BooleanVar(value=valores[j])  # BooleanVar inicializado com True/False
        vars_checkbox[var_name].append(var)    # Adiciona à lista do dicionário
        cb = tk.Checkbutton(root, variable=var, command=lambda idx=i: atualizar_linha(idx))
        # Cria o checkbox e associa a função que atualiza a linha
        cb.grid(row=i+1, column=j, padx=10, sticky='w')  # Posiciona com espaçamento e alinhamento à esquerda
     
    # Criando Labels para cada operação lógica
    resultados = calcular_resultados(valores)
    for k, op in enumerate(resultados):
        if i == 0:
            # Primeira linha: coloca cabeçalho com o nome da operação
            tk.Label(root, text=op).grid(row=0, column=len(variaveis)+1+k, padx=10, sticky='w')
        label = tk.Label(root, text=str(resultados[op]))
        label.grid(row=i+1, column=len(variaveis)+1+k, padx=10, sticky='w')  # Posiciona o Label
        linha_resultados[op] = label  # Guarda o Label no dicionário da linha
    
    labels_resultados.append(linha_resultados)  # Adiciona a linha à lista principal

# Executa o loop principal da janela Tkinter
root.mainloop()