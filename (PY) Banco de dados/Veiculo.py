class Veiculo:
    def __init__(self, fabricante, modelo, ano, cor):
        self.set_dados(fabricante,modelo,ano,cor)


    def insere_dados(self):
        return ("INSERT INTO veiculos (Fabricante,Modelo,Ano,Cor) VALUES ('{}','{}','{}','{}');".format(self._fab,self._mod,self._ano,self._cor))


    def set_dados(self, fabricante, modelo, ano, cor):
        self._fab = fabricante
        self._mod = modelo
        self._ano = ano
        self._cor = cor
        




