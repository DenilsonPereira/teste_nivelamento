from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

try:
    df = pd.read_csv(r'D:/teste_de_nivelamento/Teste_Api/backend/Relatorio_cadop.csv', encoding='utf-8', sep=';')
    for col in ['Razao_Social', 'Nome_Fantasia', 'CNPJ', 'Registro_ANS']:
        df[col] = df[col].fillna('').astype(str)
except FileNotFoundError:
    print("Erro: O arquivo 'Relatorio_cadop.csv' não foi encontrado no diretório atual.")
    df = pd.DataFrame()
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")
    df = pd.DataFrame()

@app.route('/api/search', methods=['GET'])
def search_operadoras():
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify({'results': df.to_dict('records')[:10]})
    
    mask = (
        df['Razao_Social'].str.lower().str.contains(query, na=False) |
        df['Nome_Fantasia'].str.lower().str.contains(query, na=False) |
        df['CNPJ'].str.contains(query, na=False) |
        df['Registro_ANS'].str.contains(query, na=False)
    )
    
    results = df[mask].fillna('Não informado').sort_values('Razao_Social').to_dict('records')
    return jsonify({'results': results[:20]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)