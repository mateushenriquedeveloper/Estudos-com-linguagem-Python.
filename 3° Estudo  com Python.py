num = int(input("informe um número:"))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("Analisando o número {}".format(num))
print("Unidade: \033[0;31;40m{}".format(u))
print("Dezena: \033[0;32;40m{}".format(d))
print("Centena: \033[0;33;40m{}".format(c))
print("Milhar: \033[0;34;40m{}".format(m))