numero = int(input())

if numero < 0:
    print('impossível!')
    print('não precisa se alistar.')
elif numero < 18:
    print('não precisa se alistar.')
elif numero > 18 and numero < 65:
    print('Não esqueça de votar na próxima eleição.')
elif numero > 65:
    print('Vá descansar.')
else:
    print('eita!')
    