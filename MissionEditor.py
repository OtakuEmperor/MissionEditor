# coding=UTF-8
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import font
import csv


desfont = '微軟正黑體 14 bold'
bkfont = 'Courier\ New 8 bold'
fileNmae = 'MissionTree.csv'
bkFileName = 'MissionTree'

CONSTGridCol = 7
CONSTGridRow = 14

loadingDataLen = 21

# 每一個分頁所含的頁數
everyTypeContaionsPage = [[]] * 10

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
nowBigPageNumber = 0
nowSmallPageNumber = 0
allMissionBigDict = [{}] * 10
missionList = []

exportIDHead = 0
nowPageStype = 2

def DeclareVar():
    exportIDHead = 0
    nowPageStype = 2

def SaveSetting():
    tmpdata = allMissionBigDict[nowBigPageNumber][nowSmallPageNumber][nowSelectRow][nowSelectCol].Data
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
    tmpBox = allMissionBigDict[nowBigPageNumber][nowSmallPageNumber][nowSelectRow][nowSelectCol]
    if(tmpBox.UIText == None):
        tmpBox.UIText = tk.Label(mighty,
                               text=tmpBox.Data.name,
                               bg="white",
                               width=2, height=1
                               )
        tmpBox.UIText.grid(row=nowSelectRow, column=nowSelectCol)
    else:
        tmpBox.UIText['text'] = tmpBox.name


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
    posIndex = 0
    Data = None

    def __init__(self, row, col):
        self.posCol = col
        self.posRow = row
        self.posIndex = ((row * 7) + (col + 1))
        self.Data = SingleData()
        super(SingleMission, self).__init__()

    def SetLineType(self, lineType):
        self.lineType = lineType
        if(lineType == 1):
            self.UILabel.config(text="│\n│\n", fg="white")
        if(lineType == 3):
            self.UILabel.config(text="\n\n│\n│", fg="white")
        if(lineType == 4):
            self.UILabel.config(text="\n＿＿     \n", fg="white")
        if(lineType == 2):
            self.UILabel.config(text="\n     ＿＿\n", fg="white")

    def SetData(self, dataInput):
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
tab1.grid(column=0, row=0, sticky=tk.NW)    # Add the tab
tab2 = ttk.Frame(tabControl)            # Create a tab
tab2.grid(column=1, row=0, sticky=tk.NE)
pageSettingTab = ttk.Frame(tabControl)            # Create a tab
pageSettingTab.grid(column=2, row=0, sticky=tk.NE)
drawPanel = ttk.Frame(tabControl)            # Create a tab
drawPanel.grid(column=0, row=0, sticky=tk.NW)
tabControl.pack(expand=1, fill="both")
setPanel = ttk.Frame(tabControl)
setPanel.grid(column=0, row=1, sticky=tk.SW)
mighty = ttk.LabelFrame(tab1, text=' 任務預覽 ')
mighty.grid(column=0, row=0)


def ClickLabel(col, row):
    global nowSelectCol
    global nowSelectRow
    nowSelectCol = col
    nowSelectRow = row
    missionPosIndexDis['text'] = ((row * 7) + (col + 1))
    missionList = allMissionBigDict[nowBigPageNumber][nowSmallPageNumber]
    missionBoxTypeDis['text'] = (missionList[nowSelectRow][nowSelectCol].Data.boxType)
    missionLineTypeDis['text'] = (missionList[nowSelectRow][nowSelectCol].Data.lineType)
    missionName.set(missionList[nowSelectRow][nowSelectCol].Data.name)
    MoveSign.set(missionList[nowSelectRow][nowSelectCol].Data.moveSignObj)
    StaticSig.set(missionList[nowSelectRow][nowSelectCol].Data.staticSignObj)
    missionPre1.set(missionList[nowSelectRow][nowSelectCol].Data.missionPre1Obj)
    missionPre2.set(missionList[nowSelectRow][nowSelectCol].Data.missionPre2Obj)
    missionPre3.set(missionList[nowSelectRow][nowSelectCol].Data.missionPre3Obj)
    missionNeedLevel.set(missionList[nowSelectRow][nowSelectCol].Data.missionNeedLevelObj)
    missionMap.set(missionList[nowSelectRow][nowSelectCol].Data.missionSceneIDObj)
    missionStartNpc.set(missionList[nowSelectRow][nowSelectCol].Data.missionTeacherNameBeginObj)
    missionPosX.set(missionList[nowSelectRow][nowSelectCol].Data.missionTeacherXObj)
    missionPosY.set(missionList[nowSelectRow][nowSelectCol].Data.missionTeacherYObj)
    missionSpecialItem.set(missionList[nowSelectRow][nowSelectCol].Data.missionSpecialItemObj)
    missionSpecialDes.set(missionList[nowSelectRow][nowSelectCol].Data.missionSpecialDesObj)
    SetLabelBKHighLight(row, col)
    # print(missionList[nowSelectRow][nowSelectCol].UILabel.winfo_rootx())


def ClickArrow(arrorLinetype):
    allMissionBigDict[nowBigPageNumber][nowSmallPageNumber][nowSelectCol][nowSelectRow].SetLineType(arrorLinetype)


def SetLabelBKHighLight(row, col):
    missionList = allMissionBigDict[nowBigPageNumber][nowSmallPageNumber]
    for i in range(len(missionList)):
        for j in range(len(missionList[i])):
            if(i == row and j == col):
                # print(missionList[i][j].posRow)
                # print(missionList[i][j].posCol)
                # print(missionList[i][j].UILabel)
                missionList[i][j].UILabel.config(bg="red")
            else:
                missionList[i][j].UILabel.config(bg=_from_rgb((32, 100, 140)))
                # missionList[i][j].UILabel.config(bg="red")


# ======================
# 任務預覽
def GentGridPanel():
    tmpDict = allMissionBigDict[nowBigPageNumber][nowSmallPageNumber]
    # for data in tmpDict:
    for x in range(CONSTGridRow):
        if(tmpDict[x] == None):
            print("X is Empty")
            tmpDict[x] = []
        for y in range(CONSTGridCol):
            if(tmpDict[x][y]==None):
                tmpDict[x][y] = SingleMission(x, y)
            missionBK = tk.Label(mighty,
                                text="{0},{1}".format(x,y),
                                 bg=_from_rgb((32, 100, 140)),
                                 width=10, height=3,
                                 borderwidth=2, relief="groove",
                                 font=bkfont
                                 )
            missionBK.grid(row=x, column=y)
            missionBK.bind("<Button-1>", lambda e, col=y,
                           row=x: ClickLabel(col, row))
            tmpDict[x][y].UILabel = missionBK
# ======================


missionEditor = ttk.LabelFrame(tab2, text=' 任務編輯 ')
missionEditor.grid(column=0, row=0)
# ======================
# 定位點索引
missionPosIndexLabel = ttk.Label(missionEditor, text="定位點索引", font=desfont)
missionPosIndexLabel.grid(column=0, row=0)
missionPosIndex = tk.StringVar()
missionPosIndexDis = ttk.Label(
    missionEditor, text=missionPosIndex, font=desfont)
missionPosIndexDis.grid(column=1, row=0)
# ======================

# ======================
# 資料型式
missionBoxTypeLabel = ttk.Label(missionEditor, text="資料型式", font=desfont)
missionBoxTypeLabel.grid(column=0, row=1)
missionBoxType = tk.StringVar()
missionBoxTypeDis = ttk.Label(missionEditor, text=missionBoxType, font=desfont)
missionBoxTypeDis.grid(column=1, row=1)
# ======================

# ======================
# Line樣式
missionLineTypeLabel = ttk.Label(missionEditor, text="Line樣式", font=desfont)
missionLineTypeLabel.grid(column=0, row=2)
missionLineType = tk.StringVar()
missionLineTypeDis = ttk.Label(
    missionEditor, text=missionLineType, font=desfont)
missionLineTypeDis.grid(column=1, row=2)
# ======================

# ======================
# 任務名稱
missionNameLabel = ttk.Label(missionEditor, text="任務名稱", font=desfont)
missionNameLabel.grid(column=0, row=3)
missionName = tk.StringVar()
missionNameEntered = ttk.Entry(
    missionEditor, width=12, textvariable=missionName, font=desfont)
missionNameEntered.grid(column=1, row=3)
# ======================

# ======================
# 動標
missionMoveSignLabel = ttk.Label(missionEditor, text="動標", font=desfont)
missionMoveSignLabel.grid(column=0, row=4)
MoveSign = tk.StringVar()
missionMoveSignEntered = ttk.Entry(
    missionEditor, width=12, textvariable=MoveSign, font=desfont)
missionMoveSignEntered.grid(column=1, row=4)
# ======================

# ======================
# 永標
missionStaticSignLabel = ttk.Label(missionEditor, text="永標", font=desfont)
missionStaticSignLabel.grid(column=0, row=5)
StaticSig = tk.StringVar()
missionStaticSignEntered = ttk.Entry(
    missionEditor, width=12, textvariable=StaticSig, font=desfont)
missionStaticSignEntered.grid(column=1, row=5)
# ======================

# ======================
# 前置任務索引1
missionPre1Label = ttk.Label(missionEditor, text="前置任務索引1", font=desfont)
missionPre1Label.grid(column=0, row=6)
missionPre1 = tk.StringVar()
missionPre1Entered = ttk.Entry(
    missionEditor, width=12, textvariable=missionPre1, font=desfont)
missionPre1Entered.grid(column=1, row=6)
# ======================

# ======================
# 前置任務索引2
missionPre2Label = ttk.Label(missionEditor, text="前置任務索引2", font=desfont)
missionPre2Label.grid(column=0, row=7)
missionPre2 = tk.StringVar()
missionPre2Entered = ttk.Entry(
    missionEditor, width=12, textvariable=missionPre2, font=desfont)
missionPre2Entered.grid(column=1, row=7)
# ======================

# ======================
# 前置任務索引3
missionPre3Label = ttk.Label(missionEditor, text="前置任務索引3", font=desfont)
missionPre3Label.grid(column=0, row=8)
missionPre3 = tk.StringVar()
missionPre3Entered = ttk.Entry(
    missionEditor, width=12, textvariable=missionPre3, font=desfont)
missionPre3Entered.grid(column=1, row=8)
# ======================

# ======================
# 所需等級
missionNeedLevelLabel = ttk.Label(missionEditor, text="所需等級", font=desfont)
missionNeedLevelLabel.grid(column=0, row=9)
missionNeedLevel = tk.StringVar()
missionNeedLevelEntered = ttk.Entry(
    missionEditor, width=12, textvariable=missionNeedLevel, font=desfont)
missionNeedLevelEntered.grid(column=1, row=9)
# ======================

# ======================
# 起始地圖
missionMapLabel = ttk.Label(missionEditor, text="起始地圖", font=desfont)
missionMapLabel.grid(column=0, row=10)
missionMap = tk.StringVar()
missionMapEntered = ttk.Entry(
    missionEditor, width=12, textvariable=missionMap, font=desfont)
missionMapEntered.grid(column=1, row=10)
# ======================

# ======================
# 起始NPC
missionStartNpcLabel = ttk.Label(missionEditor, text="起始NPC", font=desfont)
missionStartNpcLabel.grid(column=0, row=11)
missionStartNpc = tk.StringVar()
missionStartNpcEntered = ttk.Entry(
    missionEditor, width=12, textvariable=missionStartNpc, font=desfont)
missionStartNpcEntered.grid(column=1, row=11)
# ======================

# ======================
# 所在座標X
missionPosXLabel = ttk.Label(missionEditor, text="所在座標X", font=desfont)
missionPosXLabel.grid(column=0, row=12)
missionPosX = tk.StringVar()
missionPosXEntered = ttk.Entry(
    missionEditor, width=12, textvariable=missionPosX, font=desfont)
missionPosXEntered.grid(column=1, row=12)
# ======================

# ======================
# 所在座標Y
missionPosYLabel = ttk.Label(missionEditor, text="所在座標Y", font=desfont)
missionPosYLabel.grid(column=0, row=13)
missionPosY = tk.StringVar()
missionPosYEntered = ttk.Entry(
    missionEditor, width=12, textvariable=missionPosY, font=desfont)
missionPosYEntered.grid(column=1, row=13)
# ======================

# ======================
# 特殊獎勵
missionSpecialItemLabel = ttk.Label(missionEditor, text="特殊獎勵", font=desfont)
missionSpecialItemLabel.grid(column=0, row=14)
missionSpecialItem = tk.StringVar()
missionSpecialItemEntered = ttk.Entry(
    missionEditor, width=12, textvariable=missionSpecialItem, font=desfont)
missionSpecialItemEntered.grid(column=1, row=14)
# ======================

# ======================
# 特殊說明
missionSpecialDesLabel = ttk.Label(missionEditor, text="特殊說明", font=desfont)
missionSpecialDesLabel.grid(column=0, row=15)
missionSpecialDes = tk.StringVar()
missionSpecialDesEntered = ttk.Entry(
    missionEditor, width=12, textvariable=missionSpecialDes, font=desfont)
missionSpecialDesEntered.grid(column=1, row=15)
# ======================

arrowButtonPanel = ttk.LabelFrame(tab2, text=' 方向按鈕 ')
arrowButtonPanel.grid(column=0, row=1)
upButton = ttk.Button(
    arrowButtonPanel,
    text='↑',
    width=3,
    command=lambda: ClickArrow(1)
)
upButton.grid(column=0, row=0)
rightButton = ttk.Button(
    arrowButtonPanel,
    text='→',
    width=3,
    command=lambda: ClickArrow(2)
)
rightButton.grid(column=1, row=0)
downButton = ttk.Button(
    arrowButtonPanel,
    text='↓',
    width=3,
    command=lambda: ClickArrow(3)
)
downButton.grid(column=2, row=0)
leftButton = ttk.Button(
    arrowButtonPanel,
    text='←',
    width=3,
    command=lambda: ClickArrow(4)
)
leftButton.grid(column=3, row=0)

upRightButton = ttk.Button(
    arrowButtonPanel,
    text='└',
    width=3
)
upRightButton.grid(column=0, row=1)

downRightButton = ttk.Button(
    arrowButtonPanel,
    text='┌',
    width=3
)
downRightButton.grid(column=1, row=1)

downLeftButton = ttk.Button(
    arrowButtonPanel,
    text='┐',
    width=3
)
downLeftButton.grid(column=2, row=1)

upLeftButton = ttk.Button(
    arrowButtonPanel,
    text='┘',
    width=3
)
upLeftButton.grid(column=3, row=1)

verticalButton = ttk.Button(
    arrowButtonPanel,
    text='│',
    width=3
)
verticalButton.grid(column=0, row=2)

horizontalButton = ttk.Button(
    arrowButtonPanel,
    text='—',
    width=3
)
horizontalButton.grid(column=1, row=2)

crossButton = ttk.Button(
    arrowButtonPanel,
    text='┼',
    width=3
)
crossButton.grid(column=2, row=2)

confirmSetting = ttk.Button(
    setPanel,
    text='確認',
    command=SaveSetting)
confirmSetting.grid(column=0, row=0)


# ======================
# 任務類型選擇
missionBigType = tk.StringVar(win)
missionBigType.set(bigMissionType[0])  # default value
missionBigTypeLabel = ttk.Label(pageSettingTab, text="任務類型選擇", font=desfont)
missionBigTypeLabel.grid(column=0, row=0)
missionBigTypeDropdown = ttk.OptionMenu(
    pageSettingTab, missionBigType, *bigMissionType)
missionBigTypeDropdown.config(width=12)
missionBigTypeDropdown.grid(column=1, row=0, sticky="n")
# ======================

# ======================
# 分頁頁碼選擇
missionSmaillType = tk.StringVar(win)
missionSmaillType.set(smallMissionType[0])  # default value
missionSmaillTypeLabel = ttk.Label(pageSettingTab, text="分頁頁碼選擇", font=desfont)
missionSmaillTypeLabel.grid(column=0, row=1)
missionSmaillTypeDropdown = ttk.OptionMenu(
    pageSettingTab, missionSmaillType, *smallMissionType)
missionSmaillTypeDropdown.config(width=12)
missionSmaillTypeDropdown.grid(column=1, row=1, sticky="n")
# ======================

# ======================
# 新增小頁籤按鈕
confirmSetting = ttk.Button(
    pageSettingTab,
    text='新增小頁籤',
    command=SaveSetting)
confirmSetting.grid(column=0, row=2)
# ======================

# Exit GUI cleanly


def _quit():
    win.quit()
    win.destroy()
    exit()


def ImportData():
    with open(fileNmae, newline='',encoding='utf-8', 
        errors='ignore') as inputFile:
        rows = csv.reader(fileNmae)
        for index, row in enumerate(rows):
            if(len(row) < loadingDataLen and index == 0):
                everyTypeContaionsPage[0].append(0)
                allMissionBigDict[0][0] = [[None for x in range(CONSTGridCol)] for y in range(CONSTGridRow)] 
                # print(allMissionBigDict[0][0])
                # for x in range(len(allMissionBigDict[0][0])):
                #     for y in range(len(allMissionBigDict[0][0][0])):
                #         print(hex(id(allMissionBigDict[0][0][x][y])))
                break
            print("Not break")
            if row[4] not in everyTypeContaionsPage[row[2]]:
                everyTypeContaionsPage[row[2]].append(row[4])
                allMissionBigDict[row[2]][row[4]] = [[None * CONSTGridCol]]*CONSTGridRow
            tmpData = SingleMission((row[5] % CONSTGridCol) - 1,(row[5] / CONSTGridCol) - 1)
            tmpData.Data.boxType = row[6]
            tmpData.Data.lineType = row[7]
            tmpData.Data.name = row[8]
            tmpData.Data.moveSignObj = row[9]
            tmpData.Data.staticSignObj = row[10]
            tmpData.Data.missionPre1Obj = row[11]
            tmpData.Data.missionPre2Obj = row[12]
            tmpData.Data.missionPre3Obj = row[13]
            tmpData.Data.missionNeedLevelObj = row[14]
            tmpData.Data.missionSceneIDObj = row[15]
            tmpData.Data.missionTeacherNameBeginObj = row[16]
            tmpData.Data.missionTeacherXObj = row[17]
            tmpData.Data.missionTeacherYObj = row[18]
            tmpData.Data.missionSpecialItemObj = row[19]
            tmpData.Data.missionSpecialDesObj = row[20]
            print("{0},{1} Add Data".format(tmpData.posRow, tmpData.posCol))
            allMissionBigDict[row[2]][row[4]][tmpData.posRow][tmpData.posCol] = tmpData


def ExportData():
    global exportIDHead
    with open(fileNmae, "w", newline='',encoding='utf-8', 
        errors='ignore') as outputFile:
        writer = csv.writer(outputFile)
        for Bkey, Bdata in enumerate(allMissionBigDict):
            for Skey, Sdata in Bdata.items():
                for i in range(len(Sdata)):
                    for j in range(len(Sdata[0])):
                        print(Sdata[i][j].Data)
                        writer.writerow([
                            exportIDHead,
                            1,
                            Bkey,
                            nowPageStype,
                            Skey,
                            ((i)*7)+(j+1),
                            Sdata[i][j].Data.boxType,
                            Sdata[i][j].Data.lineType,
                            Sdata[i][j].Data.name,
                            Sdata[i][j].Data.moveSignObj,
                            Sdata[i][j].Data.staticSignObj,
                            Sdata[i][j].Data.missionPre1Obj,
                            Sdata[i][j].Data.missionPre2Obj,
                            Sdata[i][j].Data.missionPre3Obj,
                            Sdata[i][j].Data.missionNeedLevelObj,
                            Sdata[i][j].Data.missionSceneIDObj,
                            Sdata[i][j].Data.missionTeacherNameBeginObj,
                            Sdata[i][j].Data.missionTeacherXObj,
                            Sdata[i][j].Data.missionTeacherYObj,
                            Sdata[i][j].Data.missionSpecialItemObj,
                            Sdata[i][j].Data.missionSpecialDesObj
                        ])
                        exportIDHead += 1


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


# ======================
# 初始化資料
DeclareVar()
ImportData()
GentGridPanel()
# ======================


# ======================
# Start GUI
# ======================
win.mainloop()
