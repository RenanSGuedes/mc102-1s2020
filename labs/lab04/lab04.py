a = float(input())
b = float(input())
c = float(input())

equilateral = (a == b) and (b == c) and (a == c)
isosceles = (a == b) or (b == c) or (a == c)
scalene = (a != b) and (a != c) and (c != a)
acutangle = (a**2 < b**2 + c**2) and (b**2 < a**2 + c**2) and (c**2 < a**2 + b**2) 
rectangle = (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2)
obtusangle = (a**2 > b**2 + c**2) or (b**2 > a**2 + c**2) or (c**2 > a**2 + b**2)
error = (a > b + c) or (b > a + c) or (c > a + b) or (a <= 0) or (b <= 0) or (c <= 0) 

if error: 
  print("Valores invalidos na entrada")
elif equilateral:
  print("Triangulo equilatero")
  print("Triangulo acutangulo")
elif isosceles:
  print("Triangulo isosceles")
  if acutangle:
    print("Triangulo acutangulo")
  if obtusangle:
    print("Triangulo obtusangulo")
elif scalene:
    print("Triangulo escaleno")
    if rectangle: 
      print("Triangulo retangulo")
    if acutangle:
      print("Triangulo acutangulo")
    if obtusangle: 
      print("Triangulo obtusangulo")
