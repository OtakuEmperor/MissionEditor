import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import font


helv36 = font.Font(family='Helvetica', size=36, weight=font.BOLD)
nowSelectRow = 0
nowSelectCol = 0
missionList = []

def SaveSetting():
    global mighty
    global nowSelectCol
    global nowSelectRow
    missionList[nowSelectCol][nowSelectRow].SetName(missionName.get())
    if(missionList[nowSelectCol][nowSelectRow].UIText == None):
        missionText = tk.Label(mighty,
         text = missionList[nowSelectCol][nowSelectRow].name,
         bg="white",
         width=2, height=1
         )
        missionText.grid(row =nowSelectRow,column = nowSelectCol)
        missionList[nowSelectCol][nowSelectRow].UIText = missionText
    else:
        missionList[nowSelectCol][nowSelectRow].UIText['text']=missionList[nowSelectCol][nowSelectRow].name


class SingleMission(object):
    """docstring for SingleMission"""
    UILabel = None
    UIText = None
    posRow = 0
    posCol = 0
    name = "1"
    def __init__(self, col, row):
        self.posCol = col
        self.posRow = row
        super(SingleMission, self).__init__()
    def SetName(self,nameInput ):
        self.name = nameInput
        

test = 0

# Create instance
win = tk.Tk()   

# Add a title       
win.title("任務編輯器")  
win.geometry("600x600")

tabControl = ttk.Frame(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab 
tab1.grid(column=0, row=0,sticky=tk.NW)    # Add the tab
tab2 = ttk.Frame(tabControl)            # Create a tab 
tab2.grid(column=1, row=0,sticky=tk.NE)
tabControl.pack(expand=1, fill="both")
setPanel = ttk.Frame(tabControl)
setPanel.grid(column=0,row=1,sticky=tk.SW)



def ClickLabel( col, row ):
    global nowSelectCol
    global nowSelectRow
    nowSelectCol = col
    nowSelectRow = row
    SetLabelBKHighLight(col,row)
    print(str(nowSelectCol) + " : " + str(nowSelectRow))

def ClickArrow( type ):
    if(type == "up"):
        missionList[nowSelectCol][nowSelectRow].UILabel.config(text="↑",fg="green")

def SetLabelBKHighLight ( col, row):

    for i in range(len(missionList)):
        for j in range(len(missionList[i])):
            if(i == col and j == row):
                missionList[i][j].UILabel.config(bg="red")
            else:
                missionList[i][j].UILabel.config(bg="black")
#======================
# B Panel
#======================
mighty = ttk.LabelFrame(tab1, text=' 任務預覽 ')
mighty.grid(column=0, row=0)
for x in range(7):
    missionList2 = []
    for y in range(14):
        missionBK = tk.Label(mighty,
         bg="black",
         width=5, height=2,
         borderwidth=2, relief="groove",
         font=helv36
         )
        missionBK.grid(row =y,column = x)
        missionBK.bind("<Button-1>", lambda e,tx=x,ty=y:ClickLabel(tx, ty))

        # missionText = tk.Label(mighty,
        #  text ="",
        #  bg="white",
        #  width=0, height=0
        #  )
        # missionText.grid(row =y,column = x)

        singleMission = SingleMission(x,y)
        singleMission.UILabel = missionBK
        missionList2.append((singleMission))    
    missionList.append(missionList2)

missionEditor = ttk.LabelFrame(tab2, text=' 任務編輯 ')
missionEditor.grid(column=0, row=0)
missionNameLabel = ttk.Label(missionEditor, text="任務名稱")
missionNameLabel.grid(column=0)
missionName = tk.StringVar()
missionNameEntered = ttk.Entry(missionEditor, width=12, textvariable=missionName)
missionNameEntered.grid(column=1,row=0)

arrowButtonPanel = ttk.LabelFrame(tab2, text=' 方向按鈕 ')
arrowButtonPanel.grid(column = 0,row=1)
upButton = ttk.Button(
    arrowButtonPanel,
    text = '↑',
    width = 1,
    command=lambda :ClickArrow("up")
    )
upButton.grid(column=0, row = 0)
downButton = ttk.Button(
    arrowButtonPanel,
    text = '↓',
    width = 1
    )
downButton.grid(column=1, row = 0)
leftButton = ttk.Button(
    arrowButtonPanel,
    text = '←',
    width = 1
    )
leftButton.grid(column=2, row = 0)
rightButton = ttk.Button(
    arrowButtonPanel,
    text = '→',
    width = 1
    )
rightButton.grid(column=3, row = 0)

confirmSetting = ttk.Button(
    setPanel,
    text = '確認',
    command=SaveSetting)
confirmSetting.grid(column=0, row = 0)

# controlPanel.pack()

# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit() 

# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add another Menu to the Menu Bar and an item
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_menu)

#======================
# Start GUI
#======================
win.mainloop()