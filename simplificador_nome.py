def simplificador_nome(nome):

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
    