with_cough = input()
with_fever = input()
difficulty_breathing = input()
with_covid = "True"

def verify(a, b, c):
  if a == "True" and b == "True" and c == "True":
    return with_covid
  else:
    return with_covid == "False"

print('Tosse:', with_cough == "True")
print('Febre:', with_fever == "True")
print('Dificuldade para respirar:', difficulty_breathing == "True")
print('Provavelmente eh COVID-19:', verify(with_cough, with_fever, difficulty_breathing)) 
