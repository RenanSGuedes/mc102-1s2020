invoice_value = float(input())
days_of_delay = int(input())

value = invoice_value
penalty = .02  * value 
interest = .00033 * value * days_of_delay
total_value = invoice_value + penalty + interest
minimum_payment = .1 * total_value

print('Valor: R$', format(value, '.2f'))
print('Multa: R$', format(penalty, '.2f'))
print('Juros: R$', format(interest, '.2f'))
print('Valor total: R$', format(total_value, '.2f'))
print('Valor minimo para renegociacao: R$', format(minimum_payment, '.2f'))