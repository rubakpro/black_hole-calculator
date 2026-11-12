from decimal import Decimal, getcontext
getcontext().prec = 200
c = Decimal('299792458')
G = Decimal('0.000000000066743')
hbar = Decimal('0.000000000000000000000000000000000105457')
pi = Decimal('3.141592653589793238462643383279')
r = Decimal(input("радиус Шварцшильда (в метрах): ").replace(",", "."))
vibor = ["1 масса черной дыры, 2 время полного испарения , 3 средняя плотность"]
print(vibor)
vibor = int(input())
M = (c ** 2 * r) / (Decimal('2') * G)
if vibor == 1:
    print(M , "кг")
elif vibor == 2:
    t_ev = (Decimal('5120') * pi * (G ** 2) * (M ** 3)) / (hbar * (c ** 4))
    print(t_ev , "секунд" )
elif vibor == 3:
    rho = (Decimal('3') * (c ** 6)) / (Decimal('32') * pi * (G ** 3) * (M ** 2))
    print(rho , "кг/м³")

