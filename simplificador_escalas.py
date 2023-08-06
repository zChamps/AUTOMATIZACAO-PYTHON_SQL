def escalas(escala):
    final_padrao = []


    while True:
        lista_escalas = []
        lista2 = []
        lista_padrao = []
        lista_teste_dia = []
        lista_escalas.append(escala)

        #escalas mais curtas
        if len(escala) > 27 and len(escala) < 34:
            for i in lista_escalas:
                for a in i:
                    lista2.append(a)
                valor_novo = "{}{}".format(lista2[:5], lista2[17:])
                lista_padrao.append(valor_novo)

            for i in lista_padrao:
                teste = "".join(i)
                teste1 = teste.replace("(", "").replace(")", "").replace("'", "").replace("\"", "").replace("[", "").replace("]", "").replace(",", "")
                if len(teste1) == 32:
                    string1 = teste1[:20].replace(" ", "")
                    string2 = teste1[-6:].replace(" ", "")
                elif len(teste1) == 36:
                    string1 = teste1[:20].replace(" ", "")
                    string2 = teste1[-9:].replace(" ", "")
                final = (f"{string1} | {string2}")
                
                final_padrao.append("".join(final))
            break


        #escala intermitente
        elif len(escala) > 49 and len(escala) < 53:
            for i in lista_escalas:
                for a in i:
                    lista2.append(a)
                lista_padrao.append(lista2[16:28])
                for i in lista_padrao:
                    teste = "".join(i)
                    teste1 = teste.replace("(", "").replace(")", "").replace("'", "").replace("\"", "").replace("[", "").replace("]", "").replace(",", "")
                final_padrao.append("".join(teste1))
            break


        #escalas 6x1 ou 5x2 maiores 
        elif len(escala) > 58 and len(escala) < 63:
                for i in lista_escalas[0]:
                    lista2.append(i)
                lista_teste_dia.append(lista2[58:])
                if ["S", "E", "X"] in lista_teste_dia:
                    valor_novo = "{}{}{}".format(lista2[:6], lista2[18:23], "   5x2")
                    lista_padrao.append(valor_novo)
                elif ["S", "A", "B"] in lista_teste_dia:
                    valor_novo = "{}{}{}".format(lista2[:6], lista2[18:23], "   6x1")
                    lista_padrao.append(valor_novo)

                for i in lista_padrao:
                    teste = "".join(i)
                    teste1 = teste.replace("(", "").replace(")", "").replace("'", "").replace("\"", "").replace("[", "").replace("]", "").replace(",", "")
                    
                string1 = teste1[:20].replace(" ", "")
                string2 = teste1[-6:].replace(" ", "")
                final = (f"{string1} | {string2}")
                final_padrao.append(final)
                break



    # escala 6x1 menor
        elif len(escala) > 47 and len(escala) < 53:
                for i in lista_escalas[0]:
                    lista2.append(i)
                valor_novo = "{}{}{}".format(lista2[:6], lista2[18:23], "   6x1")
                lista_padrao.append(valor_novo)

                for i in lista_padrao:
                    teste = "".join(i)
                    teste1 = teste.replace("(", "").replace(")", "").replace("'", "").replace("\"", "").replace("[", "").replace("]", "").replace(",", "")
                    
                string1 = teste1[:20].replace(" ", "")
                string2 = teste1[-6:].replace(" ", "")
                final = (f"{string1} | {string2}")
                final_padrao.append(final)
                break
        elif len(escala) > 10 and len(escala) < 20:
            return escala
            
    return final_padrao[0]



    

