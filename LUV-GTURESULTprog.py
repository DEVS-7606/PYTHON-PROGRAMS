n = int(input('enter the number of subject'))
SM = []
SC = []
GradePoint_list = []
Grade_list = []
CiGi = []
a = 0
b = 0
i=1
while n>0 :
    print('subject', i, ':-')
    sm = int(input('enter the subject marks'))
    sc = int(input('enter the subject credits'))
    SM.append(sm)
    SC.append(sc)
    n=n-1
    i=i+1

for i in range(0, len(SM)):
    if 85 <= SM[i] <= 100:
        Grade = 'AA'
        GradePoint = 10
        print('grade' + str(i + 1) + ':' + Grade)
        GradePoint_list.append(GradePoint)
        Grade_list.append(Grade)

    if 75 <= SM[i] <= 84:
        Grade = 'AB'
        GradePoint = 9
        print('grade' + str(i + 1) + ':' + Grade)
        GradePoint_list.append(GradePoint)
        Grade_list.append(Grade)

    if 65 <= SM[i] <= 74:
        Grade = 'BB'
        GradePoint = 8
        print('grade' + str(i + 1) + ':' + Grade)
        GradePoint_list.append(GradePoint)
        Grade_list.append(Grade)

    if 55 <= SM[i] <= 64:
        Grade = 'BC'
        GradePoint = 7
        print('grade' + str(i + 1) + ':' + Grade)
        GradePoint_list.append(GradePoint)
        Grade_list.append(Grade)

    if 45 <= SM[i] <= 54:
        Grade = 'CC'
        GradePoint = 6
        print('grade' + str(i + 1) + ':' + Grade)
        GradePoint_list.append(GradePoint)
        Grade_list.append(Grade)

    if 40 <= SM[i] <= 44:
        Grade = 'CD'
        GradePoint = 5
        print('grade' + str(i + 1) + ':' + Grade)
        GradePoint_list.append(GradePoint)
        Grade_list.append(Grade)

    if 35 <= SM[i] <= 39:
        Grade = 'DD'
        GradePoint = 4
        print('grade' + str(i + 1) + ':' + Grade)
        GradePoint_list.append(GradePoint)
        Grade_list.append(Grade)

    if SM[i] < 35:
        Grade = 'FF'
        GradePoint = 0
        print('grade' + str(i + 1) + ':' + Grade)
        GradePoint_list.append(GradePoint)
        Grade_list.append(Grade)

for i in range(0, len(SM)):
    CiGi.append(SC[i] * GradePoint_list[i])
    b += CiGi[i]
    a += SC[i]

SPI = b / a

print('Total SPI:-', SPI)