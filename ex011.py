# Pintando Parede

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2

print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.3f}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.4f}l de tinta.'.format(tinta))
 