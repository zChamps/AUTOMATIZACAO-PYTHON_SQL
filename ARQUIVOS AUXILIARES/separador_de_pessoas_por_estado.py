import pyodbc

# Recebe as matriculas que estão no arquivo "matriculas.txt", faz uma pesquisa no banco de dados e interliga as tabelas com dados do funcionários e do posto de trabalho onde estão alocados.
# Assim seleciona o estado e divide dinamicamente todos os colaboradores pelo estado onde ele trabalha.

# It receives the registrations that are in the "matriculas.txt" file, searches the database and connects the tables with data on the employees and the work station where they are allocated.
# So select the stateand dynamically divides all employees by the state where they work.

server = '?'
database = '?'
username = '?'
password = '?'

conn_str = (
    f'DRIVER={{SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
)

connection = pyodbc.connect(conn_str)

cursor = connection.cursor()

matriculas = []
pessoa_estado = []
lista_de_listas = []

with open("matriculas.txt", "r") as mt:
    for i in mt:
        matriculas.append(i)

for i in matriculas:

    codigo_sql = f"""codigo SQL"""

    cursor.execute(codigo_sql)

    dados = cursor.fetchall()

    pessoa_estado.append(dados)

cursor.close()



for i in pessoa_estado:
        for a in i:
            lista_de_listas.append(a)


lista_ordenada = sorted(lista_de_listas, key=lambda x: x[1])



with open("Matriculas separadas por estado.txt", "w") as arquivo:
    for i in lista_ordenada:
            arquivo.write(f"{str(i)} \n")

with open("Matriculas separadas por estado.txt", "r") as arquivo:
    for i in arquivo:
        print(i[13:15])
        if i[13:15] == "BA":
            caminho_arquivo = f"./LOCALIDADES/BA.txt"
        elif i[13:15] == "PE":
            caminho_arquivo = f"./LOCALIDADES/PE.txt"
        elif i[13:15] == "AL":
            caminho_arquivo = f"./LOCALIDADES/AL.txt"
        elif i[13:15] == "CE":
            caminho_arquivo = f"./LOCALIDADES/CE.txt"
        elif i[13:15] == "MA":
            caminho_arquivo = f"./LOCALIDADES/MA.txt"
        elif i[13:15] == "PA":
            caminho_arquivo = f"./LOCALIDADES/PA.txt"
            print("Estou dentro do pa")
        elif i[13:15] == "PB":
            caminho_arquivo = f"./LOCALIDADES/PB.txt"
        elif i[13:15] == "PI":
            caminho_arquivo = f"./LOCALIDADES/PI.txt"
        elif i[13:15] == "RN":
            caminho_arquivo = f"./LOCALIDADES/RN.txt"
        elif i[13:15] == "SE":
            caminho_arquivo = f"./LOCALIDADES/SE.txt"
        elif i[13:15] == "SP":
            caminho_arquivo = f"./LOCALIDADES/SP.txt"
            
        with open(caminho_arquivo, "w") as arquivo:
            for i in lista_ordenada:
                    if i[1] == caminho_arquivo[14:16]:
                        arquivo.write(f"{str(i)} \n")



print("Matriculas e links salvos com sucesso!")

