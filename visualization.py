import re
import chart_studio
import cx_Oracle
import chart_studio.plotly as py
import plotly.graph_objs as go
import chart_studio.dashboard_objs as dashboard

chart_studio.tools.set_credentials_file(username='ktoto', api_key='AckP6D0eaUH5z4FPe1GW')

username = 'BD2'
password = 'oracle123'
databaseName = 'localhost/xe'

connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()

query = '''
SELECT Country.country , SUM(Map.rating) as sum_like 
FROM country 
JOIN author ON country.country = author.country 
JOIN map ON map.author_name = author.name
GROUP BY Country.country'''

cursor.execute(query)
country = []
likes = []

row = cursor.fetchone()

while row:
    if row[0]== None: 
        pass
    else: 
       country.append(row[0]) 
       likes.append(row[1])
    row = cursor.fetchone()

bar = [go.Bar(
    x=country,
    y=likes
)]
layout = go.Layout(
    # title='Спікери та загальна тривалість їхніх виступів -- топ-10',
    xaxis={
        'title':'країни'
    },
    yaxis={
        'title':'лайки'
    }
)

fig = go.Figure(data=bar, layout=layout)

url_1 = py.plot(fig, filename='країна - лайки')

#-------------------------------------------------------------
query ='''
SELECT
    game.game,
    ROUND(COUNT(map.id)*100/t.total, 2) AS percent
    FROM map JOIN game ON map.game = game.game,
        (SELECT COUNT(map.id) AS total FROM map) t
GROUP BY game.game, t.total'''

cursor.execute(query)
game = []
percent = []

row = cursor.fetchone()

while row:
    if row[0]== None: 
        pass
    else: 
       game.append(row[0]) 
       percent.append(row[1])
    row = cursor.fetchone()

pie = go.Pie(labels=game, values=percent)
url_2 = py.plot([pie], filename='гра-відсоток')

#---------------------------------------------------


query = '''SELECT
    EXTRACT(year from Map.map_date) as year,
    COUNT(Map.id)
FROM Map
GROUP BY EXTRACT(year from Map.map_date)
ORDER BY EXTRACT(year from Map.map_date)
'''

cursor.execute(query)
date = []
maps = []

row = cursor.fetchone()

while row:
    if row[0]== None: 
        pass
    else: 
       date.append(row[0]) 
       maps.append(row[1])
    row = cursor.fetchone()


scatter = go.Scatter(
    x=date,
    y=maps,
    mode='lines+markers'
)
url_3 = py.plot([scatter], filename='дата - завантажені мапи')

connection.close()

#---------------------------------------------------------------

board = dashboard.Dashboard()
board.get_preview()

def fileId_from_url(url):

    raw_fileId = re.findall("~[A-z.]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

box_1 = {
    'type':'box',
    'boxType':'plot',
    'fileId':fileId_from_url(url_1),
    'title':'країни та загальна кількість лайків(дизлайків)'
}
box_2 = {
    'type':'box',
    'boxType':'plot',
    'fileId':fileId_from_url(url_2),
    'title':'гра та відсоток карт,які були зроблені для неї серед усіх ігор'
}
box_3 = {
    'type':'box',
    'boxType':'plot',
    'fileId':fileId_from_url(url_3),
    'title':'Динаміка завантажень нових робіт(мап) за датою'
}

board.insert(box_1)
board.insert(box_3, 'below', 1)
board.insert(box_2, 'right', 1, 44)
board.get_preview()

py.dashboard_ops.upload(board, 'Chapanskiy Mark - Dashboard')