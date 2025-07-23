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
        connection = serial.Serial(port, 9600)
        time.sleep(2)
        print("연결 성공")
        return True
    except:
        print("연결 실패")
        return False

def read_distance():
    global connection, current_distance
    if connection and connection.in_waiting > 0:
        data = connection.readline().decode().strip()
        try:
            distance = float(data)
            current_distance = distance
            return distance
        except:
            pass
    return None

def main():
    if connect_sensor():
        for i in range(100):
            dist = read_distance()
            if dist:
                print(f"거리: {dist}cm")
            time.sleep(0.1)
            return dist

if __name__ == "__main__":
    main()
    
# 스크린 생성
s = turtle.getscreen()
#거북이 변수에 지정, 거북이 초기 설정
t = turtle.Turtle()
t.color("blue")
t.shape("turtle")
t.shapesize(1.5,1.5,1.5)


#시작점 그리기

#도착점 그리기

#거북이 이동

#초음파 센서 거리 값에 따른 동작
