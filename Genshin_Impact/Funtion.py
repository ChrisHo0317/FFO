import win32gui
import win32api
import win32con
import win32ui
import numpy as np
import cv2
import pyautogui
import os 
import logging
import time
import keyboard
from PIL import Image
from PIL import ImageGrab
from Format_Tool import defult



class Funtion():
    
        # cls.hwnd = [win32gui.FindWindow(None, window_titles) for window_titles in cls.open_window_titles]
        

    @classmethod
    def mouse_move_To(cls,x, y):
        ''' 
        移動滑鼠到相對對應座標
        '''
        # hwnd = win32gui.GetForegroundWindow()
        # point = win32gui.ScreenToClient(hwnd, (x, y))
        # x, y = point[0], point[1]
        # 移动鼠标到指定位置
        try:
            win32api.SetCursorPos((x, y))
            time.sleep(0.5)
        except:pass

    @classmethod
    def mouse_action(cls,how ='left',Mode='tick'):# 执行左键单击
        '''
        defult 左鍵單擊
        1.how = 左鍵(left)or 右鍵(right) 
        2.Mode = 單擊(tick) or 按下(down) or 彈起(up)
        '''
        x, y = win32api.GetCursorPos()
        if Mode=='tick'or Mode=='down':
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN if how =='left' else win32con.MOUSEEVENTF_RIGHTDOWN if how =='right' else 'NA', x, y, 0, 0)
            time.sleep(0.1)
        if Mode=='tick'or Mode=='up':
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP if how =='left' else win32con.MOUSEEVENTF_RIGHTUP if how =='right' else 'NA' , x, y, 0, 0)
        time.sleep(0.1)


    @classmethod
    def keyboardinput(cls,key):
        '''
            輸入鍵盤英文鍵
        '''
        keyboard.press(key)
        time.sleep(0.1)
        keyboard.release(key)
        time.sleep(0.01)

    @classmethod
    def find_image(cls,image_path,custom_bbox,Similarity=0.8):
        '''
            image_path :比對圖片檔案位置
            custom_bbox:比對範圍 (x1,y1,x2,y2)
            Similarity:相似度0~1
        '''
        # cls.mouse_move_To(0,0)
        msg = image_path.split('\\')[-1]
        output_path = cls.capture_screen(custom_bbox)
        cls.check_f12()
        #比對圖像
        template = cv2.imread(os.path.join(os.getcwd(),image_path), cv2.IMREAD_GRAYSCALE)
        screenshot = cv2.imread(output_path, cv2.IMREAD_GRAYSCALE)
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # 获取匹配位置
        top_left = max_loc
        confidence = max_val
        os.remove(output_path)
        if confidence > Similarity:  # 调整相似性的阈值
            # print(f"找到图像 {msg} 在屏幕中的位置：{top_left}，相似性：{confidence}")
            return top_left[0],top_left[1]
        else:
            # print(f"未找到图像 {msg} 在屏幕中的位置 相似性：{confidence}" )
            return -1,-1

    @classmethod
    def find_image_new(cls,template_path, screen_region, Similarity=0.8):
        template = cv2. imread(template_path, cv2.IMREAD_GRAYSCALE)
        left, top, right, bottom = screen_region
        screenshot_pil = ImageGrab.grab(bbox=(left, top, right, bottom))
        screenshot = np.array (screenshot_pil)
        screenshot_gray = cv2.cvtColor (screenshot, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(screenshot_gray,template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2. minMaxLoc (res)
        match_value = 0.5+max_val/2
        name = template_path.split('\\')[-1]
        if match_value >= Similarity:
            match_location = (max_loc[0] + left, max_loc[1] + top)
            # print(f"匹配位置为：{name}  {match_location}，相似度分数为:{match_value:.2f}")
            time.sleep(0.2)
            return match_location[0],match_location[1]
        else:
            # print(f"{name}，相似度分数为:{match_value:.2f}")
            return -1, -1

    @classmethod
    def Trigger_window(cls,window_name):
        hwnd = win32gui.FindWindow(None, window_name)
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(1)

    @classmethod
    def transparent(cls,fig_list):
        name_list =list()
        if not os.path.exists('UsePNG'):os.makedirs('UsePNG')
        for fig_path in fig_list:
            save_img = os.path.join('UsePNG',fig_path.split('\\')[-1].replace('bmp','png'))
            name_list.append(fig_path.split('\\')[-1].replace('bmp','png'))
            RGB,Status = cls.read_image_corners(fig_path)
            if Status:
                cls.make_color_transparent(fig_path,RGB,save_img)
        return name_list
                
    @classmethod
    def pathjoin(cls,name):
        return os.path.join('UsePNG',name)

    @classmethod
    def change_windows_title(cls,name_list):
        if len(name_list)>1:
            name_list_new=list()
            for num,name in enumerate(name_list):
                new_title = name+str(num)

                hwnd = win32gui.FindWindow(None, name)
                name_list_new.append(new_title)
                if hwnd:
                    win32gui.SetWindowText(hwnd, new_title)
                    # print(f"Window title changed to '{new_title}'.")
                else:
                    # print(f"Window '{name}' not found.")
                    pass
            return name_list_new
        else:return name_list

    #============================================================= 模組 =====================================
    @classmethod
    def read_image_corners(cls,image_path):
            '''
                檢查四個角是否相同顏色 
                True 該顏色為透明 
                False 白色為透明
            '''
            # 读取图像
            img = Image.open(image_path)
            # 获取图像大小
            width, height = img.size
            # 读取四个角落的RGB值
            top_left_color = img.getpixel((0, 0))
            top_right_color = img.getpixel((width - 1, 0))
            bottom_left_color = img.getpixel((0, height - 1))
            bottom_right_color = img.getpixel((width - 1, height - 1))
            if top_left_color==top_right_color==bottom_left_color==bottom_right_color:return top_left_color,True
            else:(255, 255, 255),False

    @classmethod
    def make_color_transparent(cls,image_path, target_color,output_path):
        '''
            將輸入顏色轉換為透明色
        '''
        img = Image.open(image_path).convert("RGBA")
        img_array = np.array(img)
        r, g, b, a = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2], img_array[:, :, 3]
        mask = (r == target_color[0]) & (g == target_color[1]) & (b == target_color[2])
        a[mask] = 0
        new_img = Image.fromarray(img_array, "RGBA")
        new_img.save(output_path)

    @classmethod
    def capture_screen(cls,custom_bbox,output_path=r'UsePNG\screenshot.png'):
        '''
            將畫面截圖
        '''
        screenshot = ImageGrab.grab(bbox=custom_bbox)
        #保存圖像
        screenshot.save(output_path)
        return output_path
    
    @classmethod
    def get_open_window_titles(cls,find_title = "Fantasy Frontier Online"):
        window_titles = []

        def enum_windows_callback(hwnd, lParam):
            title = win32gui.GetWindowText(hwnd)
            if title:
                window_titles.append(title)
            return True
        title_list = list()
        win32gui.EnumWindows(enum_windows_callback, 0)
        for title in window_titles:
            if find_title in title:
                title_list.append(title)
        return title_list
    
    @classmethod
    def check_f12(cls):
        if keyboard.is_pressed('F12'):
            logging.info("按下了 F12 键，停止脚本运行。")
            cls.windows_Status = False
            cls.main_status = False
    
    def get_mouse_position():
        # 获取当前鼠标的坐标
        x, y = pyautogui.position()
        return x,y


















