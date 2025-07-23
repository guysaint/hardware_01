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
    if dist > 5 and t.distance(325,275) > 20: #거리가 5cm 이상이고 도착점에 도달하지 못했을 때
        t.setheading(t.towards(325, 275)) #거북이 머리 방향을 도착점으로
        t.fd(10)
        

main()   