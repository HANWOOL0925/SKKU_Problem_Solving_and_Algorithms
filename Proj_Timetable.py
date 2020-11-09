# 사용자의 선택을 바탕으로 랜덤으로 시간표를 짠 후 turtle로 보여주는 코드

bsm=["선형대수학(3)","확률및통계(3)","미분적분학1(3)","일반물리1(3)","일반화학1(3)","생명과학1(3)"]
com=["창의적글쓰기(2)","학술적글쓰기(2)","스피치와토론(2)","과학기술글쓰기(2)"]
crea=["일반논리학(2)","기호논리학(2)","창의적발상(2)","비판적사고(2)"]
assign=["영어쓰기(2)","컴퓨팅사고와코딩(2)","FYE세미나1(1)"]
recommend=[]

count=0
start=int(input("안내 책자를 읽으셨습니까?(Yes-1/N0-2):"))
if start==2:
    reask=int(input("안내책자를 읽고 Yes(1)를 눌러주세요."))
    if reask==1:
        count+=1
else:
    count+=1

if count==1:
    a=int(input("기초자연 과목 중 수학만 듣고 싶은 경우 1을 입력하시고, 과학만 듣고 싶은 경우 2, 모두 듣고 싶은 경우 3을 입력해주세요.:"))
    if a==1:
        recommend+=bsm[0:3]
    elif a==2:
        recommend+=bsm[3:6]
    else:
        b=int(input("물리(1), 화학(2), 생명(3) 중 제외하고 싶은 과목의 번호를 입력해주세요.(1/2/3):"))
        recommend+=bsm[2:6]
        recommend.pop(b)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
c=int(input("문법과 글쓰기(1), 비판적사고와 글쓰기(2), 스피치와 토론(3), 논문작성 및 연구(4) 중 원하는 교양과목을 골라주세요.(1/2/3/4):"))
recommend+=com[c-1:c]
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print("창의적사유에 해당하는 과목들에 대해 설명을 드리겠습니다.\n1.일반논리학은 연역법과 귀납법을 중심으로 논리를 배우는 과목입니다.\n2.기호논리학은 논리적 구조들을 기호들로 표현하는 과목입니다.\n3.창의적발상은 발명의 아이디어를 체계적으로 배우는 과목입니다.\n4.비판적사고는 논리적 연결관계를 파악하여 글의 구조를 파악하는 과목입니다.")
d=int(input("일반논리학(1), 기호논리학(2), 창의적발상(3), 비판적사고(4) 중 원하는 과목의 번호를 입력해주세요.(1/2/3/4):"))
recommend+=crea[d-1:d]
recommend+=assign[:3]
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(recommend, "로 총 18학점을 추천드립니다.")
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print("시간표 배치를 시작하겠습니다. 영어쓰기와 컴퓨터사고와코딩은 직권배정 과목입니다.")

day1=['월1, 수2','월2 , 수1','월3 , 수4','월4 , 수3','월5 , 수6','월6 , 수5','화1, 목2','화2 , 목1','화3 , 목4','화4 , 목3','화5 , 목6','화6 , 목5','금1, 금2','금3, 금4','금5, 금6','월1, 월2','월3, 월4','월5, 월6','화1, 화2','화3, 화4','화5, 화6','수1, 수2','수3, 수4','수5, 수6','목1, 목2','목3, 목4','목5, 목6']
day2=['월1, 수2','월2 , 수1','월3 , 수4','월4 , 수3','월5 , 수6','월6 , 수5','화1, 목2','화2 , 목1','화3 , 목4','화4 , 목3','화5 , 목6','화6 , 목5','금1, 금2','금3, 금4','금5, 금6','월1, 월2','월3, 월4','월5, 월6','화1, 화2','화3, 화4','화5, 화6','수1, 수2','수3, 수4','수5, 수6','목1, 목2','목3, 목4','목5, 목6']
import random
k=random.randint(0,11)
print('영어쓰기는',day1[k], "빨간색")
del day1[21+k//2],day1[15+k//2],day1[k]


t=0
b=random.randint(11,23)
print('컴사코는',day1[b], "주황색")
for i in range(len(day2)):
    if day1[b]==day2[i]:
        t=i

if b<14:
    del day1[b]
    day1=day1[:13]

if k<6:
    if k==0 or k==1:
        if b==14:
            del day1[b], day1[2], day1[1]
        elif b==15:
            del day1[b], day1[4], day1[3]
        elif b==19:
            del day1[b], day1[2], day1[1]
        elif b==20:
            del day1[b], day1[4], day1[3]
    elif k==2 or k==3:
        if b==14:
            del day1[b], day1[1], day1[0]
        elif b==15:
            del day1[b], day1[4], day1[3]
        elif b==19:
            del day1[b], day1[1], day1[0]
        elif b==20:
            del day1[b], day1[4], day1[3]
    else:
        if b==14:
            del day1[b], day1[1], day1[0]
        elif b==15:
            del day1[b], day1[3], day1[2]
        elif b==19:
            del day1[b], day1[1], day1[0]
        elif b==20:
            del day1[b], day1[3], day1[2]
    if b==21:
        del day1[b], day1[6], day1[5]
    elif b==22:
        del day1[b], day1[8], day1[7]
    elif b==23:
        del day1[b], day1[10], day1[9]
    if b==16:
        del day1[b], day1[6], day1[5]
    elif b==17:
        del day1[b], day1[8], day1[7]
    elif b==18:
        del day1[b], day1[10], day1[9]
      
elif k<12:
    if b==14:
        del day1[b], day1[1], day1[0]
    elif b==15:
        del day1[b], day1[3], day1[2]
    elif b==16:
        del day1[b], day1[5], day1[4]
    if b==19:
        del day1[b], day1[1], day1[0]
    elif b==20:
        del day1[b], day1[3], day1[2]
    elif b==21:
        del day1[b], day1[5], day1[4]
    if k==6 or k==7:
        if b==17:
            del day1[b], day1[8], day1[7]
        elif b==18:
            del day1[b], day1[10], day1[9]
        elif b==22:
            del day1[b], day1[8], day1[7]
        elif b==23:
            del day1[b], day1[10], day1[9]
    elif k==8 or k ==9:
        if b==17:
            del day1[b], day1[7], day1[6]
        elif b==18:
            del day1[b], day1[10], day1[9]
        elif b==22:
            del day1[b], day1[7], day1[6]
        elif b==23:
            del day1[b], day1[10], day1[9]
    else:
        if b==17:
            del day1[b], day1[7], day1[6]
        elif b==18:
            del day1[b], day1[9], day1[8]     
        elif b==22:
            del day1[b], day1[7], day1[6]
        elif b==23:
            del day1[b], day1[9], day1[8]

if b>13:
    day1=day1[:len(day1)-9]


rest=[]
rest=random.sample(range(0,len(day1)),4)

bsm1=0
for i in range(len(day2)):
    if day1[rest[0]]==day2[i]:
        bsm1=i

bsm2=0
for i in range(len(day2)):
    if day1[rest[1]]==day2[i]:
        bsm2=i

bsm3=0
for i in range(len(day2)):
    if day1[rest[2]]==day2[i]:
        bsm3=i

crea=0
for i in range(len(day2)):
    if day1[rest[3]]==day2[i]:
        crea=i


print(recommend[0], day1[rest[0]], "노란색")
print(recommend[1], day1[rest[1]], "초록색")
print(recommend[2], day1[rest[2]], "파란색")
print(recommend[3], day1[rest[3]], "분홍색")

import turtle

a=turtle.Turtle()

a.speed(100000)
def graphic(k):
    for i in range(k):
        for i in range(4):
            a.forward(50)
            a.left(90)
        a.right(90)

    a.forward(100)
    for i in range(4):
        for i in range(4):
            a.forward(50)
            a.left(90)
        a.right(90)

    a.forward(50)

    for i in range(4):
        for i in range(4):
            a.forward(50)
            a.left(90)
        a.right(90)
    return a

print(graphic(4))

a.right(90)
a.forward(100)
a.right(90)

print(graphic(4))

a.left(90)
a.forward(100)
a.left(90)

print(graphic(4))


if k<6:
    a.penup()
    a.setx(-50)
    a.sety(50-50*k)
    a.fillcolor("red")
    a.begin_fill()
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.end_fill()

    a.penup()
    a.setx(50)
    a.sety(-50*k+100*(k%2))
    a.fillcolor("red")
    a.begin_fill()
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.end_fill()
    
elif k<12:
    a.penup()
    a.setx(0)
    a.sety(50-50*(k-6))
    a.fillcolor("red")
    a.begin_fill()
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.end_fill()

    a.penup()
    a.setx(100)
    a.sety(-50*(k-6)+100*((k-6)%2))
    a.fillcolor("red")
    a.begin_fill()
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.end_fill()

if t<15:
    a.penup()
    a.setx(150)
    a.sety(-100*t+1250)
    a.fillcolor("orange")
    a.begin_fill()
    a.forward(50)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(100)
    a.end_fill()

elif t>14:
    a.penup()
    a.setx((t-t%3)*(50/3)-300)
    a.sety(-100*(t%3)+50)
    a.fillcolor("orange")
    a.begin_fill()
    a.forward(50)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(100)
    a.end_fill()

if bsm1<6:
    a.penup()
    a.setx(-50)
    a.sety(-50*bsm1)
    a.fillcolor("yellow")
    a.begin_fill()
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.end_fill()

    a.penup()
    a.setx(50)
    a.sety(-50*(bsm1+1)+100*(bsm1%2))
    a.fillcolor("yellow")
    a.begin_fill()
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.end_fill()
    
elif bsm1<12:
    a.penup()
    a.setx(0)
    a.sety(-50*(bsm1-6))
    a.fillcolor("yellow")
    a.begin_fill()
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.end_fill()

    a.penup()
    a.setx(100)
    a.sety(-50*(bsm1-5)+100*((bsm1-6)%2))
    a.fillcolor("yellow")
    a.begin_fill()
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.end_fill()

elif bsm1>11:
    a.penup()
    a.setx(150)
    a.sety(-100*bsm1+1250)
    a.fillcolor("yellow")
    a.begin_fill()
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(100)
    a.end_fill()

if bsm2<6:
    a.penup()
    a.setx(-50)
    a.sety(-50*bsm2+50)
    a.fillcolor("green")
    a.begin_fill()
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.end_fill()

    a.penup()
    a.setx(50)
    a.sety(-50*bsm2+100*(bsm2%2))
    a.fillcolor("green")
    a.begin_fill()
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.end_fill()
    
elif bsm2<12:
    a.penup()
    a.setx(0)
    a.sety(-50*(bsm2-7))
    a.fillcolor("green")
    a.begin_fill()
    a.right(90)
    a.forward(50)
    a.right(90)

    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.end_fill()

    a.penup()
    a.setx(100)
    a.sety(-50*(bsm2-6)+100*((bsm2-6)%2))
    a.fillcolor("green")
    a.begin_fill()
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.end_fill()

elif bsm2>11:
    a.penup()
    a.setx(150)
    a.sety(-100*bsm2+1250)
    a.fillcolor("green")
    a.begin_fill()
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(100)
    a.end_fill()

if bsm3<6:
    a.penup()
    a.setx(-50)
    a.sety(-50*bsm3+50)
    a.fillcolor("blue")
    a.begin_fill()
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)

    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.end_fill()

    a.penup()
    a.setx(50)
    a.sety(-50*bsm3+100*(bsm3%2))
    a.fillcolor("blue")
    a.begin_fill()
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.end_fill()
    
elif bsm3<12:
    a.penup()
    a.setx(0)
    a.sety(-50*(bsm3-7))
    a.fillcolor("blue")
    a.begin_fill()
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.end_fill()

    a.penup()
    a.setx(100)
    a.sety(-50*(bsm3-6)+100*((bsm3-6)%2))
    a.fillcolor("blue")
    a.begin_fill()
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.end_fill()
    
elif bsm3>11:
    a.penup()
    a.setx(150)
    a.sety(-100*bsm3+1250)
    a.fillcolor("blue")
    a.begin_fill()
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(100)
    a.end_fill()

if crea<6:
    a.penup()
    a.setx(-50)
    a.sety(-50*crea+50)
    a.fillcolor("pink")
    a.begin_fill()
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.end_fill()

    a.penup()
    a.setx(50)
    a.sety(-50*crea+100*(crea%2))
    a.fillcolor("pink")
    a.begin_fill()
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.end_fill()
    
elif crea<12:
    a.penup()
    a.setx(0)
    a.sety(-50*(crea-7))
    a.fillcolor("pink")
    a.begin_fill()
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.end_fill()

    a.penup()
    a.setx(100)
    a.sety(-50*(crea-6)+100*((crea-6)%2))
    a.fillcolor("pink")
    a.begin_fill()
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(50)
    a.end_fill()

elif crea>11:
    a.penup()
    a.setx(150)
    a.sety(-100*crea+1250)
    a.fillcolor("pink")
    a.begin_fill()
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(100)
    a.end_fill()
