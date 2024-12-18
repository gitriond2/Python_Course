import cv2 , time, pandas
from datetime import datetime


first_frame=None
status_list=[None,None]
times=[]
df=pandas.DataFrame(columns=["Start","End"])

video=cv2.VideoCapture(0)

a=0

while True:
    a=a+1
    check, frame= video.read()
    status=0

    #print(check)
    #print(frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue   
  
    
    delta_frame=cv2.absdiff(first_frame,gray)

    thresh_delta=cv2.threshold(delta_frame,30,255, cv2.THRESH_BINARY)[1]

    thresh_delta=cv2.dilate(thresh_delta, None, iterations=2)

    (cnts,_) =cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status=1         
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)
    status_list.append(status)

    
    status_list= status_list[-2:]           #part graph

    if status_list[-1]== 1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]== 0 and status_list[-2]==1:
        times.append(datetime.now())


    #cv2.imshow("GrayFrame",gray)                    #deteccion de grises
    #cv2.imshow("DeltaFrame",delta_frame)           #deteccion de marco        
    cv2.imshow("Threshold Frame",thresh_delta)       #deteccion de contraste
    cv2.imshow("Color Frame",frame)                 #

    key=cv2.waitKey(1)

    #print(gray)
    #print(delta_frame)

    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break

#print(status_list)      #cambie de "status" a
#print(times)

for i in range(0,len(times),2):
    df = pandas.concat([df, pandas.DataFrame([{"Start": times[i], "End": times[i+1]}])], ignore_index=True)

df.to_csv("Times.csv",index=False)

video.release()

cv2.destroyAllWindows()