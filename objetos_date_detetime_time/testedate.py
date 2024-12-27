# O que é datetime?

#O módulo 'datetime' em Python é usado para lidar com datas e horas.
#Ele possui várias classes úteis como date, time e timedelta.

# from datetime import date, datetime, time

# #d = date(day=27,year=2024, month=12)

# # print(d)

# print(date.today())
# #Tras o dia de hoje, ja o datetime, ele tras com o dia, mes, ano, hora, minutos, secundos, microsegundos, e assim por diante.
# #Muito valido para compras em ecommerces.

# data_hora = datetime.today()
# print(data_hora)
# hora = time()

# print(hora)

from datetime import datetime,timedelta

tipo_carro = 'G'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()


if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro deu entrada: {data_atual}, e ficara pronto as {data_estimada}")
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro deu entrada: {data_atual}, e ficara pronto as {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro deu entrada: {data_atual}, e ficara pronto as {data_estimada}")