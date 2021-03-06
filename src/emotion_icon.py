import cv2 as cv
import numpy as np

angry_man = None
ICON_SIZE = (40, 40)
WORDS_SIZE = (160, 80)

ICON_IMG_PATH = "./src/img/emotion/"
WORD_IMG_PATH = "./src/img/emotion_word/emoji_picture/emoji_picture/"
IMG_PATH = "./src/img_1/"



EMOTION_WORD = [
        "m_angry", "w_angry", "m_disgust", "w_disgust",
        "m_fear", "w_fear", "m_happy", "w_happy",
        "m_no", "w_no", "m_sad", "w_sad", "m_suprise",
        "w_suprise"]


def load_emotion_icon():

    words_dict = {}

    for icon in EMOTION_WORD:
        tmp_img = cv.imread(WORD_IMG_PATH+icon+".png", -1)
        tmp_img = cv.resize(tmp_img, WORDS_SIZE)
        tmp_img = cv.cvtColor(tmp_img, cv.COLOR_RGB2BGR)
        words_dict[icon] = tmp_img
       # print(words_dict[icon].shape)

    return words_dict


def Addemotion(coordinates, image_array, emotion_icon=None):
    print(coordinates)
    x, y, w = coordinates[:3]
    x_offset = x + w - emotion_icon.shape[1]
    y_offset = -80 + y
    y1, y2 = y_offset, y_offset + emotion_icon.shape[0]
    x1, x2 = x_offset, x_offset + emotion_icon.shape[1]

    alpha_s = emotion_icon[:, :, 2] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        image_array[y1:y2, x1:x2, c] = (alpha_s * emotion_icon[:, :, c] + 
                                        alpha_l * image_array[y1:y2, x1:x2, c])

    return image_array


def Addemotion_word(coordinates, image_array, emotion_icon=None):
    x, y, w= coordinates[:3]
    x_offset = x+w//2-100
    y_offset = -80 + y
    y1, y2 = y_offset, y_offset + emotion_icon.shape[0]
    x1, x2 = x_offset, x_offset + emotion_icon.shape[1]
    print("----- emotion_icon")
    
    #emotion_icon1 = np.array(emotion_icon,dtype = np.int)
    width = emotion_icon.shape[0]
    height = emotion_icon.shape[1]
    alpha_value = np.ones((width, height, 1))*255
    emotion_icon1 = np.c_[emotion_icon, alpha_value]
  #  print(emotion_icon1.shape)
    
    alpha_s = emotion_icon1[:, :, 3] / 255.0 #一個白一個黑
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        image_array[y1:y2, x1:x2, c] = (alpha_s * emotion_icon1[:, :, c] + 
                                       alpha_l * image_array[y1:y2, x1:x2, c])
    print(image_array)
    return image_array


def return_finish():
    return "True"