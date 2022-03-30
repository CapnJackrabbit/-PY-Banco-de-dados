import mysql.connector,Veiculo

class Cadastra:
    def cadastra_novo():
        fabricante = input("Informe o fabricante: ")
        modelo = input("Informe o modelo: ")
        ano = input("Informe o ano : ")
        cor = input("Informe a cor: ")

        automovel = Veiculo.Veiculo(fabricante,modelo,ano,cor)

        connection = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='1234')
        if connection.is_connected():
            db_info = connection.get_server_info()
            print('\nConexao realizada com sucesso! Versao de servidor {}'.format(db_info))
        
        cursor = connection.cursor()
        cursor.execute('SELECT DATABASE();')
        linha = cursor.fetchone()
        print('Conectado ao banco de dados {}'.format(linha))
        cursor.execute(automovel.insere_dados())
        connection.commit()
        print (cursor.rowcount, "registro inserido!\n")

        if connection.is_connected():
            cursor.close()
            connection.close()
            print('\nConexao encerrada. Ate a proxima!\n')