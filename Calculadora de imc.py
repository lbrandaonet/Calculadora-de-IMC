n1 = (input("Qual o seu nome?"))
print('Olá, {}'.format (n1))

n2 = float(input('Insira sua altura em metros:'))
n3 = float(input('Insira seu peso em kg:'))

imc = n3/n2**2  
print("Seu IMC é: %.2f" % imc) 

if imc < 16:
    print('Você está com magreza grave, recomenda-se procurar um especialista')

elif imc < 17:
    print('Você está com magreza moderada, recomenda-se procurar um especialista')

elif imc < 18.5:
    print('Você está com magreza leve, se preferir procure um especialista')

elif imc < 25:
    print('Você está saudável')

elif imc < 30:
    print('Você está com sobrepeso, se preferir procure um especialista')

elif imc < 35:
    print('Você está com obesidade grau I, recomenda-se procurar um especialista')

elif imc < 40:
    print('Você está com obesidade grau II, recomenda-se procurar um especialista')
    
elif imc > 40:
    print('Vcê está com obesidade grau III, recomenda-se procurar um especialista') 
