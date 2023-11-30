import pyodbc

# Entra no banco de dados, verifica se existem chamados em aberto, caso tenha, seleciona o link da foto e a matricula do colaborador e exporta os dois dados para um arquivo separado, para agilizar
# o processo de salvar as fotos admissionais. Os crachás admissionais são feitos dessa forma pois as fotos são escaneadas na impressora, assim impossibilitando a identificação da foto no arquivo pelo Python.

# Enter the database, check if there are any open calls, if so, select the photo link and the employee's registration number and export both data to a separate file, to speed up
# the process of saving admission photos. Admission badges are made this way because the photos are scanned on the printer, making it impossible for Python to identify the photo in the file.




server = '?'
database = '?'
username = '?'
password = '?'

conn_str = (
    f'DRIVER={{?}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
)

connection = pyodbc.connect(conn_str)

cursor = connection.cursor()




codigo_sql = """Codigo SQL"""

cursor.execute(codigo_sql)

dados = cursor.fetchall()

cursor.close()
with open("Dados para Salvar fotos.txt", "w") as arquivo:
    for matricula, link in dados:
        matricula_sem_zero = matricula.lstrip("0")
        print(matricula_sem_zero)
        arquivo.write(f"{matricula_sem_zero} - {link}\n")

    print("Matriculas e links salvos com sucesso!")

