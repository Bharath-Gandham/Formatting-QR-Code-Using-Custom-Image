import cv2
import numpy as np
def main():
    
    image = cv2.imread("whiteandblack.jpeg")##Your QR Code
    image2=cv2.imread("image2.jpg")##Your custom Image
    blank_image=imageRelated(image,image2)
    cv2.imshow("Image3",blank_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def imageRelated(image, image2):
    height,width,depth=image.shape
    width2=int(width)
    height2=int(height)
    blank_image = np.ones((height,width,3), np.uint8)*255##Newly created blank Image of color white
    dimension=(width2,height2)
    resized=cv2.resize(image2,dimension,interpolation=cv2.INTER_AREA)
    height2,width2,depth2=resized.shape
    print("height",height,height2)
    print("width",width,width2)
    print("depth",depth,depth2)

    ##cv2.imwrite("newFileName.jpeg",returnedone)##Writing file to disk/local
    heightnew=0
    widthnew=0
    for i in range(0,height):
        for j in range(0,width):
            px=image[i,j]
            if(px[0]<=12 and px[1]<=12 and px[2]<=12):
                blank_image[i,j] = resized[i,j]##here you can do minus
            
            
    cv2.imshow("Image",image)
    cv2.imshow("Image2",resized)
    return blank_image
    #cv2.imshow("Image3",blank_image)
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
    
main()
