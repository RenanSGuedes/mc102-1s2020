# Discussão :speech_balloon:

Nesta tarefa de laboratório são utilizadas algumas ferramentas da tarefa anterior ao empregar a entrada de dados do usuário, a realização de operações entre variáveis e a impressão dos dados em tela.

Entretanto, o conceito de `float` ainda não foi explicado de maneira formal, mas os exemplos dados no [lab01](https://github.com/RenanSGuedes/mc102-1s2020/tree/master/labs/lab01/lab01) fazem tal referência de maneira não explícita. Ao mostrar a "conversão" do `input` do número `2.00` para `2` (sem o ponto seguido de dois zeros) temos um exemplo da mudança de tipo. Para o exemplo o `2.00` é do tipo `float` enquanto o `2` é um número inteiro. Podemos estender a ideia e consolidar a noção de que números com um ponto em sua composição são do tipo `float`.

## Exemplos

```python
Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import math  # importa a biblioteca com propriedades matemáticas
>>> a = math.pi # variável 'a' recebe o valor pi com tantas casas após a vírgula 
>>> a 
3.141592653589793 # pi com 15 casas após a vírgula
>>> type(a)
<class 'float'>
>>> b = int(a)
>>> b
3
>>> type(b)
<class 'int'>
```

Note que a linha do `import math` responsabiliza-se pela importação de um [módulo](https://docs.python.org/3/tutorial/modules.html). Este por sua vez possui propriedades matemáticas. Dentre elas foi atribuído à variável `a` o valor de `pi` por meio de `math.pi`, então ao consultar o tipo de `a` vemos que é `float`. Após converter `a` de `float` para `int` com a atribuição de `b` vemos que a classe de fato se torna inteira como previsto.

## Entrada do usuário :closed_book:

Seguindo esse conceito, de forma análoga ao que foi feito no laboratório anterior, para a entrada de um `float` basta usar a seguinte estrutura


```python
>>> a = float(input("Digite qualquer número: "))
Digite qualquer número: 20.15
>>> a
20.15
```

note que o número armazenado por estar na forma decimal é representado pelo ponto, daí parte a noção de `float` ao admitir que o ponto ao estar em várias posições atua de forma flutuante na alteração das unidades, dezenas, centenas, milhares e assim por diante para um determinado número. 

Agora que sabemos ler `inputs` do tipo `float`, se imaginarmos que no lugar do `20.15` fosse escrito somente `20`? O questionamento apresentado diz respeito ao fato do `20` por padrão ser tratado como um inteiro no `python`

```python
>>> a = 20
>>> type(a)
<class 'int'>
```

Todavia, se aplicarmos o que foi visto até agora o lado direito da atribuição na linha 

```python
>>> a = float(input("Digite qualquer número: "))
```

pode ser lido como: *"Input, receba qualquer número digitado e o converta para um tipo da classe float."*

Por essa razão se digitarmos um inteiro (sem ponto na composição) teremos algo assim

```python
>>> a = float(input("Digite qualquer número: "))
Digite qualquer número: 20
>>> a
20.0
>>> type(a)
<class 'float'>
```

Isso apenas reforça que ao converter um número para `float`, mesmo esse número não apresentando parcela diferente de zero do lado direito da vírgula ele torna-se `float` pela contabilização do `<inteiro>.0` em sua estrutura como é notado com o `20.0`. Porém, caso o `float()` ao redor do `input` não existisse, o número continuaria inteiro até que uma conversão fosse realizada, seja esta para uma `str`, `int` ou `float` por exemplo. 

Notamos grande semelhança em alguns casos ao analisar somente a quantia numérica presente em cada variável, ou seja, o `20` tem mesmo valor quantitativo do `20.0`. Então por que seria preferível utilizar um ao invés do outro? Temos que pensar que em cada situação, seja elaborando um algoritmo que resolva algum problema ou fazendo um produto que vai requerer a entrada de dados do usuário num formato pré-definido, temos que ver qual melhor se adequa em cada situação. Imagine uma proposta na qual fosse sujerida a criação de uma *landing page* e a mesma assumisse o papel de apresentar algum preço de produto a um cliente da franquia. Normalmente os valores são denotados como `float`. A loja escreveria um possível anúncio: *"Capas para almofadas com tema psicodélico por apenas R$19,99"*. O valor `19,99` seria incompatível de ser armazenado como `float`, mas imagine que para o cálculo dos produtos adicionados ao carrinho de compras estamos fazendo todas as substituições necessárias para o tratamento dos dados, nesse caso consideramos o `float` `19.99`. 

<p align="center">
  <img width="90%" src="assets/pillow_page.png"/>
</p>

Tendo em vista o que foi dito, vê-se que é comum utilizar `floats` para o registro de produtos de uma loja, até mesmo porque no setor de vendas o valor decimal do produto é sujeito a variações que não poderiam ser representadas com inteiros. 

No laboratório 02 no lugar do preço de um produto existe um documento de cobrança tratado como a  fatura dos clientes. O valor deste documento recebe um `float`. Sendo assim, ele comporta tanto `floats` com a parte decimal diferente de zero ou igual a zero (quando são inteiros).

```python
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
```

Ao analisar as duas primeiras linhas do código acima, vemos que o valor da fatura (`invoice_value`) recebe um `float` por motivos já discutidos. Os dias de atraso (`days_of_delay`) recebe um valor inteiro do número de dias. Nesse caso, como o cálculo somente é alterado num período de 24 horas é conveniente tratar o dado de entrada como `int`.

O tema de renegociação referido nessa tarefa está associado a um valor mínimo que deve ser dado ao credor visando o parcelamento da dívida [(Apresentação da tarefa)](https://github.com/RenanSGuedes/mc102-1s2020/tree/master/labs/lab02). Logo é necessário calcular os parâmentros mostrados segundo as atribuições acima

* Valor da fatura (`value`)
* Multa (`penalty`): 2% do valor da fatura.
* Juros (`interest`): 0.033% do valor da fatura multiplicado pelo número de dias em atraso.
* Valor total (`total_value`): soma do valor inicial com valor da multa e dos juros.
* Pagamento mínimo (`minimum_payment`): 10% do valor total. 

Após definir novas variáveis em função de outras a partir dos dados de entrada, podemos imprimir os dados de saída do programa com a função `print`. O maior desafio está ligado à [formatação dos números](https://pyformat.info/), nesse caso foi considerado somente dois dígitos após a vírgula, então para realizar tal procedimento podemos usar a função `format`. Essa função tem a propriedade de limitar a quantidade de dígitos após o ponto, porém, ela faz uso de métodos de arredondamento dependendo do comportamento dos dígitos do número que a função recebe e o formato do novo número após ser convertido.

## Exemplos 

**Estrutura do `print`**

```python
print(<texto>, format(<numero>, '.<casas_apos_a_virgula>f'))
```

```python
>>> from math import pi
>>> pi_value = pi
>>> pi_value
3.141592653589793
>>> print("Pi com duas casas após a vírgula:", format(pi_value, '.2f'))
Pi com duas casas após a vírgula: 3.14
```

ou

**Estrutura do `print`**

```python
print("<texto>...{:.<casas_apos_a_virgula>f}".format(<numero>))
```

```python
>>> from math import pi
>>> pi_value = pi
>>> pi_value
3.141592653589793
>>> print("Pi com duas casas após a vírgula: {:.2f}".format(pi_value))
Pi com duas casas após a vírgula: 3.14
```

**Um caso onde há arredondamento**

```python
>>> n = 30.999
>>> print('{:.2f}'.format(n))
31.00 # n com 3 dígitos (após a vírgula) é arredondado para 2 casas decimais
>>> n = 30.99
>>> print('{:.2f}'.format(n))
30.99 # sem arredondamento para n com dois dígitos após a vírgula
```