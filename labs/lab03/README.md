# Tarefa de Laboratório 03 :wink:

# Será COVID-19?

Como todos sabem, COVID-19 é uma doença infecciosa causada pelo coronavírus SARS-COV-2. Os principais sintomas desta doença são: tosse, febre e dificuldade para respirar. Sua tarefa será escrever um programa que lê dados sobre os sintomas de um paciente e que indica a provável situação correspondente.


**Importante**: Nesta tarefa iremos exercitar operações com tipo bool e você deve obter os resultados descritos abaixo **sem utilizar comandos condicionais**!

## Trabalhando com o tipo `bool`

**Operações básicas** Antes de escrever seu programa, vamos fazer alguns testes com Python shell. Abra um terminal e o programa python3:

```python
$ python3
Python 3.7.6 
Type "help", "copyright", "credits" or "license" for more information.
>>>  
```

Escreva expressões relacionais e lógicas e verifique os resultados. Veja os exemplos:

```python
>>> 37.45 < 10.00 
False
>>>> True and False
False
>>>> var_bool = True or False
>>>> print(var_bool)
True
>>>> var_bool = 2 > 5
>>>> print(var_bool)
False
```

## Descrição da entrada

A entrada do seu programa será composta por três linhas, cada uma contendo valores True ou False e indicando, respectivamente, a presença ou ausência dos sintomas **tosse**, **febre** e **dificuldade de respirar**.

Veja um exemplo:

```python
True
True
False
```

**Dica**: você poderá converter a string de entrada em um valor booleano da seguinte forma:

```python
var_str = input()
var_bool = var_str == "True"
```

Note que `var_str == "True"` é uma expressão booleana que, ao ser avaliada, retornará:

* o valor booleano `True` se a string de entrada for `"True"` ou
* o valor booleano `False` se a string de entrada for `"False"` ou qualquer outra palavra.

## Descrição da saída

A saída deverá reapresentar os sintomas lidos e se é provável que o paciente tenha COVID-19. Para o exemplo acima a saída será:

```python
Tosse: True
Febre: True
Dificuldade para respirar: False
Provavelmente eh COVID-19: False
```

[Texto original para esta tarefa](https://www.ic.unicamp.br/~mc102/labs/roteiro-lab03.html)