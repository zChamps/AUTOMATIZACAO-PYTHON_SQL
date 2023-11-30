def simplificador_nome(nome):
    
    # Simplifica e trata o nome de cada colaborador para ser colocada no formato correto dentro da planilha dos crachás. Reduz o nome completo de cada um ao primeiro nome e ultimo sobrenome, exceto casos especificados abaixo.

    # Simplifies and edits the name of each employee to be placed in the correct format within the badge spreadsheet. Reduces each person's full name to their first name and last name, except in cases specified below.

    
    lista = [nome.split(" ")]

    verificacao = lista[0][0].upper() == "FRANCISCO" or lista[0][0].upper() == "JOSE" or lista[0][0].upper() == "JOAO" or lista[0][0].upper() == "ANTONIO"
    if verificacao is True:
           return nome
    if len(lista[0]) > 2 and len(lista[0]) < 4:

            
            lista[0].pop(1)
    elif len(lista[0]) > 3 and len(lista[0]) < 5:
                    
            lista[0].pop(1)
            lista[0].pop(1)
    elif len(lista[0]) > 4 and len(lista[0]) < 6:
            
            lista[0].pop(1)
            lista[0].pop(1)
            lista[0].pop(1)
    elif len(lista[0]) > 5 and len(lista[0]) < 7:
                        
            lista[0].pop(1)
            lista[0].pop(1)
            lista[0].pop(1)
            lista[0].pop(1)
    elif len(lista[0]) > 6 and len(lista[0]) < 8:
                        
            lista[0].pop(1)
            lista[0].pop(1)
            lista[0].pop(1)
            lista[0].pop(1)
            lista[0].pop(1)
    elif len(lista[0]) > 7 and len(lista[0]) < 9:
                        
            lista[0].pop(1)
            lista[0].pop(1)
            lista[0].pop(1)
            lista[0].pop(1)
            lista[0].pop(1)
            lista[0].pop(1)
    
    return " ".join(lista[0])
    