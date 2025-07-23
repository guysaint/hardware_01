import turtle
import math
import serial
import time
import random

# 시리얼 통신 코드
connection = None
current_distance = 0

def connect_sensor(port='COM10'):
    global connection
    try:
        connection = serial.Serial(port, 9600, timeout=0.05)
        time.sleep(0.1)
        print("연결 성공")
        return True
    except:
        print("연결 실패")
        return False

def read_distance():
    global connection, current_distance
    if connection:
        
        try:
            data = connection.readline().decode().strip()
            distance = float(data)
            current_distance = distance
            return distance
        except:
            pass
    return None

def main():
    if connect_sensor():
       
        while True:
            dist = read_distance()
            if dist is not None:
                turtle_move(dist)
                print(f"거리: {dist}cm")
                if t.distance(325, 275) < 20:
                   print("도착!")
                   break  # 루프 탈출
            time.sleep(0.05)

 # 스크린 생성
s = turtle.getscreen()
#거북이 변수에 지정, 거북이 초기 설정
t = turtle.Turtle()
t.color("blue")
t.shape("turtle")
t.shapesize(1.5,1.5,1.5)
x1 = t.xcor() # 거북이의 실시간 x좌표
y1 = t.ycor() # 거북이의 실시간 y좌표

#시작점 그리기
t.penup()
t.goto(-300,-300)
t.pendown()
t.circle(30)
t.penup()

#도착점 그리기
t.goto(300,300)
t.pendown()
for i in range(4):
    t.fd(50)
    t.rt(90)
t.penup()

#거북이 시작점으로 이동
t.goto(-300,-270)
t.pendown()



#초음파 센서 거리 값에 따른 동작
def turtle_move(dist):
    if dist <= 5:
        avoid_obstacle()  # 장애물 감지되면 회피
    elif t.distance(325, 275) > 20:
        t.setheading(t.towards(325, 275))
        t.fd(10)
        
#장애물 회피 알고리즘
def avoid_obstacle():
    #장애물 회피 행동
    print("장애물 감지! 회피 시작")
    
    #1단계: 랜덤한 회전 각도 생성(30~150도)
    turn_angle = random.randint(30,150)
    print(f"회전 각도:{turn_angle}도")
    
    #2단계
    direction = random.choice([1,-1]) #1=좌회전, -1=우회전
    
    if direction == 1:
        t.lt(turn_angle)
        print(f"좌회전 {turn_angle}도")
        
    else:
        t.rt(turn_angle)
        print(f"우회전 {turn_angle}도")
        
    #3단계: 회전 후 안전 거리만큼 이동
    move_distance = random.randint(20,50)
    t.fd(move_distance)
    print(f"{move_distance}픽셀 이동 완료")


main()   