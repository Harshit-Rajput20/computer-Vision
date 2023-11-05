import cv2

img = cv2.imread("ironman_lob_mas_hlf_02_0.jpg",0)
cv2.imshow("original",img)
k=cv2.waitKey(0)

if(k=='s'):
    
    cv2.imwrite("/home/harshit/harshit/computer Vision/output.jpg",img)
    
else:    
    cv2.destroyAllWindows()