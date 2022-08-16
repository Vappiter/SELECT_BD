import sqlalchemy
import csv
from pprint import pprint
import os

data_bd = []


def insert_table(colums,len_list):
  inrt_data_bd = []
  for i1 in range (1, len_list):
    inrt_data_bd.append(data_bd[i1][colums])
  var_test1 = set (inrt_data_bd)
  pprint(var_test1)
  

file_path = (os.path.split(__file__)) # Считывает текущую директорию скрипта, тут же должен храниться файл CSV
os.chdir(file_path [0]) # Устанавливает директорию
with open("file_BD.csv") as f:
  rows = csv.DictReader(f, delimiter=";")
  # pprint (rows)
  for row in rows:
    print(row['musician_name'], row['album_year'])
  data_bd = list(rows)
# pprint (data_bd)

db = 'postgresql://postgres:123456@localhost:5432/test_py47'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()
# print (engine)
# connection.execute('''INSERT INTO album(album_id, album_name, album_year) \
#                    VALUES (4, 'ALBUM 4', 1980), (5, 'ALBUM 5', 1990), (6, 'ALBUM 6', 1990)''')
len_list = len (data_bd)
insert_table(0, len_list)
insert_table(1, len_list)
insert_table(3, len_list)

# for data_bd_2 in data_bd:
#     if data_bd_2[0] == 'musician_name':
#      continue   
#     musician_test = connection.execute('''SELECT musician_name FROM musician;''')
#     var1 = musician_test.fetchone()
#     if var1 == None:
#       sql_text = '''INSERT INTO musician (musician_name, musician_nickname) VALUES (%s, %s)'''
#       data_insert = data_bd_2[0], data_bd_2[1]
#       connection.execute(sql_text, data_insert)
#     elif var1 == data_bd_2[0]:
#         continue
#     else:
#       sql_text = '''INSERT INTO musician (musician_name, musician_nickname) VALUES (%s, %s)'''
#       data_insert = data_bd_2[0], data_bd_2[1]
#       connection.execute(sql_text, data_insert)   
              
            
# pprint (musician_test)
  
    
# sel = connection.execute('''SELECT * FROM album;''').fetchmany(6)
# print (sel)