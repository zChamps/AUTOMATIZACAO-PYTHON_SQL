def matricula_foto():

    # Entra no sistema e verifica os chamados de crachá em aberto, seleciona esses chamados e localiza a foto e matricula do colaborador, realiza o tratamento completo da imagem e salva na pasta, de forma automática.
    # Enter the system and check open badge tickets, select these tickets and locate the employee's photo and registration number, complete the image processing and save it in the folder, automatically.


    import requests
    import re
    from bs4 import BeautifulSoup
    import shutil
    import os
    from urllib.parse import urljoin
    from PIL import Image
    matriculas1 = []

    caminho_arquivo = r"caminho arquivo"

    with open(caminho_arquivo, "r") as arquivo:
        for i in arquivo:

    # Faz a requisição para obter o conteúdo HTML da página
            requisitar = requests.get(i)
            html = requisitar.text

            # Cria um objeto BeautifulSoup para analisar o HTML
            soup = BeautifulSoup(html, 'html.parser')


            # Encontra todos os textos na página
            textos = soup.get_text()

            # Define o padrão usando uma expressão regular
            padrao = r"\w+ \((\d+)\)"

            # Procura o padrão na página
            matriculas = re.findall(padrao, textos)
            

            # Verifica se o padrão foi encontrado
            if matriculas:
                for matricula in matriculas:
                    if len (matricula) > 5:
                        matriculas1.append(matricula)
                        matriculas_foto = matricula

        ##############################################################################################################



            # Faz o download do conteúdo HTML da página
            response = requests.get(i)
            html_content = response.text
            html_content = response.text

            # Cria um objeto BeautifulSoup para analisar o HTML
            soup = BeautifulSoup(html_content, 'html.parser')

            # Encontra todas as tags de imagem (tags <img>) na página
            image_tags = soup.find_all('img')

            # Diretório de destino para salvar as imagens
            destination_directory = r'Caminho arquivo'

            # Verifica se o diretório de destino existe, caso contrário, cria-o
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)

            # Loop pelas tags de imagem encontradas
            for img in image_tags:
                # Obtém o URL da imagem
                image_url = img['src']
                
                if image_url.split('/')[-1] != 'formulario_cracha.png' and image_url.split('/')[-1] != 'serval_50.png':
                    # Converte URL relativa em URL absoluta
                    absolute_url = urljoin(i, image_url)
                    
                    # Faz o download da imagem
                    response = requests.get(absolute_url, stream=True)
                    
                    # Verifica se o download foi bem-sucedido
                    if response.status_code == 200:
                        # Cria o caminho completo do arquivo de destino
                        foto_final = matriculas_foto[2:]
                        filename = foto_final + ".jpg"
                        destination_path = os.path.join(destination_directory, filename)
                        
                        # Salva a imagem no diretório de destino
                        with open(destination_path, 'wb') as out_file:
                            response.raw.decode_content = True
                            shutil.copyfileobj(response.raw, out_file)
                        
                        imagem_original =  Image.open(destination_path)
                        imagem = imagem_original.convert("RGB")
                        largura_cm = 29   
                        altura_cm = 42

                        # Converte as dimensões em centímetros para pixels
                        PPI = imagem.info.get('dpi', (72, 72))[0]  # Obtém a resolução da imagem em pixels por polegada (horizontal)
                        largura_px = int(largura_cm * PPI / 2.54)
                        altura_px = int(altura_cm * PPI / 2.54)

                        # Redimensiona a imagem
                        imagem_redimensionada = imagem.resize((largura_px, altura_px), resample=Image.LANCZOS)
                        # imagem_redimensionada = imagem.resize((largura_px, altura_px))
                        caminho_salvar = f"caminho arquivo\\{filename}"
                        # Salva a imagem redimensionada
                        imagem_redimensionada.save(caminho_salvar)
                        
                    else:
                        print('Falha ao fazer o download da imagem:', image_url)


    with open("matriculas.txt", "w") as arquivo:
        for i in matriculas1:
            arquivo.write(i + "\n")
    print("Processo concluido com sucesso!")






if __name__ == "__main__":
    matricula_foto()