import win32gui
import win32con
import win32print
import utils
import ctypes

if __name__ == '__main__':
    width, height = 800, 600
    hwnd = utils.find_window('aaa.txt - 记事本')
    win32gui.SetActiveWindow(hwnd)
    utils.set_window_size(hwnd=hwnd, width=width, height=height)

    win32gui.SetForegroundWindow(hwnd)
    arr = utils.get_window_child(hwnd)
    img = utils.get_window_image(hwnd, width, height)
    template = '../file/template.png'
    # print(utils.find_image_in_window(hwnd, template, width, height))
    utils.save_matched_image(hwnd, template, width, height)
