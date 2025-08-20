from controllers.livro_controller import LivroController

def main():
    db_config = {
        "dbname": "mvc_3a",
        "user": "postgres",
        "password": "wcc@2024",
        "host": "localhost",
        "port": "5432"
    }

    livro_controller = LivroController(db_config)

    # Exemplo de uso
    livro_controller.adiciona_livro(1, "1984", "George Orwell ", 1949, "1234567890123")
    livro_controller.adiciona_livro(2, "It a Coisa", "Sthephen King", 1932, "1234567890124")
    livro_controller.adiciona_livro(3, "O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "1234567890125")

if __name__ == "__main__":
    main()
