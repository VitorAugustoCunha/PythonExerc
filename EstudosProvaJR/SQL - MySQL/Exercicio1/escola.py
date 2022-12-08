import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="escola"
)
mycursor = mydb.cursor()

class Sala1:
  def __init__(self, nome, nota1, nota2, nota3):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2
    self.nota3 = nota3

  def adicionar_aluno(self):
    sql = "INSERT INTO sala1 (nome, nota1, nota2, nota3, media) VALUES (%s, %s, %s, %s, %s)"
    mediaCalc = (self.nota1 + self.nota2 + self.nota3) / 3
    val = (self.nome, self.nota1, self.nota2, self.nota3, mediaCalc)
    mycursor.execute(sql, val)
    mydb.commit()
    print('Aluno adicionado')

  @staticmethod
  def calcular_media(ID):
    sql = (f"SELECT media FROM sala1 WHERE ID = '{ID}'")
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

class Sala2:
  def __init__(self, nome, nota1, nota2, nota3):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2
    self.nota3 = nota3

  def adicionar_aluno(self):
    sql = (f"INSERT INTO sala2 (nome, nota1, nota2, nota3, media) VALUES (%s, %s, %s, %s, %s)")
    mediaCalc = (self.nota1 + self.nota2 + self.nota3) / 3
    val = (self.nome, self.nota1, self.nota2, self.nota3, mediaCalc)
    mycursor.execute(sql, val)
    mydb.commit()
    print('Aluno adicionado')

  @staticmethod
  def calcular_media(ID):
    sql = (f"SELECT media FROM sala2 WHERE ID = '{ID}'")
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult
