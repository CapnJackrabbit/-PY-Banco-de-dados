import mysql.connector, Consulta

class Apaga:
    def apaga_registro():
        connection = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='1234')
        if connection.is_connected():
            db_info = connection.get_server_info()
            print('\nConexao realizada com sucesso! Versao de servidor {}'.format(db_info))

            id=input('INFORME O ID DO VEICULO: ')
            Consulta.Consulta.consulta_um(id)
            
            resp = input('TEM CERTEZA QUE DESEJA EXCLUIR ESTE REGISTRO? (1-Sim / 2-Nao)')

            if resp == '1':
                cursor = connection.cursor()
                cursor.execute("DELETE FROM veiculos WHERE id={};".format(id))
                connection.commit()
                print('REGISTRO EXCLUIDO')
            
            elif resp == '2':
                print('EXCLUSAO CANCELADA')

            else:
                print('OPCAO INVALIDA')