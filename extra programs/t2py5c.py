n = 5
stars = [('*' + '**'*i).center(2*n + 1) for i in range(n)]

print('\n'.join(stars + stars[::-1][1:]))
print(stars[1:-1])
