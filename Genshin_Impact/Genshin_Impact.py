from Genshin_Impact.Tool import Tool
import time
import keyboard
import logging


class Genshin_Impact(Tool):

    Genshin_Impact_format = (1643, 864, 2277, 1106)
    Genshin_Impact_format_box = {0:(1800, 873,1890, 965),1:(1870, 873,1960, 965),2:(1940, 873,2030, 965)}
    check_format = (1136, 802,1244, 842)

    @classmethod
    def Run(cls,input_count=1):
        cls.open_window_titles = cls.get_open_window_titles()
        cls.open_window_titles = cls.change_windows_title(cls.open_window_titles)
        title_list = '\n'.join(cls.open_window_titles)
        logging.info(f"開啟的視窗: {title_list}")
        time.sleep(2)
        cls.windows_Status=True
        while cls.windows_Status:
            for window_name in cls.open_window_titles:
                cls.Trigger_window(window_name)
                cls.windows_check()
                cls.main()
        return True

    @classmethod
    def windows_check(cls,check =True):
        time.sleep(1)
        cls.keyboardinput('h')
        time.sleep(1)
        while check:
            x,y = cls.find_image_new([cls.pathjoin(fig) for fig in cls.fig_list if fig=='big_frame.png'][0],(0, 0, 2560, 1440),Similarity=0.7)
            if (x>0) or (y>0):
                cls.mouse_move_To(x+30,y+75)# 1693, 976
                cls.mouse_action(how ='left',Mode='down')
                cls.mouse_move_To(1715, 999)
                cls.mouse_action(how ='left',Mode='up')
                check = False
            else:
                cls.keyboardinput('h')
                check = True

    @classmethod
    def main(cls):
        start_time = time.time() 
        max_execution_time = 40
        elapsed_time = time.time() - start_time
        cls.main_status = elapsed_time <= max_execution_time
        while cls.main_status:
            for i in range(3):
                x,y = cls.find_image_new([cls.pathjoin(fig) for fig in cls.fig_list if fig=='Gift.png'][0],cls.Genshin_Impact_format_box[i],Similarity=0.8)#禮物
                if (x>0) or (y>0):
                    cls.mouse_move_To(x+25,+y+25)
                    cls.mouse_action(how='left',Mode='tick')
                    time.sleep(0.5)
                    x1,y1 = cls.find_image_new([cls.pathjoin(fig) for fig in cls.fig_list if fig=='receive.png'][0],cls.Genshin_Impact_format,Similarity=0.8)#領取
                    if (x1>0) or (y1>0):
                        cls.mouse_move_To(x1+25,y1+15)
                        cls.mouse_action(how='left',Mode='tick')
                        cls.msg1(cls.Genshin_Impact_format_box[i],cls.Genshin_Impact_format)
                        cls.final(cls.Genshin_Impact_format,cls.check_format)
                cls.msg1(cls.Genshin_Impact_format_box[i],cls.Genshin_Impact_format)
                x,y = cls.find_image_new([cls.pathjoin(fig) for fig in cls.fig_list if fig=='frame.png'][0],cls.Genshin_Impact_format_box[i],Similarity=0.84)#框
                if (x>0) or (y>0):
                    cls.mouse_move_To(x+25,y+25)
                    cls.mouse_action(how='left',Mode='tick')
                    cls.final(cls.Genshin_Impact_format,cls.check_format)

            cls.main_status = time.time() - start_time <=max_execution_time
            cls.check_f12()

if __name__ =='__main__':
    Genshin_Impact.Run()