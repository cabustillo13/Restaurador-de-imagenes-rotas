import numpy as np
import cv2

# Imagen a restaurar
image = cv2.imread('mural.jpg')

# Mascara
mask = cv2.imread('mask_mural.png',0)

# La mascara debe tener las mismas dimensiones que la imagen a restaurar
height, width, channels = image.shape
mask = cv2.resize(mask, (width, height))         

restauracion1 = cv2.inpaint(image,mask,3,cv2.INPAINT_TELEA)
restauracion2 = cv2.inpaint(image,mask,3,cv2.INPAINT_NS)

cv2.imwrite("./restauracion1.jpg", restauracion1) 
cv2.imwrite("./restauracion2.jpg", restauracion2)

#cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows() 
