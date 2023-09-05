# Calculando descontos

price = float(input('Qual é o preço do produto? €'))
discount_price = price - (price * 0.05)

print(f'O produto que custava €{price:.2f}, na promoção com desconto de 5% vai custar €{discount_price:.2f}.')