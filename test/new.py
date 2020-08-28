import datetime
y = str(input("y: ")).split()

x = datetime.datetime(int(y[0]), int(y[1]), int(y[2]))

print(x.strftime("%Y-%m-%d"))
