import cv2
capture = cv2.VideoCapture(0)
# 비디오 캡려 장치번호 0

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# 프레임 가로너미
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# 프레임 세로너비

while cv2.waitKey(33) < 0: #입력된 키값 > 뭐라도 키를 입력하면 실행꺼짐
     ret, frame = capture.read() # 계속프레임을 저장
     cv2.imshow("VideoFrame", frame) # 계속 화면에 출력

capture.release() # 카메라 장치에서 받아온 메모리를 해제한다
cv2.destroyAllWindows() # 와일문끝나면 화면꺼짐

