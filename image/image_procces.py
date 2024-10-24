import cv2 as cv
import numpy as np
import os

def to_silhouette(image):
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY) # Convert to gray scale
    # binary = cv.adaptiveThreshold(gray_image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 2)
    _, binary = cv.threshold(gray_image, 128, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU) # Convert to binary black and white based on threshhold
    contours, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) # Identifiy the silhouette
    blank = np.ones_like(gray_image) * 255 # Create blank image
    drawn = cv.drawContours(blank, contours, -1, (0, 0), thickness=cv.FILLED) # Draw silhouette on to the blank image
    return drawn

def resize_with_padding(image, target_height, target_width):
    original_height, original_width = image.shape[:2]
    scale_ratio = target_height / original_height
    new_height = target_height
    new_width = int(original_width * scale_ratio)

    resized_image = cv.resize(image, (new_width, new_height), interpolation=cv.INTER_AREA)

    # If the new width is less than the target width, add black padding
    if new_width < target_width:
        padding_left = (target_width - new_width) // 2
        padding_right = target_width - new_width - padding_left
        
        padded_image = cv.copyMakeBorder(
            resized_image, 0, 0, padding_left, padding_right, 
            cv.BORDER_CONSTANT, value=[0, 0, 0])
        return padded_image
    else:
        return resized_image

def image_to_ascii(image):
    rows, cols = image.shape

    txt_rows = []
    txt_rows.append(' ' + os.linesep)
    for i in range(rows):
        row_txt = ''
        for j in range(cols):
            k = image[i, j]
            if k <= 0:
                row_txt += '  '
            else:
                row_txt += '██'
        row_txt += os.linesep
        txt_rows.append(row_txt)
        
    return txt_rows