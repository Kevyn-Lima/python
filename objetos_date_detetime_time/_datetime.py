from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2024-12-27 10:55"
masacara_ptbr = '%d/%m/%y'
print(data_hora_atual.strftime(masacara_ptbr))