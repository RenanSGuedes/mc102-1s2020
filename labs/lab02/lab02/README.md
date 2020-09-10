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

Note que a linha do `import math` responsabiliza-se pela importação de uma biblioteca. Como o nome sugere ela possui propriedades matemáticas. Dentre as mesmas foi atribuído à variável `a` o valor de `pi` por meio de `math.pi`, então ao consultar o tipo de `a` vemos que é `float`. Após converter `a` de `float` para `int` com a atribuição de `b` vemos que a classe de fato se torna inteira.