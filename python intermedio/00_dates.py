# 1. Crea una variable con la fecha y hora actual.
from datetime import datetime,timedelta

now = datetime.now()

# 2. Imprime solo el aÃ±o, mes y dÃ­a de la fecha actual.

print(now.year)
print(now.month)
print(now.day)
# 3. Crea una fecha especÃ­fica: 25 de diciembre de 2025 y muÃ©strala.

christmas_day = datetime(2025,12,25)
print(christmas_day)
# 4. Muestra solo la hora, los minutos y los segundos de un objeto time.

print(now.hour)
print(now.minute)
print(now.second)
# 5. Calcula cuÃ¡ntos dÃ­as faltan para el 1 de enero del aÃ±o siguiente.

print(datetime(2026,1,1)-now)

# 6. Crea una funciÃ³n que reciba una fecha y devuelva su timestamp.

def return_timestamp(datetime : datetime):
    return datetime.timestamp()

print(return_timestamp(datetime(2025,4,21)))

# 7. Suma 30 dÃ­as a la fecha actual usando timedelta.
add_tmd=timedelta(days=30)

print(now + add_tmd)

# 8. Crea una fecha y aÃ±ade 1 mes (consejo: hazlo sumando 30 dÃ­as como simplificaciÃ³n).
date = datetime(2026,12,30)
print(date + timedelta(days=30))

# 9. Compara dos fechas y muestra cuÃ¡l es anterior.

date_1 = datetime(2024,5,12)
date_2 = datetime(2024,8,12)

if date_1 > date_2 :
    print('la fecha mayor es date 1')
elif date_2 == date_1:
    print('son el mismo dia ambas fechas')
else:
    print('date 2 es la fecha mayor')

# 10. Crea una lista con varias fechas y ordÃ©nalas cronolÃ³gicamente.

date_3 = datetime(2021,12,12)

list_dates = [date_1,date_2,date_3]
sorted_dates = sorted(list_dates)

for date in sorted_dates:
    print(date)
