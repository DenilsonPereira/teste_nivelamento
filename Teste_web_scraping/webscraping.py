import requests
import os
import zipfile

anexos = {
    "Anexo I.pdf": "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
    "Anexo II.pdf": "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"}

pasta_destino = "C:/Users/Denilson/Downloads/temps_pdfs"
os.makedirs(pasta_destino, exist_ok=True)

zip_path = "C:/Users/Denilson/Desktop/teste_de_nivelamento/Teste_web_scraping/Anexos.zip"

arquivos_baixados = []

for nome_anexo, url in anexos.items():
    caminho = os.path.join(pasta_destino, nome_anexo)
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        with open(caminho, "wb") as file:
            file.write(resposta.content)
        arquivos_baixados.append(caminho)
        print(f"Download concluído: {caminho}")
    else:
        print(f"Erro ao baixar {nome_anexo}: {resposta.status_code}")
    
with zipfile.ZipFile(zip_path, "w") as zipf:
    for arquivo in arquivos_baixados:
        zipf.write(arquivo, os.path.basename(arquivo))
        
for arquivo in arquivos_baixados:
    os.remove(arquivo)
os.rmdir(pasta_destino)

print("Download completo!")