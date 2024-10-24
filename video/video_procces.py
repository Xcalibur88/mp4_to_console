import cv2 as cv
import time
from image import image_procces
from main import SAVE_DIRECTORY


def video_to_ascii(video_file, save_file, fps_out=5, max_frames=100000):
    vidcap = cv.VideoCapture(video_file)
    assert vidcap.isOpened()
    
    fps_in = vidcap.get(cv.CAP_PROP_FPS)
    index_in = -1
    index_out = -1
    while True:
        if index_out >= max_frames: break

        success = vidcap.grab()
        if not success: break
        index_in += 1

        out_due = int(index_in / fps_in * fps_out)
        if out_due > index_out:
            success, frame = vidcap.retrieve()
            if not success: break

            downscaled_frame = image_procces.resize_with_padding(frame, 39, 95) # Downscale to fit console
            binary_frame = image_procces.to_silhouette(downscaled_frame) # Convert to black and white silhouette
            ascii = image_procces.image_to_ascii(binary_frame) # Convert frame to ascii
            write_to_file(ascii, save_file) # Write ascii to save file
            
            cv.imwrite(str(SAVE_DIRECTORY + "/bframe%d.jpg") % (index_out + 1), binary_frame) # save frame as JPEG file for review

            index_out += 1
    vidcap.release()

def write_to_file(lines, save_file):
    with open(save_file, 'a') as afile:
        afile.writelines(lines)

def play_ascii(ascii_video_file):
    with open(ascii_video_file, 'r') as file:
        fps = int(file.readline().split('.')[1])
        for line in file:
            if line == ' \n':
                time.sleep((1 / fps))
            else:
                print(line, end='')
