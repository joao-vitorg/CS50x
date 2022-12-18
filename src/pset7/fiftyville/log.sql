select csr.description
from crime_scene_reports csr
where csr.street = 'Humphrey Street'
  and csr.day = 28;

select i.transcript
from interviews i
where i.day = 28
  and i.month = 7
  and i.transcript like '%thief%';

select name
from bakery_security_logs bsl
         join people p on bsl.license_plate = p.license_plate
where bsl.day = 28
  and bsl.hour = 10
  and bsl.minute >= 15
  and bsl.minute <= 25
  and bsl.activity = 'exit';

select p.name
from atm_transactions at
         join bank_accounts ba on at.account_number = ba.account_number
         join people p on p.id = ba.person_id
where at.day = 28
  and at.atm_location = 'Leggett Street'
  and at.transaction_type = 'withdraw'
  and p.name in ('Vanessa', 'Bruce', 'Barry', 'Luca', 'Sofia', 'Iman', 'Diana', 'Kelsey');

select caller.name, rec.name
from phone_calls pc
         join people rec on rec.phone_number = pc.receiver
         join people caller on caller.phone_number = pc.caller
where pc.day = 28
  and pc.duration <= 60
  and caller.name in ('Bruce', 'Diana', 'Iman', 'Luca');

select f.id, a2.city
from flights f
         join airports a on a.id = f.origin_airport_id
         join airports a2 on a2.id = f.destination_airport_id
where a.city = 'Fiftyville'
  and f.day = 29
ORDER BY hour
limit 1;

select p2.name
from passengers p
         join people p2 on p.passport_number = p2.passport_number
where p.flight_id = 36
  and p2.name in ('Bruce', 'Diana')
