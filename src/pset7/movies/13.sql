select distinct p.name
from movies m
         join stars s on m.id = s.movie_id
         join people p on p.id = s.person_id
where m.id in (select s.movie_id
               from stars s
                        join people p on p.id = s.person_id
               where p.name = 'Kevin Bacon'
                 and p.birth = 1958)
  and p.name <> 'Kevin Bacon'
