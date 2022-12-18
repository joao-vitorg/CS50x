select avg(s.energy)
from songs s
         join artists a on a.id = s.artist_id
where a.name = 'Drake';
