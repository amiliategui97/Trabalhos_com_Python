import psycopg2

class AppBD:
    def __init__(self):
        print('Método Construtor')
    
    def abrirConexao(self):
        try:
            self.connection = psycopg2(user="postgres",
                                    passwoerd="senha123",
                                    host="localhost",
                                    port="5433",
                                    database="Empresa")
        except (Exception, psycopg2.Error) as error:
            if(self.connection):
                print("Falha ao se conectar ao Banco de Dados", error)
    