# love calculator
couple1 = "amada and parker "
Y1 = 2
P1 = 4
Hm1 = 1
Mf1 = .5
J1 = 1
G1 = .75
Sm1 = .75
Sf1 = .75
I1 = .75
C1 = .25
couple2 = "Rina and Spencer "
Y2 = 1/12
P2 = 2
Hm2 = 1
Mf2 = .40
J2 = 1
G2 = .1
Sm2 = .50
Sf2 = .50
I2 = .75
C2 = .25


def love_calculator(couple, Y, P, Hm, Mf, J, G, Sm, Sf, I, C):
    L = 8 + .5 * Y - .2 * P + .9 * Hm + .3 * Mf + J - .3 * G - (Sm - Sf) + I + 1.5 * C
    print("L= ")
    print(L)
    if L < 1:
        return couple + "are not compatible"
    elif 1 < L < 2:
        return couple + "may be compatible"
    else:
        return couple + "are very compatible"


Result1 = love_calculator(couple1, Y1, P1, Hm1, Mf1, J1, G1, Sm1, Sf1, I1, C1)
print (Result1)
Result2 = love_calculator(couple2, Y2, P2, Hm2, Mf2, J2, G2, Sm2, Sf2, I2, C2)
print (Result2)
