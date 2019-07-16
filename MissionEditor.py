import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import font
import csv








desfont = '微軟正黑體 18 bold'
bkfont = 'Courier\ New 8 bold'
fileNmae = 'MissionTree.csv'
bkFileName = 'MissionTree'




bigMissionType = [
"主線",
"支線",
"組隊",
"特殊",
"增補",
"皇榜",
"關卡",
"時空",
"活動"
]




smallMissionType = [1]




nowSelectRow = 0
nowSelectCol = 0
nowBigPageNumber = 1
nowSmallPageNumber = 1
allMissionBigDict = {}
allMissionSmallDict = {}
missionList = []




exportIDHead = 0
nowPageStype = 2




def SaveSetting():
    global mighty
    global nowSelectCol
    global nowSelectRow
    tmpdata = SingleData()
    tmpdata.name = missionName.get()
    tmpdata.lineType = missionName.get()
    tmpdata.moveSignObj = MoveSign.get()
    tmpdata.staticSignObj = StaticSig.get()
    tmpdata.missionPre1Obj = missionPre1.get()
    tmpdata.missionPre2Obj = missionPre2.get()
    tmpdata.missionPre3Obj = missionPre3.get()
    tmpdata.missionNeedLevelObj = missionNeedLevel.get()
    tmpdata.missionSceneIDObj = missionMap.get()
    tmpdata.missionTeacherNameBeginObj = missionStartNpc.get()
    tmpdata.missionTeacherXObj = missionPosX.get()
    tmpdata.missionTeacherYObj = missionPosY.get()
    tmpdata.missionSpecialItemObj = missionSpecialItem.get()
    tmpdata.missionSpecialDesObj = missionSpecialDes.get()
    missionList[nowSelectCol][nowSelectRow].SetData(tmpdata)
    if(missionList[nowSelectCol][nowSelectRow].UIText == None):
        missionText = tk.Label(mighty,
         text = missionList[nowSelectCol][nowSelectRow].Data.name,
         bg="white",
         width=2, height=1
         )
        missionText.grid(row =nowSelectRow,column = nowSelectCol)
        missionList[nowSelectCol][nowSelectRow].UIText = missionText
    else:
        missionList[nowSelectCol][nowSelectRow].UIText['text']=missionList[nowSelectCol][nowSelectRow].name








class SingleData(object):
    name = "1"
    boxType = 0
    lineType = 0
    moveSignObj = 0
    staticSignObj = 0
    missionPre1Obj = 0
    missionPre2Obj = 0
    missionPre3Obj = 0
    missionNeedLevelObj = 0
    missionSceneIDObj = 0
    missionTeacherNameBeginObj = ""
    missionTeacherXObj = 0
    missionTeacherYObj = 0
    missionSpecialItemObj = ""
    missionSpecialDesObj = ""




    def __init__(self):
        super(SingleData, self).__init__()




class SingleMission(object):




    UILabel = None
    UIText = None
    posRow = 0
    posCol = 0
    Data = SingleData()




    def __init__(self, col, row):
        self.posCol = col
        self.posRow = row
        super(SingleMission, self).__init__()
    def SetLineType( self, lineType ):
        self.lineType = lineType
        if(lineType == 1):
            self.UILabel.config(text="│\n│\n",fg="white")
        if(lineType == 3):
            self.UILabel.config(text="\n\n│\n│",fg="white")
        if(lineType == 4):
            self.UILabel.config(text="\n＿＿     \n",fg="white")
        if(lineType == 2):
            self.UILabel.config(text="\n     ＿＿\n",fg="white")
    def SetData(self,dataInput ):
        self.Data.name = dataInput.name
        self.Data.boxType = dataInput.boxType
        self.Data.lineType = dataInput.lineType
        self.Data.moveSignObj = dataInput.moveSignObj
        self.Data.staticSignObj = dataInput.staticSignObj
        self.Data.missionPre1Obj = dataInput.missionPre1Obj
        self.Data.missionPre2Obj = dataInput.missionPre2Obj
        self.Data.missionPre3Obj = dataInput.missionPre3Obj
        self.Data.missionNeedLevelObj = dataInput.missionNeedLevelObj
        self.Data.missionSceneIDObj = dataInput.missionSceneIDObj
        self.Data.missionTeacherNameBeginObj = dataInput.missionTeacherNameBeginObj
        self.Data.missionTeacherXObj = dataInput.missionTeacherXObj
        self.Data.missionTeacherYObj = dataInput.missionTeacherYObj
        self.Data.missionSpecialDesObj = dataInput.missionSpecialDesObj
        




def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb   




test = 0




# Create instance
win = tk.Tk()   




# Add a title       
win.title("任務編輯器")  
win.geometry("1360x768")




tabControl = ttk.Frame(win)          # Create Tab Control




tab1 = ttk.Frame(tabControl)            # Create a tab 
tab1.grid(column=0, row=0,sticky=tk.NW)    # Add the tab
tab2 = ttk.Frame(tabControl)            # Create a tab 
tab2.grid(column=1, row=0,sticky=tk.NE)
pageSettingTab = ttk.Frame(tabControl)            # Create a tab 
pageSettingTab.grid(column=2, row=0,sticky=tk.NE)
drawPanel = ttk.Frame(tabControl)            # Create a tab 
drawPanel.grid(column=0, row=0,sticky=tk.NW)
tabControl.pack(expand=1, fill="both")
setPanel = ttk.Frame(tabControl)
setPanel.grid(column=0,row=1,sticky=tk.SW)












def ClickLabel( col, row ):
    global nowSelectCol
    global nowSelectRow
    nowSelectCol = col
    nowSelectRow = row
    SetLabelBKHighLight(col,row)
    print(missionList[nowSelectCol][nowSelectRow].UILabel.winfo_rootx())




def ClickArrow( arrorLinetype ):
    missionList[nowSelectCol][nowSelectRow].SetLineType( arrorLinetype )




def SetLabelBKHighLight ( col, row):




    for i in range(len(missionList)):
        for j in range(len(missionList[i])):
            if(i == col and j == row):
                missionList[i][j].UILabel.config(bg="red")
            else:
                missionList[i][j].UILabel.config(bg=_from_rgb((32,100,140)))
#======================
# B Panel
#======================
mighty = ttk.LabelFrame(tab1, text=' 任務預覽 ')
mighty.grid(column=0, row=0)
for x in range(7):
    missionList2 = []
    for y in range(14):
        missionBK = tk.Label(mighty,
         bg= _from_rgb((32,100,140)),
         width=10, height=3,
         borderwidth=2, relief="groove",
         font=bkfont
         )
        missionBK.grid(row =y,column = x)
        missionBK.bind("<Button-1>", lambda e,tx=x,ty=y:ClickLabel(tx, ty))
        # canvas = tk.Canvas(missionBK)
        # canvas.pack()
        # canvas.create_line(10,10,20,20, fill='black')




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
#======================
# 定位點索引
missionPosIndexLabel = ttk.Label(missionEditor, text="定位點索引",font=desfont)
missionPosIndexLabel.grid(column=0,row=0)
missionPosIndex = tk.StringVar()
missionPosIndexDis = ttk.Label(missionEditor, text=missionPosIndex,font=desfont)
missionPosIndexDis.grid(column=1,row=0)
#======================




#======================
# 資料型式
missionBoxTypeLabel = ttk.Label(missionEditor, text="資料型式",font=desfont)
missionBoxTypeLabel.grid(column=0,row=1)
missionBoxType = tk.StringVar()
missionBoxTypeDis = ttk.Label(missionEditor, text=missionBoxType,font=desfont)
missionBoxTypeDis.grid(column=1,row=1)
#======================




#======================
# Line樣式
missionLineTypeLabel = ttk.Label(missionEditor, text="Line樣式",font=desfont)
missionLineTypeLabel.grid(column=0,row=2)
missionLineType = tk.StringVar()
missionPosIndexDis = ttk.Label(missionEditor, text=missionLineType,font=desfont)
missionPosIndexDis.grid(column=1,row=2)
#======================




#======================
# 任務名稱
missionNameLabel = ttk.Label(missionEditor, text="任務名稱",font=desfont)
missionNameLabel.grid(column=0,row=3)
missionName = tk.StringVar()
missionNameEntered = ttk.Entry(missionEditor, width=12, textvariable=missionName,font=desfont)
missionNameEntered.grid(column=1,row=3)
#======================




#======================
# 動標
missionMoveSignLabel = ttk.Label(missionEditor, text="動標",font=desfont)
missionMoveSignLabel.grid(column=0,row=4)
MoveSign = tk.StringVar()
missionMoveSignEntered = ttk.Entry(missionEditor, width=12, textvariable=MoveSign,font=desfont)
missionMoveSignEntered.grid(column=1,row=4)
#======================




#======================
# 永標
missionStaticSignLabel = ttk.Label(missionEditor, text="永標",font=desfont)
missionStaticSignLabel.grid(column=0,row=5)
StaticSig = tk.StringVar()
missionStaticSignEntered = ttk.Entry(missionEditor, width=12, textvariable=StaticSig,font=desfont)
missionStaticSignEntered.grid(column=1,row=5)
#======================




#======================
# 前置任務索引1
missionPre1Label = ttk.Label(missionEditor, text="前置任務索引1",font=desfont)
missionPre1Label.grid(column=0,row=6)
missionPre1 = tk.StringVar()
missionPre1Entered = ttk.Entry(missionEditor, width=12, textvariable=missionPre1,font=desfont)
missionPre1Entered.grid(column=1,row=6)
#======================




#======================
# 前置任務索引2
missionPre2Label = ttk.Label(missionEditor, text="前置任務索引2",font=desfont)
missionPre2Label.grid(column=0,row=7)
missionPre2 = tk.StringVar()
missionPre2Entered = ttk.Entry(missionEditor, width=12, textvariable=missionPre2,font=desfont)
missionPre2Entered.grid(column=1,row=7)
#======================




#======================
# 前置任務索引3
missionPre3Label = ttk.Label(missionEditor, text="前置任務索引3",font=desfont)
missionPre3Label.grid(column=0,row=8)
missionPre3 = tk.StringVar()
missionPre3Entered = ttk.Entry(missionEditor, width=12, textvariable=missionPre3,font=desfont)
missionPre3Entered.grid(column=1,row=8)
#======================




#======================
# 所需等級
missionNeedLevelLabel = ttk.Label(missionEditor, text="所需等級",font=desfont)
missionNeedLevelLabel.grid(column=0,row=9)
missionNeedLevel = tk.StringVar()
missionNeedLevelEntered = ttk.Entry(missionEditor, width=12, textvariable=missionNeedLevel,font=desfont)
missionNeedLevelEntered.grid(column=1,row=9)
#======================




#======================
# 起始地圖
missionMapLabel = ttk.Label(missionEditor, text="起始地圖",font=desfont)
missionMapLabel.grid(column=0,row=10)
missionMap = tk.StringVar()
missionMapEntered = ttk.Entry(missionEditor, width=12, textvariable=missionMap,font=desfont)
missionMapEntered.grid(column=1,row=10)
#======================




#======================
# 起始NPC
missionStartNpcLabel = ttk.Label(missionEditor, text="起始NPC",font=desfont)
missionStartNpcLabel.grid(column=0,row=11)
missionStartNpc = tk.StringVar()
missionStartNpcEntered = ttk.Entry(missionEditor, width=12, textvariable=missionStartNpc,font=desfont)
missionStartNpcEntered.grid(column=1,row=11)
#======================




#======================
# 所在座標X
missionPosXLabel = ttk.Label(missionEditor, text="所在座標X",font=desfont)
missionPosXLabel.grid(column=0,row=12)
missionPosX = tk.StringVar()
missionPosXEntered = ttk.Entry(missionEditor, width=12, textvariable=missionPosX,font=desfont)
missionPosXEntered.grid(column=1,row=12)
#======================




#======================
# 所在座標Y
missionPosYLabel = ttk.Label(missionEditor, text="所在座標Y",font=desfont)
missionPosYLabel.grid(column=0,row=13)
missionPosY = tk.StringVar()
missionPosYEntered = ttk.Entry(missionEditor, width=12, textvariable=missionPosY,font=desfont)
missionPosYEntered.grid(column=1,row=13)
#======================




#======================
# 特殊獎勵
missionSpecialItemLabel = ttk.Label(missionEditor, text="特殊獎勵",font=desfont)
missionSpecialItemLabel.grid(column=0,row=14)
missionSpecialItem = tk.StringVar()
missionSpecialItemEntered = ttk.Entry(missionEditor, width=12, textvariable=missionSpecialItem,font=desfont)
missionSpecialItemEntered.grid(column=1,row=14)
#======================




#======================
# 特殊說明
missionSpecialDesLabel = ttk.Label(missionEditor, text="特殊說明",font=desfont)
missionSpecialDesLabel.grid(column=0,row=15)
missionSpecialDes = tk.StringVar()
missionSpecialDesEntered = ttk.Entry(missionEditor, width=12, textvariable=missionSpecialDes,font=desfont)
missionSpecialDesEntered.grid(column=1,row=15)
#======================




arrowButtonPanel = ttk.LabelFrame(tab2, text=' 方向按鈕 ')
arrowButtonPanel.grid(column = 0,row=1)
upButton = ttk.Button(
    arrowButtonPanel,
    text = '↑',
    width = 3,
    command=lambda :ClickArrow(1)
    )
upButton.grid(column=0, row = 0)
rightButton = ttk.Button(
    arrowButtonPanel,
    text = '→',
    width = 3,
    command=lambda :ClickArrow(2)
    )
rightButton.grid(column=1, row = 0)
downButton = ttk.Button(
    arrowButtonPanel,
    text = '↓',
    width = 3,
    command=lambda :ClickArrow(3)
    )
downButton.grid(column=2, row = 0)
leftButton = ttk.Button(
    arrowButtonPanel,
    text = '←',
    width = 3,
    command=lambda :ClickArrow(4)
    )
leftButton.grid(column=3, row = 0)




upRightButton = ttk.Button(
    arrowButtonPanel,
    text = '└',
    width = 3
    )
upRightButton.grid(column=0, row = 1)




downRightButton = ttk.Button(
    arrowButtonPanel,
    text = '┌',
    width = 3
    )
downRightButton.grid(column=1, row = 1)




downLeftButton = ttk.Button(
    arrowButtonPanel,
    text = '┐',
    width = 3
    )
downLeftButton.grid(column=2, row = 1)




upLeftButton = ttk.Button(
    arrowButtonPanel,
    text = '┘',
    width = 3
    )
upLeftButton.grid(column=3, row = 1)




verticalButton = ttk.Button(
    arrowButtonPanel,
    text = '│',
    width = 3
    )
verticalButton.grid(column=0, row = 2)




horizontalButton = ttk.Button(
    arrowButtonPanel,
    text = '—',
    width = 3
    )
horizontalButton.grid(column=1, row = 2)




crossButton = ttk.Button(
    arrowButtonPanel,
    text = '┼',
    width = 3
    )
crossButton.grid(column=2, row = 2)




confirmSetting = ttk.Button(
    setPanel,
    text = '確認',
    command=SaveSetting)
confirmSetting.grid(column=0, row = 0)








#======================
# 任務類型選擇
missionBigType = tk.StringVar(win)
missionBigType.set(bigMissionType[0]) # default value
missionBigTypeLabel = ttk.Label(pageSettingTab, text="任務類型選擇",font=desfont)
missionBigTypeLabel.grid(column=0,row=0)
missionBigTypeDropdown = ttk.OptionMenu(pageSettingTab,missionBigType,*bigMissionType)
missionBigTypeDropdown.config(width=12)
missionBigTypeDropdown.grid(column=1,row=0,sticky="n")
#======================




#======================
# 分頁頁碼選擇
missionSmaillType = tk.StringVar(win)
missionSmaillType.set(smallMissionType[0]) # default value
missionSmaillTypeLabel = ttk.Label(pageSettingTab, text="分頁頁碼選擇",font=desfont)
missionSmaillTypeLabel.grid(column=0,row=1)
missionSmaillTypeDropdown = ttk.OptionMenu(pageSettingTab,missionSmaillType,*smallMissionType)
missionSmaillTypeDropdown.config(width=12)
missionSmaillTypeDropdown.grid(column=1,row=1,sticky="n")
#======================




#======================
# 新增小頁籤按鈕
confirmSetting = ttk.Button(
    pageSettingTab,
    text = '新增小頁籤',
    command=SaveSetting)
confirmSetting.grid(column=0, row = 2)
#======================




# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit() 




def ExportData():
    with open(fileNmae,"w", newline= '') as outputFile:
        writer = csv.writer(outputFile)
        for Bkey, Bdata in allMissionBigDict.items():
            for Skey, Sdata in Bdata.items():
                for j in range(len(Sdata[0])):
                    for i in range(len(Sdata)):
                        writer.writerow([
                            exportIDHead,
                            1,
                            Bkey,
                            nowPageStype,
                            Skey,
                            ((j)*7)+(i+1),
                            Sdata[i][j].boxType,
                            Sdata[i][j].lineType,
                            Sdata[i][j].name,
                            Sdata[i][j].moveSignObj,
                            Sdata[i][j].staticSignObj,
                            Sdata[i][j].missionPre1Obj,
                            Sdata[i][j].missionPre2Obj,
                            Sdata[i][j].missionPre3Obj,
                            Sdata[i][j].missionNeedLevelObj,
                            Sdata[i][j].missionSceneIDObj,
                            Sdata[i][j].missionTeacherNameBeginObj,
                            Sdata[i][j].missionTeacherXObj,
                            Sdata[i][j].missionTeacherYObj,
                            Sdata[i][j].missionSpecialItemObj,
                            Sdata[i][j].missionSpecialDesObj
                            ])








# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)




# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="匯出", command=ExportData)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)




# Add another Menu to the Menu Bar and an item
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_menu)








#======================
# 初始化資料
allMissionBigDict[nowBigPageNumber] = allMissionSmallDict
allMissionSmallDict[nowSmallPageNumber] = missionList
#======================








#======================
# Start GUI
#======================
win.mainloop()