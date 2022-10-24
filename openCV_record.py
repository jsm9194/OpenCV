import cv2
cap = cv2.VideoCapture(0)
if cap.isOpened: # 성공적으로 열리면 트루 아니면 False
 file_path = 'record.avi' #이걸로 저장
 fps = 30.0
 fourcc = cv2.VideoWriter_fourcc(*'DIVX')
 width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
 height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
 size = (int(width), int(height)) # 비디오가 정하고있는 가로, 높이
 out = cv2.VideoWriter(file_path, fourcc, fps, size)

 while True: #무한반복
     ret, frame = cap.read()  #읽어온다 > 프레임으로 읽어옴
     if ret:
         cv2.imshow('camera-recording',frame)  #캡쳐성공이면 보여줌
         out.write(frame)
         if cv2.waitKey(int(1000/fps)) != -1: # 키입력 대기 없으면 0.33초뒤에 자동리턴값
             break
     else:
         print("no frame!")
         break
 out.release() # 작업 닫기
else:
 print("can't open camera!")
cap.release()
cv2.destroyAllWindows()