import matplotlib.pyplot as plt 
 
x = []
y = []

sty = 0
n = 27
step = 0
 
#plt.plot(x, y) 
#plt.show()
while True:
    if n % 2 == 0:
        new_n = n / 2
        step += 1
    else:
        new_n = (3 * n) + 1
        step += 1
    n = new_n
    print(step, n)
    y.append(n)

    if n == 1:
        break

for st in range(step):
    sty += 1
    x.append(sty)

print(x)
print(y)
plt.plot(x, y) 
plt.show()