CREATE TABLE operadoras_ativas (
    registro_ans VARCHAR(10) PRIMARY KEY,
    cnpj VARCHAR(14) NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(8),
    ddd VARCHAR(2),
    telefone VARCHAR(20),
    fax VARCHAR(15),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    regiao_comercializacao INTEGER,
    data_registro_ans DATE
);

CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    data DATE,
    reg_ans VARCHAR(6),
    cd_conta_contabil VARCHAR(20),
    descricao VARCHAR(255),
    vl_saldo_inicial NUMERIC(15,2),
    vl_saldo_final NUMERIC(15,2)
);