select
    flight_date as day,
    count(*) as total_flights,
    avg(departure_delay) as avg_departure_delay,
    avg(arrival_delay) as avg_arrival_delay,
    sum(distance_km) as total_distance
from {{ ref('stg_flights') }}
group by 1