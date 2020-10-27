n = input()
k = len(n)
for a in range(0, k-1):
    if n[a]=='н':
        print('n first')
        break
    elif n[a] == 'к':
        print('k first')
        break
    else:
        continue