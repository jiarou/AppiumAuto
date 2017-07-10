import os

Brew_v = str(os.system("brew -v"))
if Brew_v == "0":
    print("already install")
else:
    print("start to install brew")
    os.system("ruby -e $(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)")

if Brew_v == "0":
    Node_v = str(os.system("node -v"))
    if Node_v == "0":
        print("already install")
    else:
        print("start to install brew")
        os.system("brew install node")
    if Node_v == "0":
        Appium_v = str(os.system("appium -v"))
        if Appium_v == "0":
            print("already install")
            Appium_doctor = str(os.system("appium-doctor"))
            if Appium_doctor == "0":
              print("already install")
            else:
              print("start to install brew")
              os.system("npm install appium-doctor -g")
        else:
            print("start to install brew")
            os.system("npm install -g appium")
            Appium_doctor = str(os.system("appium-doctor"))
            if Appium_doctor == "0":
              print("already install")
            else:
              print("start to install brew")
              os.system("npm install appium-doctor -g")
else:
    print("you don`t install brew , please check")
    str(os.system("brew -v"))



