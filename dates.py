import datetime

def fecha_actual():
    return print(datetime.datetime.now())

def diferemcia_fechas(fecha1,fecha2):
    '''
    Funcion que calcula la diferencia en fechas con formato Y-m-d
    '''
    fecha1 =datetime.datetime.strptime(fecha1,'%Y-%m-%d')
    fecha2 =datetime.datetime.strptime(fecha2,'%Y-%m-%d')
    
    diferencia = fecha1 - fecha2
    return print(diferencia.days)