ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))
idade = 2023-ano_nascimento

if idade <= 9:
    categoria = "Mirim"
elif 9 < idade <= 19:
    categoria = "Júnior"
elif 19 < idade <= 25:
    categoria = "Sênior"
else:
    categoria = "Master"

print(f"O atleta possui {idade} anos, então a sua categoria é {categoria}")