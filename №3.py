import math
CenterKruga = list(input("Введите координаты центра круга(например 0,0) "))
CenterKruga.remove(',')

rad=int(input("Введите радиус круга "))

TA= list(input("Введите координаты 1-й вершины круга(например 0,0) "))
TA.remove(',')
a1=int(TA[0])
a2=int(TA[1])

TB= list(input("Введите координаты 2-й вершины круга(например 0,0) "))
TB.remove(',')
b1=int(TB[0])
b2=int(TB[1])

TC= list(input("Введите координаты 3-й вершины круга(например 0,0) "))
TC.remove(',')
c1=int(TC[0])
c2=int(TC[1])

RTA=math.sqrt(a1**2+a2**2)
RTB=math.sqrt(b1**2+b2**2)
RTC=math.sqrt(c1**2+c2**2)

if rad>RTA and rad>RTB and rad>RTC:
    print("Треугольник расположен в окружности")
elif rad==RTA and rad==RTB and rad==RTC:
    print("Треугольник расположен на окружности")
elif rad<RTA and rad==RTB and rad==RTC:
    print("Треугольник расположен за окружностью")
elif (RTA>rad and RTB<rad and RTC<rad) or (RTA<rad and RTB>rad and RTC<rad) or (RTA<rad and RTB<rad and RTC>rad):
    print("Вершина треугольника выходит за окружность")
elif (RTA<rad and RTB>rad and RTC>rad) or (RTA>rad and RTB<rad and RTC>rad) or (RTA>rad and RTB>rad and RTC<rad):
    print("Вершина треугольника входит в окружность")
elif (RTA==rad and RTB>rad and RTC>rad) or (RTA>rad and RTB==rad and RTC>rad) or (RTA>rad and RTB>rad and RTC==rad):
    print("Вершина треугольника касается окружностью")
