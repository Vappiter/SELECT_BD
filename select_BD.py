import sqlalchemy
import csv
from pprint import pprint
import os

data_bd = []

file_path = (os.path.split(__file__)) # Считывает текущую директорию скрипта, тут же должен храниться файл CSV
os.chdir(file_path [0]) # Устанавливает директорию
with open("file_BD.csv") as f:
  rows = csv.reader(f, delimiter=";")
  data_bd = list(rows)
pprint (data_bd)

db = 'postgresql://postgres:123456@localhost:5432/test_py47'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()
# print (engine)
# connection.execute('''INSERT INTO album(album_id, album_name, album_year) \
#                    VALUES (4, 'ALBUM 4', 1980), (5, 'ALBUM 5', 1990), (6, 'ALBUM 6', 1990)''')

for data_bd_2 in data_bd:
  musician_test = connection.execute('''SELECT musician_name FROM musician;''')
  if musician_test.fetchone() == None:
      connection.execute('''INSERT INTO musician (musician_name, musician_nickname) VALUES (str(data_db_2[0]), str(data_db_2[1]));''')
      pprint('Пусто')
  else:
      pprint ('УРА!!! Работает')  
  pprint (musician_test)
  
    
sel = connection.execute('''SELECT * FROM album;''').fetchmany(6)
print (sel)