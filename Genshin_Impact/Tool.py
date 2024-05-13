from Genshin_Impact.Funtion import Funtion
import time
import logging

class Tool(Funtion):
    finglist = [r'PNG\1440p\Genshin_Impact\Gift.bmp',r'PNG\1440p\Genshin_Impact\big_frame.bmp',r'PNG\1440p\Genshin_Impact\receive.bmp',r'PNG\1440p\Genshin_Impact\frame.bmp',r'PNG\1440p\Genshin_Impact\link.bmp',r'PNG\1440p\Genshin_Impact\big_msg.bmp',r'PNG\1440p\Genshin_Impact\msg.bmp',r'PNG\1440p\Genshin_Impact\link_black.bmp',r'PNG\1440p\confirm.bmp']
    fig_list = Funtion.transparent(finglist)

    @classmethod
    def msg1(cls,Genshin_Impact_format_box,Genshin_Impact_format):
        # x,y = cls.find_image([cls.pathjoin(fig) for fig in cls.fig_list if fig=='msg.png'][0],Genshin_Impact_format_box,Similarity=0.6)
        x,y = cls.find_image_new([cls.pathjoin(fig) for fig in cls.fig_list if fig=='msg.png'][0],Genshin_Impact_format_box,Similarity=0.8)
        if (x>0) or (y>0):
            cls.mouse_move_To(x+25,y+25)
            cls.mouse_action(how='left',Mode='tick')
            time.sleep(0.3)
            # x,y = cls.find_image([cls.pathjoin(fig) for fig in cls.fig_list if fig=='dialogue.png'][0],Genshin_Impact_format,Similarity=0.8)
            x,y = cls.find_image_new([cls.pathjoin(fig) for fig in cls.fig_list if fig=='big_msg.png'][0],Genshin_Impact_format,Similarity=0.8)
            if (x>0) or (y>0):
                for i in range(3):
                    cls.mouse_move_To(x+25,y+15)
                    cls.mouse_action(how='left',Mode='tick')
                    cls.mouse_move_To(x+200,y+15)
                    cls.mouse_action(how='left',Mode='tick')
                    time.sleep(0.3)

    @classmethod
    def final(cls,Genshin_Impact_format,check_format):
        # x,y = cls.find_image([cls.pathjoin(fig) for fig in cls.fig_list if fig=='link.png'][0],Genshin_Impact_format,Similarity=0.5)
        x,y = cls.find_image_new([cls.pathjoin(fig) for fig in cls.fig_list if fig=='link.png'][0],Genshin_Impact_format,Similarity=0.7)
        if (x>0) or (y>0):
            cls.mouse_move_To(x+25,y+25)
            cls.mouse_action(how='left',Mode='tick')
            time.sleep(0.3)
            # x,y = cls.find_image([cls.pathjoin(fig) for fig in cls.fig_list if fig=='confirm.png'][0],check_format,Similarity=0.6)
            x,y = cls.find_image_new([cls.pathjoin(fig) for fig in cls.fig_list if fig=='confirm.png'][0],check_format,Similarity=0.8)
            if (x>0) or (y>0):
                cls.mouse_move_To(x+25,y+15)
                cls.mouse_action(how='left',Mode='tick')
                time.sleep(0.3)
        else:
            # x,y = cls.find_image([cls.pathjoin(fig) for fig in cls.fig_list if fig=='link_black.png'][0],Genshin_Impact_format,Similarity=0.9)
            x,y = cls.find_image_new([cls.pathjoin(fig) for fig in cls.fig_list if fig=='link_black.png'][0],Genshin_Impact_format,Similarity=0.75)
            if (x>0) or (y>0):
                cls.keyboardinput('h')
                time.sleep(0.3)
                cls.keyboardinput('h')