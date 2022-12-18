select m.title
from movies m
         join ratings r on m.id = r.movie_id
         join stars s on m.id = s.movie_id
         join people p on p.id = s.person_id
where p.name = 'Chadwick Boseman'
order by rating desc
limit 5;
