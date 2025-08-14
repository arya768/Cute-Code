# Cute-Code
name = input('Enter the name you want in the heart: ')

print('\n'.join(
    [''.join(
        [name[(x - y) % len(name)] if ((x * 0.04)**2 + (y * 0.1)**2 - 1)**3 - (x * 0.04)**2 * (y * 0.1)**3 <= 0 else ' '
         for x in range(-30, 30)])
     for y in range(15, -15, -1)]
))

print("\nYour name in a heart ❤️")

