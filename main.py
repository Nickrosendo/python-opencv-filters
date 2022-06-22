import cv2
import sys
import os

filter_type = sys.argv[1]

file_path = sys.argv[2]

file_metadata = os.path.splitext(file_path)
filename = file_metadata[0]
file_extension = file_metadata[1]

try:
    file_output_path = sys.argv[3]
except:
    file_output_path = f'{filename}_{filter_type}{file_extension}'

print(f'filename: {filename}')
print(f'file_extension: {file_extension}')
print(f'file_path: {file_path}')
print(f'file_output_path: {file_output_path}')

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

def applyFilter(file_path, filter_type='gray'):
    
    img = cv2.imread(file_path)
    
    new_img = eval(f'{filter_type}Filter(img)')
            
    cv2.imwrite(file_output_path, new_img)

applyFilter(file_path, filter_type)
