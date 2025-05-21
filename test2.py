import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  #yüz için kaynak dosyaları kullanımı için ayrı bir nesne
eye_cascade=cv2.CascadeClassifier("saggoz.xml")                     #göz için kaynak dosyaları
mouth_cascade=cv2.CascadeClassifier("haarcascade_mouth.xml")                 #ağız için kaynak dosyaları

kamera=cv2.VideoCapture(0)          #openCV deki video yakalama fonksiyonunu kolay kullanım için bir nesneye atama.
while True:
    _,goruntu=kamera.read()         #openCV deki video yu okuma diye adlandırdığımız read fonk. yine bir nesneye atama işlemi.
    gray = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)  #yakalanan goruntu griye döndürülüyor
    faces= face_cascade.detectMultiScale(gray,1.1,5)  #bu fonksiyonla algılama için gerekli koordinatlar
    eyes=eye_cascade.detectMultiScale(gray,1.3,6)
    mouths=mouth_cascade.detectMultiScale(gray,1.3,2)
    cv2.putText(goruntu,"Koordinatlar:(x,y)",(350,415),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,150),1)
    for (x,y,w,h) in faces:  #gerekli koordinatların değerlere atanması
        cv2.rectangle(goruntu,(x,y),(x+w,y+h),(0,255,0),1) #yüz için verilen koordinatlara bağlı dikdörtgen çizimi
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=goruntu[y:y+h,x:x+w]
        x=(2*x+w)/2         #verilen çerçevede orta nokta bulma işlemi 
        y=(2*y+h)/2
        x=int(x)
        y=int(y)
        cv2.circle(goruntu,(x,y),2,(0,250,0),-1)
        ba="face:"+str(x)+","+str(y)    #putText için float-string dönüşümü
        cv2.putText(goruntu,ba,(350,430),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
        
        for(ex,ey,ew,eh) in eyes:
            ey+=10 #çerçevlerin daha küçük olması için değerlerde küçültme 
            
            cv2.rectangle(goruntu,(ex,ey),(ex+ew,ey+eh),(255,0,0),1)  #gözler için verilen koordinatlara bağlı dikdörtgen çizimi
            ex=(2*ex+ew)/2
            ey=(2*ey+eh)/2
            ex=int(ex)
            ey=int(ey)
            cv2.circle(goruntu,(ex,ey),2,(0,250,0),-1)
            eb="eyes:"+str(ex)+","+str(ey)
            cv2.putText(goruntu,eb,(350,445),cv2.FONT_HERSHEY_COMPLEX,0.5,(150,0,150),1)
            i=0 
            for(mx,my,mw,mh) in mouths:
        
                i+=1
                cv2.rectangle(goruntu,(mx,my),(mx+mw,my+mh),(150,150,150),1)  #ağız için verilen koordinatlara bağlı dikdörtgen çizimi
                mx=(2*mx+mw)/2
                my=(2*my+mh)/2
                mx=int(mx)
                my=int(my)
                cv2.circle(goruntu,(mx,my),2,(0,250,0),-1)
                ma="mouth:"+str(mx)+","+str(my)
                cv2.putText(goruntu,ma,(350,460),cv2.FONT_HERSHEY_COMPLEX,0.5,(150,150,150),1)
                if i==1:
                    break 
    cv2.imshow("Hasan Mert Oktem",goruntu)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
       break
    
kamera.release()
cv2.destroyAllWindows()