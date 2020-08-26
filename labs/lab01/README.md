# Tarefa de Laboratório 01 :monocle_face:

## Inteiros

Nesta tarefa, daremos continuidade à familiarização com o interpretador Python e com a ferramenta de submissão SuSy. Você deverá ler valores na entrada e produzir as saídas esperadas. Além disso, verificaremos como funcionam as operações de divisão inteira e módulo em Python.

## Testes com a shell

Antes de escrever seu programa, vamos fazer alguns testes com a linha de comando. Abra um terminal e o programa `python3`:

```python
$ python3
Python 3.7.1 
Type "help", "copyright", "credits" or "license" for more information.
>>>  
```

Atribua valores inteiros para as variáveis `a` e `b`:

```python
>>> a = 7
>>> b = 3 
```

**Soma**, **subtração**, **multiplicação**. Verifique o valor das operações básicas:

```python
>>> a + b
10
>>> a - b
4
>>> a * b
21
```

**Divisão inteira**. Utiliza o operador // e irá retornar como quociente o valor q = ⌊ a/b ⌋. Observe:

```python
>>> a // b
2
```

Verifique o comportamento desta operação quando alteramos os sinais dos operandos. Lembre-se que a função piso é o arredondamento de um número para baixo e, portanto, ⌊ 2.33 ⌋ = 2 e ⌊ -2.33 ⌋ = -3. Para facilitar a conferência dos valores, vamos imprimir as equações:

```python
>>> print(a, "//", b, "=", a // b)
7 // 3 = 2

>>>> print(-a, "//", b, "=", -a // b)
-7 // 3 = -3

>>> print(a, "//", -b, "=", a // -b)
7 // -3 = -3

>>> print(-a, "//", -b, "=", -a // -b)
-7 // -3 = 2
```

**Módulo** O operador % retorna o resto r de uma divisão inteira, tal que r = a - ⌊ a/b ⌋ * b. Observe a variação do resultado com a variação dos sinais dos operadores.

```python
>>> print(a, "%", b, "=", a % b)
7 % 3 = 1

>>> print(-a, "%", b, "=", -a % b)
-7 % 3 = 2

>>> print(a, "%", -b, "=", a % -b)
7 % -3 = -2

>>> print(-a, "%", -b, "=", -a % -b)
-7 % -3 = -1
```

**Divisão real**. A divisão em Python com resultados reais tem como resultado um float. Este assunto será abordado em outra tarefa.

**Divisão por zero**. A divisão por zero não tem valor definido (leia [Wikipedia: Divisão por zero](https://pt.wikipedia.org/wiki/Divis%C3%A3o_por_zero) ou veja o vídeo [Why can't you divide by zero? - TED-Ed"](https://www.youtube.com/watch?v=NKmGVE85GUU)). Em Python, uma tentativa de dividir por zero ou tentar calcular o resto da divisão por zero levará à interrupção do programa devido a uma exceção.

```python
>>> a // 0
Traceback (most recent call last):
  File "", line 1, in 
ZeroDivisionError: integer division or modulo by zero

>>> a % 0
Traceback (most recent call last):
  File "", line 1, in 
ZeroDivisionError: integer division or modulo by zero
>>>
```

## Descrição de entrada

A entrada do seu programa será composta por duas linhas, cada uma contendo um número inteiro. Observe o exemplo abaixo:

```python
10
7
```

Dica: você poderá ler este par de valores com os comandos:

```python
a = int(input())
b = int(input())
```

## Descrição de saída

A saída deverá reproduzir o valor lido das variáveis a e b e apresentar o conjunto de equações com as operações descritas nesta tarefa da seguinte forma:

```python
a = 10
b = 7
a + b = 17
a - b = 3
a * b = 70
a // b = 1
a % b = 3
```

[Texto original para esta tarefa](https://www.ic.unicamp.br/~mc102/labs/roteiro-lab01.html)