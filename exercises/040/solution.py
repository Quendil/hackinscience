import operator
x = 0
for i in range(0, 101):
    if i % 2 == 0:
        x = operator.add(x, i)
print(x)
