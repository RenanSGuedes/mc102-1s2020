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