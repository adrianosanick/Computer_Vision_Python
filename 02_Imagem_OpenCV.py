import cv2

img = cv2.imread('animals/00_Connie.jpg')

while True:

    cv2.imshow('Connie',img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
