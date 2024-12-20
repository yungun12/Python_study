#code7-1
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from wand.image import *

#함수 선언 부분
def displayImage() :
    pass
def func_open() :
    pass
def func_save() :
    pass
def func_exit() :
    pass
def func_zoomin() :
    pass
def func_zoomout() :
    pass
def func_mirror1() :
    pass
def func_mirror2() :
    pass
def func_rotate() :
    pass
def func_bright() :
    pass
def func_dark() :
    pass
def func_clear() :
    pass
def func_unclear() :
    pass
def func_bw() :
    pass



#전역 변수 부분
window, canvas, paper = None, None, None
photo, photo2 = None, None
oriX, oriY = 0, 0

#메인 코드 부분
window = Tk()
window.geometry("250x250")
window.title("미니포토샵")

mainMenu = Menu(window)
window.config(menu=mainMenu)
photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_command(label = "파일 저장", command = func_save)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label = "이미지 처리(1)", menu = image1Menu)
image1Menu.add_command(label = "확대", command = func_zoomin)
image1Menu.add_command(label = "축소", command = func_zoomout)
image1Menu.add_separator()
image1Menu.add_command(label = "상하 반전", command = func_mirror1)
image1Menu.add_command(label = "좌우 반전", command = func_mirror2)
image1Menu.add_command(label = "회전", command = func_rotate)

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label = "이미지 처리(2)", menu = image2Menu)
image2Menu.add_command(label = "밝게", command = func_bright)
image2Menu.add_command(label = "어둡게", command = func_dark)
image2Menu.add_separator()
image2Menu.add_command(label = "선명하게", command = func_clear)
image2Menu.add_command(label = "탁하게", command = func_unclear)
image2Menu.add_separator()
image2Menu.add_command(label = "흑백이미지", command = func_bw)
window.mainloop()