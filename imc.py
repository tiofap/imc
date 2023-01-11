p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))
imc = p / (a**2) * 1000
print('Seu IMC: {:.2f}'.format(imc))

c = str(input('Deseja ver sua classificação?'))
if c == 'sim' or 'Sim':
    print('Ok, vamos lá')
elif c == 'não' or 'nao':
    print('Tudo bem, até a próxima')
else:
    print('Não entendi a resposta, digite: sim ou não')

ca = float(input('Digite seu IMC: '))
if ca <=1.85:
    print('Sua classificação: Magreza')
elif ca >=1.85 and ca<=0.00249:
    print('Sua classificação: Normal')
elif ca >=2.50 and ca<=0.00299:
    print('Sua classificação: Sobrepeso')
elif ca >=3.00 and ca<=3.99:
    print('Sua classificação: Obesidade')
elif ca >=4.00:
    print('Sua classificação: Obesidade Grave')














