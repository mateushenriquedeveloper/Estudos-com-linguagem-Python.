n1 = int(input("Informe sua 1° nota:"))
n2 = int(input("Informe sua 2° nota:"))
n3 = int(input("Informe sua 3° nota:"))
n4 = int(input("Informe sua 4° nota:"))
m = (n1 + n2 + n3 + n4) / 4
print("A sua média foi:{}".format(m))
if m >= 60:
  print("Você está acima da média!")
else:
  print("Você está abaixo da média!")