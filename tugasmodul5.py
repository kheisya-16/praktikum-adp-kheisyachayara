x = [i for i in range(-7,8)]
fx = []
for i in x :
    if i > 0 :
        fx.append(i**3-i)
    elif i < 0 :
        fx.append(1 /(i**2))
    else :
        fx.append(1)
print("|  x |  f(x) |")
for i in range(len(x)):
    print("|", end=" ")
    print(f"{x[i]:<2}", end=" | ")
    print(f"{fx[i]:<6.2f}|")