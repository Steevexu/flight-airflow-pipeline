with src as (
    select *
    from staging.flight_raw
)

select
    flight_id,
    flight_date,
    origin,
    destination,
    airline,
    departure_delay,
    arrival_delay,
    distance_km
from src