import cv2
import pyautogui
import os
import time
import subprocess
import win32com.client
import numpy as np
from PIL import ImageGrab

i = 1

while True:
    # 检查原神是否已经启动
    if os.system('tasklist /FI "IMAGENAME eq YuanShen.exe" 2>NUL | find /I /N "YuanShen.exe">NUL') == 0:
        print("已在运行!")

    screen_width, screen_height = pyautogui.size()

    print("检测屏幕...")
    screenshot = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))), cv2.COLOR_BGR2RGB)

    white_pixels = np.count_nonzero(screenshot == [255, 255, 255])
    black_pixels = np.count_nonzero(screenshot == [0, 0, 0])
    total_pixels = screenshot.shape[0] * screenshot.shape[1]
    white_percentage = white_pixels / total_pixels * 100
    black_percentage = black_pixels / total_pixels * 100

    # 判断是否满足启动条件
    if white_percentage >= 80 and i == 1:
        try:
            # 获取快捷方式路径
            shortcut = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\原神\原神.lnk'

            # 解析快捷方式获取安装路径
            shell = win32com.client.Dispatch("WScript.Shell")
            install_dir = shell.CreateShortCut(shortcut)
            install_dir = install_dir.TargetPath.replace('launcher.exe', '')

            # 拼接游戏exe路径
            game_exe = os.path.join(install_dir, 'Genshin Impact Game', 'YuanShen.exe')
            subprocess.Popen(game_exe)

            # 获取屏幕尺寸
            screenWidth, screenHeight = pyautogui.size()

            # 获取最小化程序的窗口坐标
            window = pyautogui.getWindowsWithTitle("原神")[0]
            x, y = window.left, window.top

            # 将窗口最大化
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(x + screenWidth // 2, y + screenHeight // 2, duration=0.5)
            pyautogui.click()

            i += 1
        except:
            pass

    if black_percentage >= 80:
        try:
            # 获取快捷方式路径
            shortcut = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\崩坏：星穹铁道\崩坏：星穹铁道.lnk'

            # 解析快捷方式获取安装路径
            shell = win32com.client.Dispatch("WScript.Shell")
            install_dir = shell.CreateShortCut(shortcut)
            install_dir = install_dir.TargetPath.replace('launcher.exe', '')

            # 拼接游戏exe路径
            game_exe = os.path.join(install_dir, 'Game', 'StarRail.exe')

            # 将游戏置顶启动
            subprocess.Popen(game_exe)
                     # 获取最小化程序的窗口坐标
            window = pyautogui.getWindowsWithTitle("崩坏：星穹铁道")[0]
            x, y = window.left, window.top

            # 将窗口最大化
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(x + screenWidth // 2, y + screenHeight // 2, duration=0.5)
            pyautogui.click()


            break

        except:
            pass
