import mysql.connector


def main():
    conexao = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='usuario',
        password='senhausuario',
        database='meubanco'
    )
    cursor = conexao.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100)
        )
    """)


    cursor.execute("INSERT INTO pessoas (nome) VALUES ('Maria')")
    cursor.execute("INSERT INTO pessoas (nome) VALUES ('João')")
    conexao.commit()


    cursor.execute("SELECT * FROM pessoas")
    for row in cursor.fetchall():
        print(row)


    cursor.close()
    conexao.close()


if __name__ == "__main__":
    main()
