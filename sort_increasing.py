ln = int(input('Enter no. of Values: '))
nos = [0]
for l in range(1, ln + 1):
    nos.append(int(input(f'Enter {l}th no: ')))
nos.remove(0)
print(f'Original: {nos}')
ch = 0
while ch < len(nos) - 1:
    ch2 = ch + 1
    while ch2 < len(nos):
        if nos[ch] > nos[ch2]:
            temp = nos[ch]
            nos[ch] = nos[ch2]
            nos[ch2] = temp
        ch2 += 1
    ch += 1
print(f'New: {nos}')
