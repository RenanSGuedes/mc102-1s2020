# Discussão :speech_balloon:

## Entrada de Dados :keyboard:

Nesse segundo laboratório é buscado do aluno aplicar a entrada de dados do usuário por meio da função de `input` e ler dois números inteiros que vão passar por várias operações matemáticas e retornar os valores

Para ler os dois valores inteiros, é utilizado o `input`. Geralmente, para facilitar o entendimento do usuário sobre o tipo de dado que está sendo requisitado nós adicionamos uma `string` dentro do `input` 

```python
number_1 = input("Digite um número: ")
```

Dessa forma, ao abrir a `CLI` *(Command line interface)* teremos algo dessa forma

```
C:\Users\username>
```

Se na hora de instalar o python você adicionou ele ao `PATH` (clicar na *checkbox* da janela de instalação), ao digitar `python` e dar `<enter>` você verá algo semelhante a isso

```
C:\Users\username>python
Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Vemos algumas especificações da versão do programa, data, hora, arquitetura do processador e sistema operacional. Entretanto, o que realmente importa é que agora é possível adicionar trechos de código em `python` que poderão ser interpretados com êxito. 

Como estávamos falando, a entrada de dados do usuário é feita por meio do `input`. Com base nisso, após o símbolo `>>>` significa que o prompt está em modo espera para receber comandos. No nosso caso, vamos escrever

```python
C:\Users\username>python
Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> algum_numero = input("Digite algum numero: ")
```

ao dar `<enter>`

```python
C:\Users\username>python
Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> algum_numero = input("Digite algum numero: ")
Digite algum numero: 
```

note que o cursor ficará piscando logo à frente do caractere `: ` aguardando que alguém digite um número. Quando digitamos e apertamos `<enter>`

```python
C:\Users\username>python
Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> algum_numero = input("Digite algum numero: ")
Digite algum numero: 4
>>>
```

simplesmente o terminal retorna à condição de espera por novos comandos já que a solicitação feita pelo `input` já foi satisfeita. Todavia, e se quiséssemos acessar o valor de `algum_numero`? Bastaria digitar o nome da variável que a mesma apareceria impressa na linha seguinte

```python
C:\Users\username>python
Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> algum_numero = input("Digite algum numero: ")
Digite algum numero: 4
>>> algum_numero
'5'
```

note que o `5` aparece entre aspas simples indicando que a classe da variável é `string`. É possível verificar isso por meio da função `type`, veja

```python
>>> algum_numero
'5'
>>> type(algum_numero)
<class 'str'>
```

Então é possível vir à tona a seguinte questão: *"Por que a classe da variável escolhida é do tipo string sendo que no input eu estava pedindo um número?"*

A resposta para isso vem do fato de que o `input`, ao não receber nenhuma função de conversão do tipo de dado, sempre armazenará uma `string` em seu interior. Não é a toa que se quiséssemos fazer operações aritméticas com `algum_numero` talvez não fosse retornado o que de fato esperamos, mas isso será tratado adiante.

## Operações :symbols:

Em `python` é possível fazermos diversos tipos de operações. Normalmente quando esse tema é tratado fazemos a associação dessas operações contemplando o aspecto matemático da questão. Entretanto, será visto que o tema ultrapassa esse conceito e pode ser entendido sob outro plano quando aplicamos a lógica de programação. 

Imagine que deseja-se mostrar duas palavras de modo que uma seja posicionada seguida da outra. Então a forma mais lógica é pensar em colocar as palavras seguindo uma ordem que resolva o pedido. Por exemplo, atribuimos a uma variável `palavra_1` o valor `"casa"`

```python
Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> palavra_1 = "casa"
```

A classe da variável `palavra_1` pode ser aferida por meio da função `type` analogamente ao que foi feito em outra seção, então

```python
>>> palavra_1 = "casa"
>>> type(palavra_1)
<class 'str'>
```

O retorno `<class 'str'>` indica pela abreviação de `str` que a classe é do tipo `string`. Essa resposta é obtida nos casos em que temos textos sendo armazenados pelas variáveis, sendo que os mesmos são cercados pelos caracteres de aspas. Elas, por sua vez, podem ser simples ou duplas

```python
>>> string_com_aspas_duplas = "Aspas duplas"
>>> string_com_aspas_duplas
'Aspas duplas'
>>> string_com_aspas_simples = 'Aspas simples'
>>> string_com_aspas_simples
'Aspas simples'
```

Conclui-se que é facultativo o emprego dos tipos de aspas já que o valor declarado ao ser chamado traz a mesma forma - cercada por aspas simples.

Digamos que quiséssemos atribuir uma qualidade à casa tendo em vista seu imenso tamanho e quantidade de cômodos. Com base nisso, vamos atribuir a uma nova varíável (`palavra_2`) o valor de `'imensa'`

```python
palavra_2 = "imensa"
```

Para colocar uma palavra seguida da outra podemos usar a função `print`, responsável por imprimir na tela os valores desejados

```python
>>> palavra_1 = "Casa"
>>> palavra_2 = "imensa"
>>> print(palavra_1, palavra_2)
Casa imensa
```

Ao analisarmos o resultado do `print` vemos que a expressão `Casa imensa` foi impressa livrementente sem o acréscimo dos parêntesis. Porém, o espaço presente entre as palavras `Casa` e `imensa` é proveniente da vírgula da função `print`, ou seja, ao adicionar a vírgula é feita a concatenação das palavras, de modo que a enumeração imprime cada palavra seguida uma da outra com um espaço entre elas. Porém, se atribuírmos ao `print(palavra_1, palavra_2)` uma variável qualquer - por exemplo a letra `x` - e verificarmos o tipo dela teremos

```python
>>> palavra_1 = "Casa"
>>> palavra_2 = "imensa"
>>> x = print(palavra_1, palavra_2)
Casa imensa
>>> type(x)
<class 'NoneType'>
```

A linha `<class 'NoneType'>` indica que a variável `x` não possui tipo.

Uma maneira de imprimir de forma semelhante, só que em vez de `NoneType` passar a ter uma `string` seria abandonar a função `print` e se preocupar com os parâmetros passados para ela. O `NoneType` representa o retorno da função `print` e não do conteúdo o qual ela imprime ou recebe. Para concatenarmos *strings* fora do `print` vamos fazer uso de um símbolo matemático utilizado em operações de soma. Todavia, ao invés de somar números serão "somadas" palavras  

```python
>>> palavra_1 = "Casa"
>>> palavra_2 = "imensa"
>>> expressao = palavra_1 + " " + palavra_2
>>> expressao
'Casa imensa'
>>> type(expressao)
<class 'str'>
```

A variável `expressao` representa a concatenção de `palavra_1` e `palavra_2` com a inserção do caractere espaço entre elas. Note que o espaço existe devido ao conteúdo presente entre as aspas e não pelo espaço deixado entre o operador (`+`) e as variáveis, sendo o último aplicado somente para melhor organização do código. Para melhorar as habilidades referente aos tipos de operadores acesse [Python Operators, w3schools](https://www.w3schools.com/python/python_operators.asp)

- [x] *Arithmetic operators* (`+`, `-`, `*`, `/`, `%`, `**`, `//`)
- [ ] *Assignment operators*
- [ ] *Comparison operators*
- [ ] *Logical operators*
- [ ] *Identity operators*
- [ ] *Membership operators*
- [ ] *Bitwise operators* 

### Depois de toda a discussão, vamos ao principal
 
 Um algoritmo que resolve o problema proposto nesta tarefa é dado abaixo
 
```python
# Entrada do usuário

a = int(input())
b = int(input())

# Impressão dos valores recebidos e realização das operações entre os inteiros

print('a =',a)
print('b =',b)
print('a + b =',(a + b)) 
print('a - b =',(a - b))
print('a * b =',(a * b))
print('a // b =',(a // b))
print("a % b =",(a % b)) 
```

A interpretação de cada linha pode ser feita em etapas:

### Entrada do usuário
Nesse caso são lidos os valores de entrada do usuário por meio da função `input`, entretanto, o `int` externo ao `input` representa a função que converte o tipo de número lido num valor inteiro, então caso o usuário passe `2.00` de entrada `a` armazenará somente o inteiro `2`. Caso os valores pertençam ao intervalo entre `2` e `3` alguns critérios de arredondamento são aplicados de acordo com o número de casas após a vírgula (ponto), mas para o número `2.99`, por exemplo, seu `int` retornaria
```python
>>> n = 2.99
>>> int(n)
2
```

conclui-se que mesmo o número estando mais próximo de `3` do que `2` ainda assim o arredondamento é feito para baixo. Isso também ocorreria caso `n` fosse igual a `2.01` sendo o inteiro retornado igual a `2`. Nesse segundo caso é plausível pensar np respectivo arredondamento baseando-se na proximidade com o `2`, talvez só não seja tão trivial no primeiro.

```python
>>> n = 2.01
>>> int(n)
2
```

### Impressão dos valores recebidos e realização das operações entre os inteiros

A impressão dos valores recebidos foi feita por meio da função `print` mencionada anteriormente, sendo que as [operações](#operações) fizeram uso dos *Arithmetic operators*. Assim, as duas primeiras linhas do conjunto de `prints` imprime os valores armazenados por `a` e `b`, facilitando a orientação do usuário para os valores escolhidos. Em seguida é feita a sequência de operações enunciando algo do tipo `a * b = um número`, logo

"O produto de `a` e `b` é `um número`"

e isso se repete para as outras operações (soma, subtração, divisão...)

É válido ressaltar que como feito anteriormente, a vírgula, ao separar o primeiro argumento da função `print` (uma `string`), seguido do resultado da operação aritmética de `a` e `b` (um `int`), insere um espaço no local entre os argumentos. Aqui o operador de soma (`+`) não serviria para concatenar ao levar em conta os tipos de parâmetros passados para o `print`. Nesse caso os valores de `a` e `b` e suas respectivas operações precisariam estar cercadas pelo `str`, convertendo, dentro do `print` os valores inteiros para texto como segue

```python
>>> n_1 = 2
>>> n_2 = 5
>>> print("A soma de", n_1, "e", n_2, "eh", str(int(n_1 + n_2)))
A soma de 2 e 5 eh 7
```

ou 

```python
>>> n_1 = 2
>>> n_2 = 5
>>> print("A soma de " + str(int(n_1)) + " e " + str(int(n_2))  + " eh " + str(int(n_1 + n_2)))
A soma de 2 e 5 eh 7
```

ou (Acesse [w3resources](https://www.w3resource.com/python/python-print-statement.php) na seção **Using other data types** para mais detalhes do apresentado abaixo)

```python
>>> n_1 = 2
>>> n_2 = 5
>>> print("A soma de %d e %d eh %d"  %(n_1, n_2, n_1 + n_2))
```

usando o `format` ([Python String format() Method](https://www.w3schools.com/python/ref_string_format.asp))

```python
>>> n_1 = 2
>>> n_2 = 5
>>> print("A soma de {0} e {1} eh {2}".format(n_1, n_2, n_1 + n_2))
A soma de 2 e 5 eh 7
```

Os índices no interior das chaves (0, 1 e 2) podem ser substituidos por chaves vazias `{}` ou pelo nome das variáveis, desde que nesta última opção os valores das variáveis sejam declarados no interior do `format`

```python
>>> print("A soma de {n_1} e {n_2} eh {n_3}".format(n_1 = 2, n_2 = 5, n_3 = 2 + 5))
A soma de 2 e 5 eh 7
```

Note que o terceiro parâmetro do `format` (`n_3 = 2 + 5`) não poderia ser substituído por (`n_3 = n_1 + n_2`) caso os valores de `n_1` e `n_2` não fossem expicitados **dentro** do `format`.

```python
>>> n_1 = 2
>>> n_2 = 5
>>> print("A soma de {n_1} e {n_2} eh {n_3}".format(n_1 = 2, n_2 = 5, n_3 = n_1 + n_2))
A soma de 2 e 5 eh 7
```

Lembrando mais uma vez que os valores de `n_1` e `n_2` dentro do `format` não dependem dos valores declarados fora do print, logo se houve omissão das atribuições teríamos um erro

```python
>>> n_1 = 2
>>> n_2 = 5
>>> print("A soma de {n_1} e {n_2} eh {n_3}".format(n_1, n_2, n_3 = n_1 + n_2))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'n_1'
```

Então podemos imaginar que ao especificar um índice nomeado no interior de `strings` isso nos obriga a especificar o valor desse índice dentro do format, sendo que após a declaração é possível realizar operações considerando o conteúdo das variáveis gerenciado dentro do `format`.

## Conclusão :thinking:

Essa tarefa é fundamental para muitos artifícios que serão empregados nas próximas. Ela é importante por mais que pareça simples, entretanto, a infinidade de possibilidades e abordagens que podem ser dadas podem criar conexões importantes para resoluções mais complexas e problemas que não exijam necessariamente números em sua composição.