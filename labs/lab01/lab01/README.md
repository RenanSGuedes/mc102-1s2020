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

-[x] *Arithmetic operators* (`+`, `-`, `*`, `/`, `%`, `**`, `//`)
-[ ] *Assignment operators*
-[ ] *Comparison operators*
-[ ] *Logical operators*
-[ ] *Identity operators*
-[ ] *Membership operators*
-[ ] *Bitwise operators* 