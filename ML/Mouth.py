import cv2
import numpy as np
import dlib
import math
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
def distance(x1, y1, x2, y2):
    part1 = math.pow((x1-x2), 2)
    part2 = math.pow((y1-y2), 2)
    dist = math.pow((part1 + part2) , 0.5)
    return dist

def check(mouth):
    count1 = mouth.count("closed")
    count2 = mouth.count("open")
    if(count1==8):
        print("Mouth Closed")
        print(mouth)
    elif(count2==8):
        print("Mouth open")
        print(mouth)
    elif(count2 != count1 and (count1==1 or count2==1)):
        print("Talking suspected")
        print(mouth)
    elif(count2 != count1 and (count1 > 1 or count2 > 1)):
        print("Talking confirmed")
        print(mouth)
    
mouth_Stats = []
fc = 0
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 3)
        
        landmarks = predictor(gray, face)
        for n in range(48,68):
            
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x,y), 4, (255,0,0), -1)
        if(len(faces)==1):
            left_x1 = landmarks.part(61).x
            left_x2 = landmarks.part(67).x
            left_y1 = landmarks.part(61).y
            left_y2 = landmarks.part(67).y
            mid_x1 = landmarks.part(62).x
            mid_x2 = landmarks.part(66).x
            mid_y1 = landmarks.part(62).y
            mid_y2 = landmarks.part(66).y
            right_x1 = landmarks.part(63).x
            right_x2 = landmarks.part(65).x
            right_y1 = landmarks.part(63).y
            right_y2 = landmarks.part(65).y
            dist1 = distance(left_x1,left_y1,left_x2,left_y2)
            dist2 = distance(mid_x1,mid_y1,mid_x2,mid_y2)
            dist3 = distance(right_x1,right_y1,right_x2,right_y2)
            if(dist1<=8 and dist2<=8 and dist3<=8 and fc<=8):
                fc = fc + 1
                mouth_Stats.append("closed")
            elif(dist1>8 and dist2>8 and dist3>8 and fc<=8):
                fc = fc + 1
                mouth_Stats.append("open")
            if(fc==8):
                check(mouth_Stats)
                mouth_Stats = []
                fc = 0
            
            
            
    
    cv2.imshow("Frame", frame)
    if(cv2.waitKey(1) & 0xFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
    
