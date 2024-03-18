import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

_, frame = cap.read()
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
rows ,cols, chanel = frame.shape
writer = cv2.VideoWriter("output/2_output.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (cols, rows))

while True:
    ret, frame = cap.read()
    
    frame[220:260,300:305] = 0
    frame[220:225,300:340] = 0
    frame[260:265,300:340] = 0
    frame[220:265,340:345] = 0

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    check_h = frame[225:260,305:340, 0]
    print(np.average(check_h),"h")
    check_s = frame[225:260,305:340, 1]
    print(np.average(check_s),"s")
    check_v = frame[225:260,305:340, 2]
    print(np.average(check_v),"v")

    if 65 <= np.average(check_h) <= 80 and 10 <= np.average(check_s) <= 45 and 20 <= np.average(check_v) <= 40:
        cv2.putText(frame,"Black",(280,300),cv2.FONT_ITALIC,1,(0,0,0),2)
    
    elif 50 <= np.average(check_h) <= 90 and 0 <= np.average(check_s) <= 20 and 100 <= np.average(check_v) <= 160:
        cv2.putText(frame,"White",(280,300),cv2.FONT_ITALIC,1,(0,0,0),2)
    
    elif 155 <= np.average(check_h) <= 180 and 160 <= np.average(check_s) <= 190 and 90 <= np.average(check_v) <= 175:
        cv2.putText(frame,"Red",(280,300),cv2.FONT_ITALIC,1,(0,0,0),2)
    
    elif 60 <= np.average(check_h) <= 70 and 110 <= np.average(check_s) <= 150 and 50 <= np.average(check_v) <= 110:
        cv2.putText(frame,"Green",(280,300),cv2.FONT_ITALIC,1,(0,0,0),2)

    elif 110 <= np.average(check_h) <= 125 and 40 <= np.average(check_s) <= 100 and 50 <= np.average(check_v) <= 80:
        cv2.putText(frame,"Blue",(280,300),cv2.FONT_ITALIC,1,(0,0,0),2)

    elif 10 <= np.average(check_h) <= 30 and 180 <= np.average(check_s) <= 195 and 90 <= np.average(check_v) <= 130:
        cv2.putText(frame,"Yellow ",(280,300),cv2.FONT_ITALIC,1,(0,0,0),2)

    if not ret:
        break

    frame = cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)
    writer.write(frame)
    cv2.imshow("result", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

writer.release()