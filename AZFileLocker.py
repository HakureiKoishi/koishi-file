#-----------------------引用-----------------------
import os
import time
import shutil
import zipfile
from os.path import join, getsize
import winreg
import pyzipper
import binascii
import sys
print("正在准备运行环境...")
try:
    import pyzipper
except:
    cmd_mkdir = r'cd C:\Windows\System32'
    cmd_new_file = 'pip install pyzipper -i https://pypi.tuna.tsinghua.edu.cn/simple'
    cmd = "{0} && {1}".format(cmd_mkdir, cmd_new_file)
    os.system(cmd)
    import pyzipper
try:
    import requests
except:
    cmd_mkdir = r'cd C:\Windows\System32'
    cmd_new_file = 'pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple'
    cmd = "{0} && {1}".format(cmd_mkdir, cmd_new_file)
    os.system(cmd)
    import requests
#-----------------------定义-----------------------
#↓解压缩↓

def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')

#-----------------------程序-----------------------

#↓声明↓
os.system("cls")
print("""① >本程序仅供研究学习使用，请务必在法律允许的范围内使用。<
>否则，由此引起的一切后果均须自行承担责任，与本软件和其作者无关<""")
print("")
print("""② >本程序遵守 Creative Commons (知识共享)发布的《署名-非商业性使用-相同方式共享 4.0 国际 (CC BY-NC-SA 4.0)》开源共享协议<
>有关该协议的详细内容, 请访问 http://p79.net/b4b5c.<""")
print("")

if os.path.exists(r'C:\ProgramData\AZFileLocker_checkversion.txt'):
    pass
    #版本文件存在
else:
    #版本文件不存在，正在创建
    file = open(r'C:\ProgramData\AZFileLocker_checkversion.txt','w')
    file.write("主功能未安装，请检查您的网络是否正常，并重启程序以重新下载~！")
    #未下载数据文件
    #版本文件已创建"
    file.close()
try:
    #下载地址
    Download_addres='https://codeload.github.com/HakureiKoishi/ALaU_Version/zip/refs/heads/main'
    #把下载地址发送给requests模块
    Download_mainpart=requests.get(Download_addres)
    #下载文件
    with open(r"C:\ProgramData\ALaU_Version-main.zip","wb") as code:
         code.write(Download_mainpart.content)
except:
    pass
unzip_file(r"C:\ProgramData\ALaU_Version-main.zip", r"C:\ProgramData")
try:
    os.remove(r'C:\ProgramData\ALaU_Version-main.zip')
except:
    pass
try:
    shutil.move(r'C:\ProgramData\ALaU_Version-main\ALaU_Version.txt',r'C:\ProgramData')
except:
    pass
if os.path.exists(r'C:\ProgramData\ALaU_Version-main'):
    shutil.rmtree(r'C:\ProgramData\ALaU_Version-main')
else:
    pass
file = open(r'C:\ProgramData\ALaU_Version.txt')
version=file.read()
file.close()
file = open(r'C:\ProgramData\AZFileLocker_checkversion.txt')
checkversion=file.read()
file.close()
if version!=checkversion:
    if os.path.exists(r'C:\Users\Public\Documents\FLU'):
        shutil.rmtree(r'C:\Users\Public\Documents\FLU')
        #"旧版数据文件已删除"
    else:
        pass
        #"找不到旧版数据文件"
    if os.path.exists(r'C:\ProgramData\ALaU-main.zip'):
        os.remove(r'C:\ProgramData\ALaU-main.zip')
        #"旧版数据压缩包已删除"
    else:
        pass
        #"找不到旧版数据压缩包"
#下载更新文件
    try:
        #下载地址
        Download_addres='https://codeload.github.com/HakureiKoishi/ALaU/zip/refs/heads/main'
        #把下载地址发送给requests模块
        Download_mainpart=requests.get(Download_addres)
        #下载文件
        with open(r"C:\ProgramData\ALaU-main.zip","wb") as code:
             code.write(Download_mainpart.content)
    except:
        pass
    unzip_file(r"C:\ProgramData\ALaU-main.zip", r"C:\ProgramData")
    if os.path.exists(r'C:\ProgramData\ALaU-main.zip'):
        os.remove(r'C:\ProgramData\ALaU-main.zip')
        #"旧版数据压缩包已删除"
    else:
        pass
        #"找不到旧版数据压缩包"
    os.rename(r"C:\ProgramData\ALaU-main",r'C:\ProgramData\FLU')
    try:
        shutil.move(r'C:\ProgramData\FLU',r'C:\Users\Public\Documents\FLU')
    except:
        pass
    if os.path.exists(r"C:\ProgramData\ALaU-main"):
        shutil.rmtree(r"C:\ProgramData\ALaU-main")
        #"旧版数据文件已删除"
    else:
        pass
    if os.path.exists(r'C:\ProgramData\FLU'):
        shutil.rmtree(r'C:\ProgramData\FLU')
        #"旧版数据文件已删除"
    else:
        pass
    checkversion=version
    file = open(r'C:\ProgramData\AZFileLocker_checkversion.txt', 'w')
    file.write(checkversion)
    file.close()
    try:
        sys.path.append(r'C:\Users\Public\Documents\FLU')
        from FLker import FileLocker
    except:
        print("主程序无法读取")
        time.sleep(2)
        quit()
elif version==checkversion:
    try:
        sys.path.append(r'C:\Users\Public\Documents\FLU')
        from FLker import FileLocker
    except:
        print("主程序无法读取")
        time.sleep(2)
        quit()
else:
    print("\r"+"错误：无法校对版本       ")
    time.sleep(5)
    quit()

second = 10
for i in range(second,0,-1):
    print("\r"+'③ >>此页还将展示'+str(second)+'秒<',end="")
    time.sleep(1)
    second -= 1
#↓版本相关↓
os.system("cls")
time.sleep(0.5)
print("------ AZFileLocker&Unlocker ------")
print("")
print(version)
print("")
print("--------- By HKRT(博丽恋) ---------")
print("")
time.sleep(0.5)
#↓主菜单↓
print("》功能菜单《")
print("")
print("1.为文件创建加密容器")
print("2.解密加密容器")
print("")
time.sleep(0.5)
MenuChoice = input("输入模式对应序号：")
if MenuChoice == "1":
    FileLocker()
else:
    print("其他功能尚未完全开发")
    time.sleep(2)
