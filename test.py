from collections import Counter

counter = 0
while counter < 3:
    shape = str(input("enter 'c' or 'b' or 'e':"))
    if shape == 'c' or shape == 'b':
        counter = +1
        W = int(input("enter the width:"))
        L = int(input('enter the length:'))
        H = int(input('enter the height:'))
        V = W * H * L
        S_A = 2 * H + W + 2 * H * L + 2 * W * L
        ve = 'Volume is:'
        se = 'SurfaceArea is:'
        print(ve + str(V))
        print(se + str(S_A))
        if counter == 3:
            print(input('if you would like to go on,type "continue":'))

        if C == 'continue':
                counter = 0
            else:
                break


    else:
        print('error"please type a letter"')

    if counter == 3:
        counter
        C = str(input('if you would like to go on,type "continue":'))
    if C =='continue':
        counter

