import pyodbc
from salvar_fotos import salvar_imagem_do_link

# Separa os crachás em aberto de segunda via, seleciona matricula e foto deles. Após isso, repassa esses dados para o a função criada detro do arquivo "salvar_fotos.py" para de fato realizar o 
# tratamento da imagem (selecionar, editar e salvar a foto).

# Separate open duplicate badges, select their registration number and photo. After that, it passes this data to the function created within the file "salvar_fotos.py" to actually 
# process the image (select, edit and save the photo).

listar_matriculas_salvas = []
listar_matriculas_PDF = []
todas_as_matriculas = []


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


codigo_sql = """Codigo SQL"""

cursor.execute(codigo_sql)

for matricula, link in cursor.fetchall():

    if matricula is None or link is None:
        continue
    todas_as_matriculas.append(matricula)
    if link[-3:] not in {"jpg", "png"} and link[-4:] not in {"jpeg"}:
        with open("Arquivos PDF.txt", "a") as arquivo:
            arquivo.write(f"{matricula} - {link}\n\n")
        listar_matriculas_PDF.append(matricula)
        continue
    matricula_sem_zeros = matricula.lstrip("0")
    try:
        salvar_imagem_do_link(link, matricula_sem_zeros)
    except ValueError:
        continue
    listar_matriculas_salvas.append(matricula)


cursor.close()

print("TODAS AS MATRICULAS:")
for i in todas_as_matriculas:
    print(i)

print()

print("FOTOS SALVAS COM SUCESSO:")
for i in listar_matriculas_salvas:
    print(i)

print()

print("MATRICULAS NÃO SALVAS - PDF:")
for i in listar_matriculas_PDF:
    print(i)
