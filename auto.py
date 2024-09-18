import pyautogui
import cv2
import time

time.sleep(5)
btn_img = cv2.imread("C:/Users/yingjian.lu/Desktop/search.png")
btn_location = pyautogui.locateOnScreen(btn_img, confidence=0.8)
if btn_location is not None:
    btn_x, btn_y = pyautogui.center(btn_location)
    pyautogui.click(btn_x, btn_y)
else:
    print("未找到")
# try:
#     while True:
#         os.system('cls')
#         a = '%4d,%4d' % pyautogui.position()
#         print(a)
# except Exception as e:
#     print(e)
