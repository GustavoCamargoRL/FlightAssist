from __future__ import print_function
import cv2 as cv
import numpy as np
import math
#from tkinter import *
import menu_method
from test import objectives




srcMap = cv.imread("map.png")
srcPlane = cv.imread("airplane3.png")

airports_name = ["LaGuardia Airport","Teterboro Airport","JFK Airport","Republic Airport","MacArthur Airport",
"Westchester Country Airport","Hill Top Airport","Lincoln Park Airport","Essex Country Airport","Morristown Airport",
"Linden Airoprt","Newark Airport","Central Jersey Airport"]

# index(Distancia,Comprimento de pista,Altitude, Direção do vento, Nível de construções ao redor)
airport_matrix = [
    [12.41, 2134, 20, 1,0],
    [15.42,1833,8.4,0,2],
    [31.27,3048,17.4,0,1],
    [40.22,2083,82,1,2],
    [65.72,2135,99,1,2],
    [29.44,1996,439,0,1],
    [48.17,655,921,0,0],
    [38.55,3932,1219,0,1],
    [33.89,1387,172,1,1],
    [45.58,1828,187,0,1],
    [39.10,1260,23,0,2],
    [28.71,3048,17.4,0,1],
    [69.27,1070,86,0,1]
]
#coordenadas de imagem do aeroporto
airport_coord = [
    [638,392],
    [472,296],
    [710,539],
    [1031,447],
    [1304,364],
    [779,54],
    [234,39],
    [253,189],
    [292,277],
    [166,364],
    [318,573],
    [370,490],
    [15,674]
]
#Constante de aproximacao pixels - KM
c_aprox = 10.26 # valor obtido pela média das taxas de distancia pixel/km das 3 coordenadas abaixo
#(779-15)²+(674-54)²=(D)² = 983 -> taxa de 10,25 pixels/km
#(1304-15)²+(674-364)²=(D2)²= 1.325,75 -> taxa de 10,24 pixels/km
#(1304-779)²+(364-54)²=(D3)² = 609,69 -> taxa de 10,28 pixels/km
# Central jersey(15,674) - westchester(779,54) = 95.88
# Central jersey - macarthur = 129.45
# westchester - macarthur(1304,364) = 59.30
glide_ratio = 17


#INICIALIZAÇÃO COORDENADAS MAPA

# INICIALIZAÇÃO VARIAVEIS MENU
max_value_A = 12000 # M
max_value_H = 360//2
max_value_R = 360
max_value_X = srcMap.shape[1]
max_value_Y = srcMap.shape[0]
low_H = 0
low_A = 0
low_X = 0
low_Y = 0
low_R = 0
high_A = max_value_A
high_X = max_value_X
high_Y = max_value_Y
high_H = max_value_H
high_R = max_value_R
window_capture_name = 'Map'
window_detection_name = 'Flight Status'
low_H_name = 'Low H'
high_H_name = 'High H'
altitude_name = "altitude"
xpos_name = "x coord"
ypos_name = "y coord"
rotation_name = "rotation"

select = objectives()
print(select)


def on_low_H_thresh_trackbar(val):
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H-1, low_H)
    cv.setTrackbarPos(low_H_name, window_detection_name, low_H)
def on_high_H_thresh_trackbar(val):
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H+1)
    cv.setTrackbarPos(high_H_name, window_detection_name, high_H)
def on_altitude_trackbar(val):
    global low_A
    global high_A 
    high_A = val
    high_A = max(high_A, low_A+1)
    cv.setTrackbarPos(altitude_name, window_detection_name, high_A)
def on_Xpos_trackbar(val):
    global low_X
    global high_X 
    high_X = val
    high_X = max(high_X, low_X+1)
    cv.setTrackbarPos(xpos_name, window_detection_name, high_X)
def on_Ypos_trackbar(val):
    global low_Y
    global high_Y 
    high_Y = val
    high_Y = max(high_Y, low_Y+1)
    cv.setTrackbarPos(ypos_name, window_detection_name, high_Y)
def on_rotation_trackbar(val):
    global low_R
    global high_R
    high_R = val
    high_R = max(high_R, low_R+1)
    cv.setTrackbarPos(rotation_name, window_detection_name, high_R)


cv.namedWindow(window_capture_name)
cv.namedWindow(window_detection_name)
cv.createTrackbar(altitude_name, window_detection_name , high_A, max_value_A, on_altitude_trackbar)
cv.createTrackbar(xpos_name, window_detection_name , high_X, max_value_X, on_Xpos_trackbar)
cv.createTrackbar(ypos_name, window_detection_name , high_Y, max_value_Y, on_Ypos_trackbar)
cv.createTrackbar(rotation_name, window_detection_name , high_R, max_value_R, on_rotation_trackbar)
cv.resizeWindow(window_detection_name,width=400,height=2)
srcPlane = cv.resize(srcPlane,(int(srcPlane.shape[1]), int(srcPlane.shape[1])), interpolation=cv.INTER_AREA)


def combine_img(image1, image2, anchor_y, anchor_x):
    foreground, background = image1.copy(), image2.copy()
    able = True
    # Check if the foreground is inbound with the new coordinates and raise an error if out of bounds
    background_height = background.shape[0]
    background_width = background.shape[1]
    foreground_height = foreground.shape[0]
    foreground_width = foreground.shape[1]
    if foreground_height+anchor_y > background_height or foreground_width+anchor_x > background_width:
        able = False
    
    alpha =0.8

    # do composite at specified location
    start_y = anchor_y
    start_x = anchor_x
    end_y = anchor_y+foreground_height
    end_x = anchor_x+foreground_width
    if(able):
        blended_portion = cv.addWeighted(foreground, alpha, background[start_y:end_y, start_x:end_x,:], 1 - alpha,0)
        background[start_y:end_y, start_x:end_x,:] = blended_portion
    return background
def rotate_image(mat, angle):
    """
    Rotates an image (angle in degrees) and expands image to avoid cropping
    """

    height, width = mat.shape[:2] # image shape has 3 dimensions
    image_center = (width/2, height/2) # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape

    rotation_mat = cv.getRotationMatrix2D(image_center, angle, 1.)

    # rotation calculates the cos and sin, taking absolutes of those.
    abs_cos = abs(rotation_mat[0,0]) 
    abs_sin = abs(rotation_mat[0,1])

    # find the new width and height bounds
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    # subtract old image center (bringing image back to origo) and adding the new image center coordinates
    rotation_mat[0, 2] += bound_w/2 - image_center[0]
    rotation_mat[1, 2] += bound_h/2 - image_center[1]

    # rotate image with the new bounds and translated rotation matrix
    rotated_mat = cv.warpAffine(mat, rotation_mat, (bound_w, bound_h))
    return rotated_mat

def get_glide_radius(z_coord):
    radius = int((z_coord/1000)*glide_ratio*c_aprox)
    return radius

#update distance from airplane to airport in the airport matrix
def update_pos(x_coord,y_coord):
    iterator = 0
    for a in airport_coord:
        pixel_dist = pow(a[0]-x_coord,2)+pow(a[1]-y_coord,2)
        pixel_dist = math.sqrt(pixel_dist)
        airport_matrix[iterator][0] = pixel_dist/10.25
        iterator = iterator+1

def normalize_matrix():
    max_a = max(airport_matrix[0])
    max_b = min(airport_matrix[0])

planesize = np.float32([[0,0],[srcPlane.shape[0],0],[0,srcPlane.shape[1]],[srcPlane.shape[0],srcPlane.shape[1]]])
#srcPlane[np.where((srcPlane == [0,0,0]).all(axis=2))] = [1,1,1]


while True:
    
    map = srcMap.copy()
    srcPlane_R = rotate_image(srcPlane,high_R)
    cv.circle(map, (high_X,high_Y), get_glide_radius(high_A), (0,0,255), thickness=5)
    for a in airport_coord:
        if(pow(high_X-a[0],2)+pow(high_Y-a[1],2) <= pow(get_glide_radius(high_A),2)):
            map = cv.circle(map, (a[0],a[1]), radius=1, color=(0, 255, 0), thickness=10)
        else:        
            map = cv.circle(map, (a[0],a[1]), radius=1, color=(0, 255, 255), thickness=10)
   
    planecoord = np.float32([[high_X-20,high_Y-20],[high_X+20,high_Y-20],[high_X-20,high_Y+20],[high_X+20,high_Y+20]])
    update_pos(high_X,high_Y)
    homography1, status1 = cv.findHomography(planesize,planecoord)
    warpBoard1 = cv.warpPerspective(srcPlane_R, homography1, (srcMap.shape[1], srcMap.shape[0]), borderMode=cv.BORDER_CONSTANT, borderValue=(0,0,0))
    merged_image = np.where(warpBoard1==0, map, warpBoard1)
    #cv.imshow(window_capture_name, combine_img(srcPlane_R,map,high_Y,high_X))
    cv.imshow(window_capture_name, merged_image)
    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break