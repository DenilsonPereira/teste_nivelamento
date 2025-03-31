SELECT 
    o.razao_social,
    SUM(d.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras_ativas o ON d.reg_ans = o.registro_ans
WHERE 
    d.data BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY 
    o.razao_social
ORDER BY 
    total_despesas DESC
LIMIT 10;