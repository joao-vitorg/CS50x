select m.title
from movies m
         join stars s on m.id = s.movie_id
         join people p on p.id = s.person_id
WHERE p.name IN ('Johnny Depp', 'Helena Bonham Carter')
GROUP BY m.title
HAVING COUNT(m.title) = 2;
