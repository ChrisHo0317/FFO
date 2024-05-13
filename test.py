import pythoncom
import pyWinhook as pyHook
import threading
import time
import ctypes
import inspect


class stop_thread:
    '''
        刻意產生錯誤終止程序
    '''
    def __init__(self,thread):
        self._async_raise(thread.ident,SystemExit)

    def _async_raise(self,tid,exctype):
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,ctypes.py_object(exctype))
        if res ==0:
            raise ValueError('invalid thread id')
        elif res != 1 :
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,None)
            raise SystemError('PyThreadState_SetAsyncExc failed')
# 监听到鼠标事件调用
def onMouseEvent(event):
    if(event.MessageName!="mouse move"):
        print(event.MessageName)
    return True

# 监听到键盘事件调用
def onKeyboardEvent(event):
    print(event.Key)# 返回按下的键
    return True

def main():
	# 创建管理器
    hm = pyHook.HookManager()
    # 监听键盘
    hm.KeyDown = onKeyboardEvent   
    hm.HookKeyboard()  
    # 监听鼠标 
    hm.MouseAll = onMouseEvent   
    hm.HookMouse()
    # 循环监听
    parser_thread = threading.Thread(target=pythoncom.PumpMessages)
    parser_thread.start()
    time.sleep(10)
    stop_thread(parser_thread)

 
if __name__ == "__main__":
    main()