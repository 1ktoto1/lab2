SELECT Country.land , SUM(Map.rating) as sum_like 
FROM country 
JOIN author ON country.land = author.author_country 
JOIN map ON map.author_name = author.author_name
GROUP BY Country.land;

SELECT
    game.play,
    ROUND(COUNT(map.map_id)*100/t.total, 2) AS percent

FROM map,game, 
    (SELECT COUNT(map.map_id) AS total FROM map) t
GROUP BY game.play;


SELECT map.map_date, COUNT(map.map_date) as total_maps 
FROM map 
GROUP BY map.map_date;