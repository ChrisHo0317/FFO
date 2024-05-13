import tkinter as tk
from PIL import Image, ImageTk

def set_background(window, image_path):
    # 使用 Pillow 打开图像
    img = Image.open(image_path)

    # 使用 ImageTk 将图像转换为 PhotoImage 对象
    img = ImageTk.PhotoImage(img)

    # 创建画布
    canvas = tk.Canvas(window, width=img.width(), height=img.height())
    canvas.pack()

    # 将图像设置为画布的背景
    canvas.create_image(0, 0, anchor=tk.NW, image=img)

    # 设置窗口大小为图像大小
    window.geometry(f"{img.width()}x{img.height()}")

# 创建主窗口
root = tk.Tk()
root.title("Tkinter Background Image")
# 背景图像的路径，請替換成實際的圖片路徑
image_path = r'G:\我的雲端硬碟\BLACKPINK\Jennie\wp6360795-blackpink-jennie-solo-wallpapers.png'

# 设置背景
set_background(root, image_path)

# 运行主循环
root.mainloop()