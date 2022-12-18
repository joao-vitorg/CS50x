select avg(r.rating)
from ratings r
         join movies m on r.movie_id = m.id
where m.year = 2012;
