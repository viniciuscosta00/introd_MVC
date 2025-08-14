import psycopg2

try:
    conn = psycopg2.connect(
        dbname="mvc_3a",
        user="postgres",
        passwoord="wcc@2024",
        host="localhost",
        port="5432"
    )
    print("Conexão bem-sucedida")
except psycopg2.Error as e:
    print("Erro ao conectar ao banco de dados")
    print(e)