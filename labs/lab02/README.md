# Tarefa de laboratório 02 :stuck_out_tongue_winking_eye:

# Atraso e renegociação

Todos sabem que é melhor pagar as faturas em dia. No entanto, vários fatores, incluindo crises globais, podem levar ao atraso e aos terríveis encargos. Nestes casos, é sempre bom não entrar em pânico e procurar mecanismos para renegociação, visto que vários credores aceitam o parcelamento da dívida mediante o pagamento de um valor mínimo.

Nesta tarefa, ao manipular valores monetários, você irá utilizar o tipo `float` e aprenderá conceitos básicos sobre aritmética com ponto flutuante e também sobre formatação de escrita.

## Trabalhando com `floats`

**Operações básicas** Antes de escrever seu programa, vamos fazer alguns testes com a linha de comando. Abra um terminal e o programa python3:

```python
$ python3
Python 3.7.6
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Atribua um número real para a variável valor e escreva algumas operações:

```python
>>> valor = 99.99
>>> multa = valor * 0.02    
>>> juros = valor * 0.00033
>>> print(multa)
1.9998
>>> print(juros)
0.0329967
```

Formatação Note que os valores foram exibidos com mais casas decimais do que as duas usuais para valores monetários. Podemos formatar o número de casas na saída por meio do comando `format()`:

```python
>>> format(juros, '.2f')
>>> '0.03'    
>>> print("R$", format(juros, '.2f'))
R$ 0.03 
```

Abaixo temos duas outras maneiras de se obter esta saída. Para entender melhor o funcionamento destes comandos leia a página [Formatação em Python](https://www.ic.unicamp.br/~mc102/labs/format.html).

```python
>>> "{:.2f}".format(juros)
'0.03'
    
>>> "%.2f" % juros  # estilo antigo - pode não funcionar nas próximas versões de Python 
'0.03'
```

**Limitações** A exibição de um maior número de casas pode revelar resultados surpreendentes. Observe os valores 0.1 e 0.5 com 30 casas decimais:

```python
>> format(0.1, '.30f')
'0.100000000000000005551115123126'
>>> format(0.5, '.30f')
'0.500000000000000000000000000000'
```

Para entender a razão destes resultados, veja a seção [15. Floating Point Arithmetic: Issues and Limitations](https://docs.python.org/3.7/tutorial/floatingpoint.html) da documentação de Python 3.

## Descrição de entrada

A saída deverá ser apresentada como descrito a seguir, com strings sem acentos:

* **Valor**: o valor lido da entrada;
* **Multa**: 2% do valor da fatura.
* **Juros**: 0.033% do valor da fatura multiplicado pelo número de dias em atraso.
* **Valor total**: soma do valor inicial com valor da multa e dos juros.
* **Pagamento minimo para renegociacao**: 10% do valor total.

Para a entrada da seção anterior, a saída será:

```python
Valor: R$ 99.99
Multa: R$ 2.00
Juros: R$ 0.10
Valor total: R$ 102.09
Valor minimo para renegociacao: R$ 10.20
```

Note que todos os valores da saída devem ser expressos com duas casas decimais. Utilize a formatação como sugerido acima.