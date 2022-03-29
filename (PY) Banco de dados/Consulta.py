import mysql.connector

class Consulta:

    def consulta_todos():
        connection = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='1234')
        if connection.is_connected():
            db_info = connection.get_server_info()
            print('\nConexao realizada com sucesso! Versao de servidor {}'.format(db_info))
        
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM veiculos;")
        linhas = cursor.fetchall()   
        print (cursor.rowcount, "Registros retornados!")

        for linha in linhas:
            print("\nID: ", linha[0])
            print("Fabricante: ", linha[1])
            print("Modelo: ", linha[2])
            print("Ano: ", linha[3])
            print("Cor: ", linha[4])

        if connection.is_connected():
            cursor.close()
            connection.close()
            print('\nConexao encerrada. Ate a proxima!\n')

    def consulta_um(id):
        connection = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='1234')
        if connection.is_connected():
            db_info = connection.get_server_info()
            print('\nConexao realizada com sucesso! Versao de servidor {}'.format(db_info))

            cursor = connection.cursor()
            cursor.execute("SELECT * FROM veiculos WHERE id={};".format(id))
            linha = cursor.fetchone()
            print(linha)