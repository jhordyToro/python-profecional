import datetime

my_time = datetime.datetime.now() # hora local de mi PC u hora universal
my_date = datetime.date.today() # fecha actual

my_day = datetime.date.today()

print(my_time)
print(my_date)

print(f'Year: {my_day.year}')
print(f'Month: {my_day.month}')
print(f'Day: {my_day.day}')


# Formato	Código
# Año	     %Y
# Mes	     %m
# Día        %d
# Hora	     %H
# Minutos	 %M
# Segundos 	 %S

from datetime import datetime

my_datetime = datetime.now()
print(my_datetime)

latam = my_datetime.strftime('%d/%m/%Y')
print(f'Formato LATAM: {latam}')

usa = my_datetime.strftime('%m/%d/%Y')
print(f'Formato USA: {usa}')

random_format = my_datetime.strftime('año %Y mes %m día %d')
print(f'Formato random: {random_format}')

formato_utc = datetime.utcnow()
print(f'Formato UTC: {formato_utc}')

#PARA ESTO SE NECESITA INSTALAR PYTZ DESDE PIP 
from datetime import datetime
import pytz

def get_date_time_from_timezone(city_name:str, timezone:str)-> str:
  city_timezone = pytz.timezone(timezone)
  city_time = datetime.now(city_timezone)
  print(f'{city_name}: {city_time.strftime("%d/%m/%Y, %H:%M:%S")}')


get_date_time_from_timezone("London", "Europe/London")
get_date_time_from_timezone("LA", "America/Los_Angeles")
get_date_time_from_timezone("CDMX", "America/Mexico_City")
get_date_time_from_timezone("Tokyo", "Asia/Tokyo")
get_date_time_from_timezone("Sydney", "Australia/Sydney")