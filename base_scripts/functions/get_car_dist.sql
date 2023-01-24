--Функция для вычисления дистанции между домом и объектом на машине
--CREATE DATE 2023.01.24

CREATE OR REPLACE FUNCTION get_car_distance(
    f_house integer,
    f_object varchar(150),
    lat1 numeric, 
    lon1 numeric, 
    lat2 numeric, 
    lon2 numeric
)

RETURNS integer
AS
$BODY$

import requests

url = f'https://routing.openstreetmap.de/routed-car/route/v1/driving/{lat1},{lon1};{lat2},{lon2}?'

try:
    response = requests.get(url).json()
    return int(response['routes'][0]['distance'])

except Exception as Error:
    plpy.notice(f'Не уалось получить дистанцию между ддомом № {f_house} и объектом № {f_object}\n {Error}')    

$BODY$
LANGUAGE 'plpython3u'
