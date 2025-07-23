const int trigPin = 9;
const int echoPin = 10;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

float getStableDistance(int count = 5) {
  float sum = 0;
  int validCount = 0;

  for (int i = 0; i < count; i++) {
    // 트리거 펄스
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    // 에코 대기
    long duration = pulseIn(echoPin, HIGH, 30000); // 최대 30ms (약 5m)
    if (duration > 0) {
      float dist = (duration * 0.0343) / 2;
      // 유효 범위 (예: 2cm ~ 400cm)
      if (dist >= 2 && dist <= 400) {
        sum += dist;
        validCount++;
      }
    }
    delay(10); // 센서 안정화 시간
  }

  if (validCount == 0) return -1.0;  // 유효값 없음
  return sum / validCount;
}

void loop() {
  float distance = getStableDistance(5);
  if (distance > 0) {
    Serial.println(distance);  // 파이썬으로 전송
  } else {
    Serial.println("NaN");     // 오류 표시
  }
  delay(100);  // 너무 자주 보내면 버퍼 터질 수 있음
}
