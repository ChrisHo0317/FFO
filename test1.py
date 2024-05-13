import subprocess
import multiprocessing

def sandbox_process(script_path):
    # 這是你的 Python 腳本的執行命令，請替換成實際的腳本路徑
    python_command = ["python", script_path]
    
    # 启动 Python 腳本
    subprocess.Popen(python_command)

if __name__ == "__main__":
    # 這是你的 Python 腳本的路徑，請替換成實際的腳本路徑
    script_path = "path/to/your/script.py"
    
    # 创建两个独立的进程
    process1 = multiprocessing.Process(target=sandbox_process, args=(script_path,))
    process2 = multiprocessing.Process(target=sandbox_process, args=(script_path,))

    # 启动进程
    process1.start()
    process2.start()

    # 等待两个进程结束
    process1.join()
    process2.join()
