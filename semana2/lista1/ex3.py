valor = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = valor // 86400
valor = valor % 86400
horas = valor // 3600
valor = valor % 3600
minutos = valor // 60
valor = valor % 60
segundos = valor
print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
