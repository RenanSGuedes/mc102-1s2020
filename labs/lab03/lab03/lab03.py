with_cough = input()
with_fever = input()
difficulty_breathing = input()
with_covid = "True"

verify = with_cough == "True" and with_fever == "True" and difficulty_breathing == "True" 

print('Tosse:', with_cough == "True")
print('Febre:', with_fever == "True")
print('Dificuldade para respirar:', difficulty_breathing == "True")
print('Provavelmente eh COVID-19:', verify) 
