select distinct p.name
from ratings r
         join directors d on r.movie_id = d.movie_id
         join people p on p.id = d.person_id
where r.rating >= 9;
