# DemoOS.py
from os.path import *

#print( dir(os.path) )

print( abspath("python.exe") )
print( basename("C:\\Users\\82103\\\\python.exe") )
print( exists("C:\\Users\\82103\\\\python.exe") )
print( getsize("C:\\Users\\82103\\python.exe") )

#운영체제에 있는 명령어를 실행(cmd --> cd \, cd work2 )
from os import *

print("현재 폴더:", getcwd() )
chdir("..")
chdir("c:\\work2")
print("현재 폴더:", getcwd() )
#외부에 실행파일 수행
#system("notepad.exe")

#파일, 폴더 리스트
import glob
print( glob.glob("*.py") )
print( "=" * 20 )
for item in glob.glob("*.*"):
    print(item)
