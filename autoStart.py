import os
import subprocess

# 取得當前的工作目錄
os.getcwd()
# 切換到欲使用的目錄

if os.path.exists("jiarou"):
    os.chdir("jiarou")
    subprocess.Popen('python3 start_service.py ; python3 start_tests.py', shell=True)
    # os.system("python3 start_service.py")
    # os.system("python3 start_tests.py")
else:
    os.system("git clone https://bitbucket.org/chocolabsqateam/device-farm/branch/jiarou")
    os.chdir("jiarou")
    os.system("cd jiarou")
    os.system("git checkout jiarou")
    os.system("git pull origin jiarou")
