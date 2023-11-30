import pyodbc

# Verifica a existencia de crachás em aberto no sistema e enumera cada um, caso tenha.

# Check the existence of open badges in the system and list each one, if any.

server = '?'
database = '?'
username = '?'
password = '?'

conexao_BD = (
    f'DRIVER={{?}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
)

connection = pyodbc.connect(conexao_BD)

cursor = connection.cursor()


query_limpeza = "Codigo SQL"

cursor.execute(query_limpeza)
dados = cursor.fetchall()
cursor.close()

print("CRACHÁS - LIMPEZA EM ABERTO:")
for row in dados:
    for i in row:
        print(i)

print("CRACHÁS - LIMPEZA EM ABERTO:")
for contador, row in enumerate(dados, start=1):
    for i in row:
        print(f"{contador} - {i}")


