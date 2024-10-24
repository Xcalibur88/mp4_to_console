import pytest
import cv2 as cv
import numpy as np
from image import image_procces

@pytest.fixture
def original_image():
    return cv.imread('tests/oframe.png', cv.IMREAD_UNCHANGED)

@pytest.fixture
def downscaled_image():
    return cv.imread('tests/dframe.png', cv.IMREAD_UNCHANGED)

@pytest.fixture
def binary_image():
    return cv.imread('tests/bframe.png', cv.IMREAD_UNCHANGED)

@pytest.fixture
def ascii_frame():
    with open('tests/ascii_frame.txt', 'r') as f:
        return f.readlines()


def test_to_silhouette(downscaled_image, binary_image):
    image = image_procces.to_silhouette(downscaled_image)

    rows, cols = image.shape
    for i in range(rows):
        for j in range(cols):
            k = image[i, j]
            assert k == 0 or k == 255 # Assert it is a black or white pixel
    assert np.all(cv.absdiff(image, binary_image) == 0)

def test_resize_with_padding(original_image, downscaled_image):
    image = image_procces.resize_with_padding(original_image, 38, 80)
    height, width, channels = image.shape

    assert height == 38
    assert width == 80
    assert np.all(cv.absdiff(image, downscaled_image) == 0)

def test_image_to_ascii(binary_image, ascii_frame):
    ascii = image_procces.image_to_ascii(binary_image)
    height, width = binary_image.shape

    assert len(ascii) == height + 1
    assert (len(ascii[1]) - 1) / 2 == width
    assert ascii == ascii_frame