import cv2

filename = 'shiba_real'
image_type = 'jpg'

def grayFilter(img):
    
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
def blurFilter(img):
    
    return cv2.blur(img, (10, 10)) 
    
def sobelFilter(img):
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
    
def pencilFilter(img, scale_type='color'):
    
    _gray, _color = cv2.pencilSketch(img, sigma_s=2, sigma_r=0.5, shade_factor=0.1)
    
    if scale_type == 'color':
        return _color
    else:
        return _gray

def applyFilter(filename, image_type, filter_name='gray'):
    
    img = cv2.imread(f'{filename}.{image_type}')
    
    new_img = eval(f'{filter_name}Filter(img)')
        
    cv2.imwrite(f'{filename}_{filter_name}.{image_type}', new_img)

applyFilter(filename, image_type, filter_name='pencil')
