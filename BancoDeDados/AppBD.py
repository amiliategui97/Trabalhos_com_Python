#Classe para operações CRUD.
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
    
#Seleção de dados   
    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Selecionando todo os produtos")
            sql_select_query = """SELECT * FROM public."produto" """

            cursor.execute(sql_select_query)
            registros = cursor.fetchall() 
            print(registros)

        except (Exception, psycopg2.Error) as error:
            print("Error in select operation", error)

        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
        return registros

#Inserção de dados.

    def inserirDados(self, codigo, nome, preco):
       try:
           self.abrirConexao()
           cursor = self.connection.cursor()
           postgres_insert_query = """INSERT INTO public."produto" 
           ("codigo", "nome", "preco",) VALUES (%s,%s,%s)"""
           record_to_insert =(codigo,nome,preco)
           cursor.execute(postgres_insert_query, record_to_insert)
           self.connection.commit()
           count = cursor.rowccount
           print(count, "Registro inserido com sucesso na tabela Produto")
       except (Exception, psycopg2.Error) as error:
           if(self.connection):
               print("Falha ao inserir registro na tabela Produto", error)
       finally:
           if(self.connection):
               cursor.close()
               self.connection.close()
               print("A conexão com o PostgreSQL foi fechada.")
           
#Atualização dos dados.

    def atualizarDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Registro antes da atualização")
            sql_select_query = """SELECT * FROM public."produto" WHERE "codigo" = %s"""
            cursor.execute(sql_select_query, (codigo))
            record = cursor.fetchone()
            print(record)
            sql_select_query = """UPDATE public."Produto" set "nome" = %s, "preco" = %s WHERE "codigo" = %s"""
            cursor.execute(sql_select_query, (nome, preco, codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso!")
            print("Registro depois da atualização")
            sql_select_query = """SELECT * FROM public."produto" WHERE "codigo" = %s"""
            cursor.execute(sql_select_query, (codigo))
            record = cursor.fetchone()
            print(record)
        except (Exception, psycopg2.Error) as error:
            print("Erro na atualização", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com PostgreSQL foi fechada.")

# Exclusão de dados.

    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_delete_query = """DELETE * FROM public."produto" WHERE "codigo" = %s"""
            cursor.execute(sql_delete_query, (codigo))

            self.connection.coomit()
            count = cursor.rowcount
            print(count, "Registro escluído com sucesso!")
        except (Exception, psycopg2.Error) as error:
            print("Erro na exclusão", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")