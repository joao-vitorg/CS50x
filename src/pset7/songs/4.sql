select name
from songs s
where s.danceability > 0.75
  and s.energy > 0.75
  and s.valence > 0.75
