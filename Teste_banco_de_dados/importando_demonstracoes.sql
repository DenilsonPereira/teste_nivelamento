DO $$
DECLARE
    arquivo TEXT;
    arquivos TEXT[] := ARRAY[
        'C:/Program Files/PostgreSQL/16/data/1T2023.csv',
        'C:/Program Files/PostgreSQL/16/data/2T2023.csv',
        'C:/Program Files/PostgreSQL/16/data/3T2023.csv',
        'C:/Program Files/PostgreSQL/16/data/4T2023.csv',
        'C:/Program Files/PostgreSQL/16/data/1T2024.csv',
        'C:/Program Files/PostgreSQL/16/data/2T2024.csv',
        'C:/Program Files/PostgreSQL/16/data/3T2024.csv',
        'C:/Program Files/PostgreSQL/16/data/4T2024.csv'
    ];
BEGIN
    CREATE TABLE temp_demonstracoes (
        data DATE,
        reg_ans VARCHAR(6),
        cd_conta_contabil VARCHAR(20),
        descricao VARCHAR(255),
        vl_saldo_inicial TEXT,
        vl_saldo_final TEXT
    );

    FOREACH arquivo IN ARRAY arquivos LOOP
        EXECUTE format('
            COPY temp_demonstracoes (
                data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, 
                vl_saldo_final
            )
            FROM %L
            DELIMITER '';'' 
            CSV HEADER 
            ENCODING ''UTF8''
        ', arquivo);
    END LOOP;

    INSERT INTO demonstracoes_contabeis (
        data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, 
        vl_saldo_final
    )
    SELECT 
        data,
        reg_ans,
        cd_conta_contabil,
        descricao,
        REPLACE(vl_saldo_inicial, ',', '.')::NUMERIC,
        REPLACE(vl_saldo_final, ',', '.')::NUMERIC
    FROM temp_demonstracoes;

    DROP TABLE temp_demonstracoes;
END $$;