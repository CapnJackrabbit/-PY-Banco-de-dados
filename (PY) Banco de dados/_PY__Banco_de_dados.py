import mysql.connector, Veiculo, Consulta, Cadastra, Apaga


while True:
    print('1 - CADASTRAR NOVO VEICULO\n')
    print('2 - CONSULTAR UM VEICULO POR ID\n')
    print('3 - ACESSAR TODOS OS REGISTROS\n')
    print('4 - EXCLUIR UM REGISTRO\n')
    print('5 - SAIR\n')
    opc = input('ESCOLHA UMA OPCAO: ')

    if opc == '1':
        Cadastra.Cadastra.cadastra_novo()

    elif opc == '2':
        id = input('INFORME O ID DO VEICULO: ')
        Consulta.Consulta.consulta_um(id)
        

    elif opc == '3':
        Consulta.Consulta.consulta_todos()
        

    elif opc == '4':
        Apaga.Apaga.apaga_registro()

    elif opc == '5':
        print('ATE A PROXIMA!')
        break





    #cursor.execute("INSERT INTO veiculos (Fabricante,Modelo,Ano,Cor) VALUES ('{}','{}','{}','{}');".format(fabricante,modelo,ano,cor))
    #command = ("INSERT INTO veiculos (fabricante,modelo,ano,cor) VALUES ('"+ fab +"','"+ mod +"','" + ano +"', '"+ cor +"');")