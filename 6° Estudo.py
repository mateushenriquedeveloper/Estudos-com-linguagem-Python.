velocidade = float(input("Qual velocidade atuual do carro:"))
if velocidade > 80:
    print('Multado! você ultrapassou o limite permitido que é 80Km/h')
    multa = (velocidade-80) * 7
    print("Você deve pagar uma multa de R${:.2f}!".format(multa))
print("Tenha um bom dia! dirija com segurança.")