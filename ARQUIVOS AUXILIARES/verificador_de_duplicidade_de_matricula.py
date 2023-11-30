
# Dentro dos chamados de crachás em aberto, verifica se existe algum chamado aberto que esteja duplicado e sinaliza caso tenha.

#Within the open badge calls, check if there is any request open that it is duplicated and flag if it is.

matriculas_geral = []
matriculas_repetidas = []

with open("matriculas.txt", "r") as mt:
    for i in mt:
        if i in matriculas_geral:
            matriculas_repetidas.append(i)
        else:
            matriculas_geral.append(i)

for i in matriculas_repetidas:
    print(i)