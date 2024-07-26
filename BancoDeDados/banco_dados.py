import psycopg2

# Criando Tabela
conn = psycopg2.connect(database = "Empresa", user = "postgres", password = "senha123", host = "localhost", port = "5433")
print("conexão com Banco de Dados aberta com sucesso!")

cur = conn.cursor()
cur.execute('''CREATE TABLE agenda(ID INT PRIMARY KEY NOT NULL,Nome TEXT NOT NULL,Telefone CHAR(12));''')
print("Tabela criada com sucesso!")
conn.commit()

# Inserção de dados na tabela
cur=conn.cursor() 
cur.execute("""INSERT INTO public."agenda" ("id", "nome" , "telefone" ) VALUES (1, 'Pessoa 1' , '02199999999' )""") 
conn.commit() 
print("Inserção realizada com sucesso!")

# Seleção de dados na tabela
cur = conn.cursor()
cur.execute("""select * from public."agenda" where "id" = 1""")
registro = cur.fetchone()
print(registro)
conn.commit()
print("Seleção realizada com sucesso!")

conn.close()