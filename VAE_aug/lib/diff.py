import cv2
im1 = cv2.imread('im1.png')
im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
im2 = cv2.imread('im2.png')
im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
im2 = cv2.resize(im2, (im1.shape[1], im1.shape[0]))
fin = cv2.subtract(im1,im2)
cv2.imwrite('fin.png', fin)
