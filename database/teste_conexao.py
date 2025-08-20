import psycopg2

try:
    conn = psycopg2.connect(
        dbname="mvc_3a",
        user="postgres",
        password="wcc@2023",
        host="localhost",
        port="5432"
    )
    print("Conexão bem-sucedida")
except psycopg2.Error as e:
    print("Erro ao conectar ao banco de dados")
    print(e)