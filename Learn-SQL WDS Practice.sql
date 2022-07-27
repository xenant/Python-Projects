use record_company;


SELECT bands.name as "Band Name" from bands
LEFT JOIN albums on bands.id = albums.band_id
GROUP BY albums.band_id
HAVING COUNT(albums.id) = 0; 

SELECT SUM(songs.length) as 'Duration',
albums.name as "Name"
from ALBUMS 
JOIN songs on albums.id = songs.album_id
GROUP BY songs.album_id
ORDER BY Duration DESC
LIMIT 1;

SELECT id,name FROM bands
ORDER BY id DESC; 


SELECT id, name from songs
ORDER BY id desc; 


DELETE FROM albums
WHERE id = 19;
DELETE FROM bands
WHERE id = 8;

use record_company;
select avg(length) as "Average Song Duration"
from songs; 

SELECT albums.name as "Album", albums.release_year as "Release Year", MAX(songs.length) as "Duration"
FROM albums 
JOIN songs on albums.id = songs.album_id
group by songs.album_id;

SELECT
  albums.name AS 'Album',
  albums.release_year AS 'Release Year',
  MAX(songs.length) AS 'Duration'
FROM albums
JOIN songs ON albums.id = songs.album_id
GROUP BY songs.album_id;

