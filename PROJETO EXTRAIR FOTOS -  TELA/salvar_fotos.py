import requests
from PIL import Image
from io import BytesIO

# Realiza a edição e formatação completa da foto.

# Performs complete editing and formatting of the photo.

def salvar_imagem_do_link(url, nome_arquivo):
    nome_arquivo_final = f"{nome_arquivo}.jpg"
    response = requests.get(url)
    if response.status_code == 200:
        imagem_original = Image.open(BytesIO(response.content))

        imagem = imagem_original.convert("RGB")
        largura_cm = 29   
        altura_cm = 42

        PPI = imagem.info.get('dpi', (72, 72))[0]
        largura_px = int(largura_cm * PPI / 2.54)
        altura_px = int(altura_cm * PPI / 2.54)

        imagem_redimensionada = imagem.resize((largura_px, altura_px), resample=Image.LANCZOS)
        caminho_salvar = f"caminho_do_arquivo\\{nome_arquivo_final}"
        imagem_redimensionada.save(caminho_salvar)


        print(f'Imagem salva como {nome_arquivo}')
    else:
        print('Não foi possível baixar a imagem.')


