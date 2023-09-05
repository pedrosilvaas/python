# Aluguel de carros

km = int(input('Digite quantos km você rodou: '))
dias = int(input('Digite quantos dias você alugou: '))

price = (km * 0.15) + (dias * 60)

print(f'O total a pagar é de €{price:.2f}.')