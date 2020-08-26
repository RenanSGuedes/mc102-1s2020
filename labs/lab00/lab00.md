# Tarefa de Laboratório 00 :nerd_face:

O objetivo deste exercício é propiciar a familiarização com o interpretador Python e a ferramenta de submissão e testes automáticos SuSy. Teste as opções corretas e todos os erros documentados. Esta experiência poderá facilitar muito o seu processo de desenvolvimento e depuração das próximas tarefas.

Em muitos tutoriais, o primeiro programa ensinado é o que escreve a mensagem Hello, world!. Adotaremos esta abordagem e escreveremos **Oi mundo!**

Veja o código abaixo

```python
print("Oi, mundo!")
```

# Testes com a shell

Abra um terminal e o programa `python3`:

```python
$ python3
Python 3.7.1 
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

A partir deste ponto, você pode testar comandos em Python de forma interativa. Vamos lá!

```python
>>> print("Oi, mundo!")
Oi, mundo!
```

Muitas vezes não escrevemos exatamente como o interpretador esperava. São erros de sintaxe ou de definição de nomes. Veja os exemplos abaixo:

* **Falta de parênteses**

```python
>>> print "Oi, mundo!"
  File "", line 1
    print "Oi, mundo!"
                     ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Oi, mundo!")?
```

Neste caso, o interpretador teve facilidade para identificar nosso erro e nos apresentou uma mensagem bem amigável, nos direcionando para a solução.

* **Função com nome inválido**

Outro erro comum é não digitarmos corretamente o nome de uma função.

```python
>>> prit ("Oi, mundo!")
Traceback (most recent call last):
  File "", line 1, in 
NameError: name 'prit' is not defined
>>> 
```

Às vezes o nome está correto, mas o interpretador precisa de ajuda para encontrar a função. Estudaremos isso mais para a frente na disciplina.

* **String sem delimitador final**

Às vezes, a mensagem pode ser um pouco mais difícil de entender. Abaixo, o interpretador está indicando que a linha acabou (EOL = end of line) enquanto tentava processar a string.

```python
>>> print("Oi, mundo!)
  File "", line 1
    print("Oi, mundo!)
                      ^
SyntaxError: EOL while scanning string literal
```

* **String sem delimitador inicial**

Um erro semelhante leva a uma mensagem bem diferente. Neste caso, como não havia aspas demarcando o início da string, o interpretador tentou avaliar o seu conteúdo como código Python e indicou que a sintaxe está inválida.

```python
>>> print(Oi, mundo!")
  File "", line 1
    print(Oi, mundo!")
                    ^
SyntaxError: invalid syntax
```

[Link para o texto original desta tarefa](https://www.ic.unicamp.br/~mc102/labs/roteiro-lab00.html)


























