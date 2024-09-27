import pyautogui
import cv2
import win32gui
import win32con


def find_window(title: str) -> int:
    """
    获取窗口句柄
    :param title:
    :return:
    """
    hwnd = win32gui.FindWindow(None, title)
    if not win32gui.IsWindow(hwnd):
        raise Exception('句柄无效')
    return hwnd


def set_window_size(hwnd: int, x: int, y: int):
    """
    设置窗口大小
    :param hwnd:
    :param x:
    :param y:
    :return:
    """
    win32gui.SetWindowPos(hwnd, None, 0, 0, x, y, 0)


def get_window_child(hwnd: int):
    if not hwnd:
        raise Exception('传入句柄不存在')
    hwnd_child_list = []
    win32gui.EnumChildWindows(hwnd, lambda item, param: param.append(item), hwnd_child_list)
    return hwnd_child_list


def click_by_img(img: str):
    btn_img = cv2.imread(img)
    pyautogui.locateOnScreen(btn_img, confidence=0.9)
