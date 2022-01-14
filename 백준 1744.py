N = int(input())

numbers = sorted([int(input()) for _ in range(N)])

plus = []
minus = []

while N > 0:
    tmp = numbers.pop()
    if tmp > 0:
        plus.append(tmp)
    else:
        minus.append(tmp)
    N -= 1

plus = sorted(plus)
minus = sorted(minus, key=lambda x: -x)

total = 0

P = len(plus)
M = len(minus)

while P > 1:
    tmp1 = plus.pop()
    tmp2 = plus.pop()
    if tmp1 * tmp2 > tmp1 + tmp2:
        total += tmp1 * tmp2
    else:
        total += tmp1 + tmp2
    P -= 2

if P:
    total += plus.pop()

while M > 1:
    tmp1 = minus.pop()
    tmp2 = minus.pop()
    if tmp1 * tmp2 > tmp1 + tmp2:
        total += tmp1 * tmp2
    else:
        total += tmp1 + tmp2
    M -= 2

if M:
    total += minus.pop()

print(total)