import sqlalchemy

db = 'postgresql://postgres:123456@localhost:5432/test_py47'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()
print (engine)
# connection.execute('''INSERT INTO album(album_id, album_name, album_year) \
#                    VALUES (4, 'ALBUM 4', 1980), (5, 'ALBUM 5', 1990), (6, 'ALBUM 6', 1990)''')
sel = connection.execute('''SELECT * FROM album;''').fetchmany(6)
print (sel)