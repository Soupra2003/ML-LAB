import cv2

def gray_scale():
    img = cv2.imread('tree.jpg')
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray_img.jpg',gray_img)
    cv2.imshow('Gray_img',gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def resize():
    img  = cv2.imread('tree.jpg')
    resized_img = cv2.resize(img,(300,500))
    cv2.imwrite('resized_img.jpg',resized_img)
    cv2.imshow('Resized_img',resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def draw_img():
    img = cv2.imread('tree.jpg')
    cv2.rectangle(img,(0,0),(150,100),(255,0,0),5)
    cv2.circle(img,(200,200),50,(0,255,0),-1)
    cv2.line(img,(0,0),(300,300),(0,0,255),5)
    cv2.imwrite('draw_img.jpg',img)
    cv2.imshow('Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

draw_img()
def rotate_img():
    img = cv2.imread('tree.jpg')
    height, width = img.shape[:2]
    center = (width // 2, height // 2)
    angle = 180
    scale = 1.0
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
    rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))
    cv2.imwrite('rotated_img.jpg',rotated_img)
    cv2.imshow('Rotated_img',rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


