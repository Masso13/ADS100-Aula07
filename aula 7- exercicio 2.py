opcao = int(input('''
(1) Celsius para Kelvin
(2) Celsius para Fahrenheit
(3) Fahrenheit para Celsius

>'''))

if opcao == 1:
    c = float(input("Digite o valor em Celsius: "))
    k = c+273
    print(f"A conversão de {c}°C para Kelvin é de {k}")
elif opcao == 2:
    c = float(input("Digite o valor em Celsius: "))
    f = c*1.8+32
    print(f"A conversão de {c}°C para Fahrenheit é de {f}")
elif opcao == 3:
    f = float(input("Digite o valor em Fahrenheit: "))
    c = (f-32)/1.8
    print(f"A conversão de {f}°F para Celsius é de {c}°C")
else:
    print("Não existe essa opção !")