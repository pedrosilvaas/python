import math

ang = float(input('Digite o ângulo que você deseja: '))

sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(f'O valor do seno é {sin:.2f}.')
print(f'O valor do cosseno é {cos:.2f}.')
print(f'O valor da tangente é {tan:.2f}.')