import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os


cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)
cap.set(cv2.CAP_PROP_FPS, 60)
segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()

listImg = os.listdir("images")
print (listImg)
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'images/{imgPath}')
    imgList.append(img)
print(len(imgList))

indexImg = 0
while True:
    success, img = cap.read()

    imgOut = segmentor.removeBG(img, imgList[indexImg], threshold =0.5)
    imgStacked = cvzone.stackImages([img, imgOut],2,1)
    _, imageStacked = fpsReader.update(imgStacked, color= (0, 0, 255))

    cv2.imshow("Image" , imgStacked)

    cv2.waitKey(1)