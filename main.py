import cx_Oracle

username = 'BD2'
password = 'oracle123'
databaseName = 'localhost/xe'

connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()

"""-------------------------------------------------------------------------------------"""

query = '''
SELECT Country.country , SUM(Map.rating) as sum_like 
FROM country 
JOIN author ON country.country = author.country 
JOIN map ON map.author_name = author.name
GROUP BY Country.country'''

cursor.execute(query)
print('Запит 1')
print('|country             |total_likes')
print('-'*35)

row = cursor.fetchone()
while row:
	print("|{:20s}|{}".format(row[0], row[1]))
	row = cursor.fetchone()

print()


"""----------------------------------------------------------------------"""

query ='''
SELECT
    game.game,
    ROUND(COUNT(map.id)*100/t.total, 2) AS percent
    FROM map JOIN game ON map.game = game.game,
        (SELECT COUNT(map.id) AS total FROM map) t
GROUP BY game.game, t.total'''

cursor.execute(query)
print('Запит 2')
print('|game                                      |percentage')
print('-'*50)

row = cursor.fetchone()
while row:
	print("|{:42s}|{}%".format(row[0], row[1]))
	row = cursor.fetchone()
print()

"""-----------------------------------------------------"""
query = '''
SELECT
    EXTRACT(year from Map.map_date) as year,
    COUNT(Map.id)
FROM Map
GROUP BY EXTRACT(year from Map.map_date)
ORDER BY EXTRACT(year from Map.map_date)'''

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
