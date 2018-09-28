from tkinter import *
from tkinter import messagebox
# from PIL import Image

#创建窗口
window = Tk()
#窗口标题
window.title("你喜欢我吗")
#窗口大小 宽x长+x+y
window.geometry("435x543+380+80")


#点击关闭触发方法
def closewindows():
    messagebox.showinfo("提示","好好回答")
#点击喜欢触发的方法
def love():
    love = Toplevel(window)
    love.title("好巧")
    love.geometry("280x100+460+300")
    label=Label(love,text="终于等到你",font=('宋体',25))
    label.pack()
    btn= Button(love,text="确定",width=15,height=1,command=clicklove)
    btn.pack()
    love.protocol("WM_DELETE_WINDOW",closelove)

def closelove():
    # messagebox.showinfo()
    return


#点击关闭喜欢窗口
def clicklove():
    #销毁
    window.destroy()


def nolove():
    no_love = Toplevel(window)
    no_love.title("再考虑考虑呗")
    no_love.geometry("280x100+460+300")
    label =Label(no_love,text="在考虑考虑呗",font=("微软雅黑",20))
    label.pack()
    btn = Button(no_love, text="好的", width=15, height=1,command=no_love.destroy)
    btn.pack()
    no_love.protocol("WM_DELETE_WINDOW",close_nolove)



def close_nolove():
    nolove()

#监控关闭
window.protocol("WM_DELETE_WINDOW",closewindows)


#设置文字
label = Label(window,text='hi,小姐姐:',font=("微软雅黑",15))
#定位
label.grid(row=0,column=0,sticky=W)

label1 = Label(window,text = '喜欢我吗?',font=("微软雅黑",30))
#sticky 对齐方式 N,S,W,E
label1.grid(row = 1,column = 1,sticky= E)
#设置图片
photo =PhotoImage(file="./bb.gif")
# photo = Image.open("./aa.gif")
# print(photo)
imageLabel = Label(window,image=photo)
imageLabel.grid(row=2,columnspan=2,sticky=N)

#设置按钮
btn = Button(window,text="喜欢",width=20,height=2,command=love)
btn.grid(row=3,column=0,sticky=W)


btn1 = Button(window,text="不喜欢",width=5,command=nolove)
btn1.grid(row=3,column=1,sticky=E)

label2=Label(window,text="--by_cx",font=("黑体",8))
label2.grid(row=3,column=2,sticky=E)

#显示窗口
window.mainloop()