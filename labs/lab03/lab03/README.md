# Discussão :speech_balloon:

Nessa tarefa de laboratório é buscado do aluno o entendimento da classe `bool` do `python`. Essa categoria é oriunda da relação estabelecida entre variáveis. 

## Primeiro Exemplo

Imagine que nós estivéssemos estudando Mecãnica Vetorial e fôssemos comparar a ação que duas forças tem em um corpo. 

<p align="center">
  <img width="40%" src="assets/f1.png">
</p>

<p align="center">
  <img width="50%" src="assets/f2.png">
</p>

Note que nas figuras acima, temos o mesmo corpo sendo sujeito a duas situações não simultâneas. Na primeira atua uma força F<sub>1</sub> com a direção, sentido e magnitude mostrados. O mesmo se repete para F<sub>2</sub>. Caso quiséssemos comparar ambas as forças teríamos que contabilizar esses três parâmetros que definem um vetor. Imagine que F<sub>1</sub> vale 30 newtons (30 N) e está inclinada 20 graus (20°) com a horizontal no sentido anti-horário, enquanto  F<sub>2</sub> vale 7,5 newtons (7 N) e está a 180°. Nesse caso poderíamos saber se elas se assemelham de alguma forma primeiramente analisando sua magnitude. Se tomarmos como base as respostas como verdadeiras e falsas, como será aprofundado em `python`, se dissermos que ambas as forças tem mesma magnitude chegamos de maneira intuitiva que a resposta é **falsa**. Entretanto, se mudarmos o enunciado e agora dissermos que a força F<sub>1</sub> é quatro vezes maior que F<sub>2</sub>, temos que a nova resposta será **verdadeira** já que 4 vezes 7,5 é 30. Se analisamos a direção e o sentido nos dois casos a resposta é **falsa**, pois enquanto F<sub>1</sub> está inclinada, F<sub>2</sub> é horizontal.

Consequentemente, devido as forças atuarem em diferentes pontos nos corpos e apresentarem os três parâmetros enunciados anteriormente distintos, o efeito físico de suas ações também ocorre de forma distinta em cada situação. 

Após essa análise um pouco mais concreta, como poderíamos adequar o mesmo raciocínio para um algoritmo em `python`? Temos que resgatar a ideia dos tipos de variáveis e introduzir o conceito de variáveis booleanas. 

Temos as seguintes linhas de código

```python
>>> a = 30
>>> b = 20
>>> a == b
False
```

Foram declaradas as variáveis `a` e `b` e atribuídos os valores `30` e `20`, respectivamente. Contudo, diferente do que foi feito até agora, a linha `a == b` representa uma comparação entre `a` e `b`, como se fosse dito: *"a é igual a b?"*

O retorno dessa linha é verdadeiro ou falso (`True`/`False`). No caso visto `30` não é igual a `20`, logo a expressão booleana resulta em `False`. Mas se mudássemos para

```python
>>> a == a
True
```

De fato é o resultado esperado já que `30` é igual a `30`. 

Essa comparação não se limita aos números. Igual ao que foi visto na parte das operações com *ints*, *floats* e *strings* a comparação entre textos também existe. Então, se fizermos

```python
>>> nome_1 = "Newton"
>>> nome_2 = "Einstein"
>>> nome_1 == nome_2
False
>>> nome_1 != nome_2
True
```

Após atribuir os valores de dois nomes às variáveis `nome_1` e `nome_2`, foi feita a comparação de maneira análoga ao que foi visto para `a` e `b`. Entretanto, ao comparar o conteúdo de cada variável o valor retornado é `False` para o operador de igualdade (`==`). Todavia, ao fazer o emprego do operador (`!=`) é questionado se `nome_1` é **diferente** de `nome_2` como ocorre para as *strings* `"Newton"` e `"Einstein"`.

(Obs: **É importante ressaltar a diferença existente entre os símbolos `=` e `==`.** O primeiro caso - um sinal de igual - é usado para as atribuições vistas até aqui, logo ao utilizá-lo está sendo dito para uma determinada variável armazenar/receber o valor do lado direito da igualdade. Para o segundo caso deve ser considerado a igualdade de forma análoga à comparação matemática, sendo assim o lado esquerdo deve ser igual ao lado direito, sendo que os dois precisam ter sido declarados para que não haja erros na execução). Para melhorar o entendimento serão dados alguns exemplos. 

## Comprando Frutas...

<p align="center">
    <img width="80%" src="assets/fruits.jpg">
</p>

Dando continuidade à ideia inicial de operadores booleanos, pense que lhe foi solicitada a ida até o mercado mais próximo e pedido que você trouxesse uma lista de frutas indispensável para a salada do café da manhã. A lista apresenta as seguintes frutas em sua composição:

1. Maçã (10 unidades)
2. Banana (2 dúzias)
3. Carambola (7 unidades)
4. Melancia (2 unidades)
5. Caqui (6 unidades)
6. Laranja (2 dúzias e meia)
7. Melão (1 unidade)
8. Abacaxi (3 unidades)
9. Kiwi (5 unidades)

Na dúvida, após verificar o carrinho você ficou desconfiado se todas as frutas que foram solicitadas foram pegas. Então iniciou-se um *checklist* das compras. Visando a maior praticidade, você escreveu uma lista dos itens que estavam no carrinho e depois os comparou manualmente como segue

```python
itens_do_carrinho = ["Maçã", "Banana", "Melancia", "Caqui", "Laranja", "Kiwi"]

# A ideia de listas ainda não foi introduzida, porém o foco dessa parte ainda pertence aos operadores booleanos
```

Após listar as frutas, cercando por aspas duplas já que se trata de uma `string`, foi iniciada a verificação

```python
"Maçã" in itens_do_carrinho
```

A linha acima pode ser interpretada como: *"As maçãs pertencem aos itens do carrinho?"*. Se dermos `<enter>` o retorno esperado é `True`, já que as maçãs solicitadas na lista de compras estão entre os itens do carrinho no momento da verificação. Porém, se procurarmos pelo abacaxi entre os itens do carrinho com a linha de código

```python
"Abacaxi" in itens_do_carrinho
# O abacaxi está presente no carrinho de compras?
```

Nesse caso a respsota será `False`, pois a lista de compras inclui a compra de abacaxi, mas no carrinho de compras ele ainda não foi colocado, então seria preciso ir até a seção dos hortifrutigranjeiros.

<p align="center">
    <img src="assets/section.jpg">
</p>

Entre os tipos de [operadores](https://www.w3schools.com/python/python_operators.asp) (recapitulação ) presentes em `python`, os que apresentam como retorno **valores booleanos** estão em negrito

* Arithmetic operators  [(Discussão do Laboratório 1)](https://github.com/RenanSGuedes/mc102-1s2020/tree/master/labs/lab01/lab01)
    * `+` Soma
    * `-` Subtração
    * `*` Multiplicação
    * `/` Divisão
    * `%` Resto da divisão
    * `**` Potenciação
    * `//` Divisão inteira
* Assignment operators
* **Comparison operators (Visto no primeiro exemplo desse README)**
    * `==` Igual
    * `!=` Diferente
    * `>` Maior que
    * `<` Menor que
    * `>=` Maior ou igual a
    * `<=` Menor ou igual a
* **Logical operators**
    * `and` e
    * `or` ou
    * `not` contradição
* **Identity operators**
    * `is`
    * `is not`
* **Membership operators** 
    Usado para *arrays* e *strings*, verifica se um item ou trecho de texto pertence a um objeto ou `string`, por exemplo
    * `in` está contido
    * `not in` não está contido
* Bitwise operators

```python
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
```


```python
with_cough = input()
with_fever = input()
difficulty_breathing = input()
with_covid = "True"

verify = with_cough == "True" and with_fever == "True" and difficulty_breathing == "True" 

print('Tosse:', with_cough == "True")
print('Febre:', with_fever == "True")
print('Dificuldade para respirar:', difficulty_breathing == "True")
print('Provavelmente eh COVID-19:', verify) 
```

**Referências**

* [w3schools, Python Operators](https://www.w3schools.com/python/python_operators.asp)