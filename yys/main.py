import win32gui
import win32con
import win32process
import utils

if __name__ == '__main__':
    hwnd = utils.find_window('aaa.txt - 记事本')
    utils.set_window_size(hwnd, 800, 600)

    win32gui.SetForegroundWindow(hwnd)
    arr = utils.get_window_child(hwnd)
    for item in arr:
        print(str(item) + ':', end=None)
        left, top, right, bottom = win32gui.GetWindowRect(item)
        print(left, top, right, bottom)
    print(hwnd)
    print(arr)
