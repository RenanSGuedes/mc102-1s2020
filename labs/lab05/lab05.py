mass = float(input())
age = int(input())
authorization = str(input())
fever = str(input())
trip_abroad = str(input())
contact = str(input()) 
first_donation = str(input())
donation_last_12 = int(input())
months_last_donation = int(input())
gender = str(input())
pregnant_or_breastfeeding = str(input())

print("Massa corporal:", format(mass, '.1f'))
print("Idade:", age)
print("Documento de autorizacao:", authorization)
print("Febre ou sintomas gripais:", fever)
print("Viagem recente ao exterior:", trip_abroad)
print("Contato com caso de COVID-19:", contact)    
print("Primeira doacao:", first_donation)
print("Doacoes nos ultimos 12 meses:", donation_last_12)
print("Meses desde ultima doacao:", months_last_donation)    
print("Sexo biologico:", gender)

if mass < 50:
  print("Impedimento: abaixo da massa corporal minima")
elif age < 16:
  print("Impedimento: menor de 16 anos")
elif age == 16 or age == 17:
  if authorization == "N":
    print("Impedimento: menor de 18 anos sem consentimento dos responsaveis")
elif age > 60:
  if age > 69:
    print("Impedimento: maior de 69 anos")
  elif first_donation == "S":
    print("Impedimento: maior de 60 anos e primeira doacao")
elif fever == "S":
  print("Impedimento: febre ou sintomas gripais")
elif trip_abroad == "S":
  print("Impedimento: viagem recente ao exterior")
elif contact == "S":
  print("Impedimento: Contato com caso de COVID-19")
elif donation_last_12 > 3:
  print("Impedimento: numero maximo de doacoes anuais foi atingido")
elif months_last_donation > 2:
  print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
elif gender == "M":
  if pregnant_or_breastfeeding == "S":
    print("Impedimento: gravida ou amamentando")
else: 
  print("Agende um horario para triagem completa")