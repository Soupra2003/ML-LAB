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

def text_on_img():
    img = cv2.imread('tree.jpg')
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = 'Hello, OpenCV!'
    position = (50, 50)
    font_scale = 1
    color = (255, 0, 0)
    thickness = 2
    cv2.putText(img, text, position, font, font_scale, color, thickness)
    cv2.imwrite('text_on_img.jpg',img)
    cv2.imshow('Text_on_img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def blur_img():
    img = cv2.imread('tree.jpg')
    blurred_img = cv2.GaussianBlur(img, (15, 15), 0)
    cv2.imwrite('blurred_img.jpg',blurred_img)
    cv2.imshow('Blurred_img',blurred_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def edge_detection():
    img = cv2.imread('tree.jpg')
    edges = cv2.Canny(img, 100, 200)
    cv2.imwrite('edges.jpg',edges)
    cv2.imshow('Edges',edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def histogram():
    img = cv2.imread('tree.jpg')
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()
    cv2.imwrite('histogram.jpg',img)

    cv2.imshow('Histogram',img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()     

