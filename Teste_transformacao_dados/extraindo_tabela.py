import pdfplumber
import pandas as pd
import zipfile
import os

pdf_path = "C:/Users/Denilson/Desktop/teste_de_nivelamento/Teste_web_scraping/Anexos/Anexo I.pdf"
csv_path = "C:/Users/Denilson/Desktop/teste_de_nivelamento/Teste_web_scraping/Anexos/Anexo I.csv"

data = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            data.extend(table)

df = pd.DataFrame(data)

df = df.replace("OD", "Seg. Odontológica")
df = df.replace("AMB", "Seg. Ambulatorial")
    
df.to_csv(csv_path, index=False, header=False, sep=";", encoding="utf-8-sig")

zip_name = "C:/Users/Denilson/Desktop/teste_de_nivelamento/Teste_transformacao_dados/Teste_Denilson_da_Silva_Pereira.zip"
with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_path, arcname="Anexo I.csv")
    os.remove(csv_path)

print(f"Arquivo salvo em: {csv_path}")
