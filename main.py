import cx_Oracle

username = 'BD2'
password = 'oracle123'
databaseName = 'localhost/xe'

connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()

"""-------------------------------------------------------------------------------------"""

query = '''
SELECT Country.land , SUM(Map.rating) as sum_like 
FROM country 
JOIN author ON country.land = author.author_country 
JOIN map ON map.author_name = author.author_name
GROUP BY Country.land'''

cursor.execute(query)
print('Запит 1')
print('|country        |total_likes')
print('-'*35)

row = cursor.fetchone()
while row:

    print("|{:20s}|{}".format(row[0], row[1]))
    row = cursor.fetchone()

print()

"""----------------------------------------------------------------------"""

query ='''
SELECT
    game.play,
    ROUND(COUNT(map.map_id)*100/t.total, 2) AS percent

FROM map,game,
    (SELECT COUNT(map.map_id) AS total FROM map) t
GROUP BY game.play'''

cursor.execute(query)
print('Запит 2')
print('|game                    |percentage')
print('-'*35)

row = cursor.fetchone()
while row:

    print("|{:35s}|{}%".format(row[0], row[1]))
    row = cursor.fetchone()

print()

"""------------------------------------------------------------------------"""

query = '''
SELECT map.map_date, COUNT(map.map_date) as total_maps 
FROM map 
GROUP BY map.map_date'''

cursor.execute(query)
print('Запит 3')
print('|year  | maps_count')
print('-'*20)

row = cursor.fetchone()
while row:

    print("|{:<6}|{}".format(row[0], row[1]))
    row = cursor.fetchone()

print()

connection.close()