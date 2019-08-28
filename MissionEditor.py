# coding=UTF-8
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import font
from enum import Enum
from enum import IntEnum
import io
import sys
import csv
import math
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf8",
                              line_buffering=True)

desfont = '微軟正黑體 14 bold'
bkfont = 'Courier\ New 8 bold'
fileNmae = 'MissionTree.csv'
bkFileName = 'MissionTree'

CONSTGridCol = 5
CONSTGridRow = 14
CONSTGPageNumber = 9

loadingDataLen = 18

# 每一個分頁所含的頁數

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

smallMissionType = []

allMissionBigDict = None
everyTypeContaionsPage = None

missionEditorText = [
    "定位點索引",
    "資料型式",
    "Line樣式",
    "任務名稱",
    "任務字串ID",
    "動標",
    "永標",
    "所需等級",
    "起始地圖",
    "起始NPC",
    "所在座標X",
    "所在座標Y",
    "特殊獎勵ID",
    "特殊說明ID"
]

class MissionEditorIndex (IntEnum):
    boxPos = 0,
    boxType = 1,
    lineType = 2,
    name = 3,
    nameID = 4,
    moveSignObj = 5,
    staticSignObj = 6,
    missionNeedLevelObj = 7,
    missionSceneIDObj = 8,
    missionTeacherNameBeginObj = 9,
    missionTeacherXObj = 10,
    missionTeacherYObj = 11,
    missionSpecialItemObj = 12,
    missionSpecialDesObj = 13


CONSTEditorNumber = len(missionEditorText)

missionEditorLabel = []

missionEditorVar = []

missionEditorDes = []

nowSelectRow = 0
nowSelectCol = 0
nowBigPageNumber = 0
nowSmallPageNumber = 0

missionList = []

exportIDHead = 1
nowPageStype = 1


def ChangePanelType( number ):
    global CONSTGridCol
    CONSTGridCol = number

def DeclareVar():
    global exportIDHead
    global nowPageStype
    global allMissionBigDict
    global everyTypeContaionsPage
    exportIDHead = 1
    nowPageStype = 1
    allMissionBigDict = [{} for y in range(CONSTGPageNumber)]
    everyTypeContaionsPage = [[] for y in range(CONSTGPageNumber)]

def SaveSetting():
    global allMissionBigDict
    tmpdata = allMissionBigDict[nowBigPageNumber][nowSmallPageNumber][nowSelectRow][nowSelectCol].Data
    for x in range(CONSTEditorNumber):
        tmpdata[x] = missionEditorVar[x].get()
    tmpBox = allMissionBigDict[nowBigPageNumber][nowSmallPageNumber][nowSelectRow][nowSelectCol]
    if(tmpdata[MissionEditorIndex.name] != ""):
        if(tmpdata[MissionEditorIndex.boxType] == 0):
            tmpdata[MissionEditorIndex.boxType] = 1
        if(tmpdata[MissionEditorIndex.boxType] == 2):
            tmpdata[MissionEditorIndex.boxType] = 3
        missionEditorDes[MissionEditorIndex.boxType]["text"] = tmpdata[MissionEditorIndex.boxType]
        if(tmpBox.UIText == None):
            tmpBox.UIText = tk.Label(mighty,
                                   text=tmpdata[MissionEditorIndex.name],
                                   bg="white",
                                   width=2, height=1
                                   )
            tmpBox.UIText.grid(row=nowSelectRow, column=nowSelectCol)
        else:
            tmpBox.UIText['text'] = tmpdata[MissionEditorIndex.nam]

class LineFormatData(object):
    global CONSTGridCol
    global CONSTGridRow
    global allMissionBigDict
    pos = None
    def __init__(self):
        self.pos = ['','　　','','　　','','']
    def GetFinalLine(self):
        return '{0}\n{1}{2}{3}\n{4}\n{5}'.format(self.pos[0],self.pos[1],self.pos[2],
            self.pos[3],self.pos[4],self.pos[5]
            )
    
    def AddLine( self, lineType, row, col):
        nowSubLinePar = allMissionBigDict[nowBigPageNumber][nowSmallPageNumber]
        if( lineType < 13):
            self.AddMainPos(lineType)
            sublineCanSetAy = self.CheckIndexInRange(row,col,lineType)
            sublineAy = self.GetSubIndex(row,col,lineType)
            if type(sublineCanSetAy) == type(""):
                if(sublineCanSetAy == "True"):
                    nowSubLinePar[sublineAy[0]][sublineAy[1]].LineFormat.AddMainPos(int(sublineAy[2]))
                    nowSubLinePar[sublineAy[0]][sublineAy[1]].UILabel.config(text =nowSubLinePar[sublineAy[0]][sublineAy[1]].LineFormat.GetFinalLine(),fg="white")
            else:
                for idx, bol in enumerate(sublineCanSetAy):
                    if bol == "True":
                        if idx == 0:
                            print("idx1")
                            nowSubLinePar[sublineAy[0]][sublineAy[1]].LineFormat.AddMainPos(sublineAy[2])
                            nowSubLinePar[sublineAy[0]][sublineAy[1]].UILabel.config(text =nowSubLinePar[sublineAy[0]][sublineAy[1]].LineFormat.GetFinalLine(),fg="white")
                        if idx == 1:
                            print("idx2")
                            nowSubLinePar[sublineAy[3]][sublineAy[4]].LineFormat.AddMainPos(sublineAy[5])
                            nowSubLinePar[sublineAy[3]][sublineAy[4]].UILabel.config(text =nowSubLinePar[sublineAy[3]][sublineAy[4]].LineFormat.GetFinalLine(),fg="white")
                        if idx == 2:
                            print("idx3")
                            nowSubLinePar[sublineAy[6]][sublineAy[7]].LineFormat.AddMainPos(sublineAy[8])
                            nowSubLinePar[sublineAy[6]][sublineAy[7]].UILabel.config(text =nowSubLinePar[sublineAy[6]][sublineAy[7]].LineFormat.GetFinalLine(),fg="white")
                        if idx == 3:
                            print("idx4")
                            nowSubLinePar[sublineAy[9]][sublineAy[10]].LineFormat.AddMainPos(sublineAy[11])
                            nowSubLinePar[sublineAy[9]][sublineAy[10]].UILabel.config(text =nowSubLinePar[sublineAy[9]][sublineAy[10]].LineFormat.GetFinalLine(),fg="white")
                
                
    def DelLine( self, lineType, row, col):
        nowSubLinePar = allMissionBigDict[nowBigPageNumber][nowSmallPageNumber]
        if( lineType < 13):
            self.DelMainLine(lineType)
            sublineCanSetAy = self.CheckIndexInRange(row,col,lineType)
            sublineAy = self.GetSubIndex(row,col,lineType)
            if type(sublineCanSetAy) == type(""):
                if(sublineCanSetAy == "True"):
                    nowSubLinePar[sublineAy[0]][sublineAy[1]].LineFormat.DelMainLine(sublineAy[2])
                    nowSubLinePar[sublineAy[0]][sublineAy[1]].UILabel.config(text =nowSubLinePar[sublineAy[0]][sublineAy[1]].LineFormat.GetFinalLine(),fg="white")
            else:
                for idx, bol in enumerate(sublineCanSetAy):
                    if bol == "True":
                        if idx == 0:
                            nowSubLinePar[sublineAy[0]][sublineAy[1]].LineFormat.DelMainLine(sublineAy[2])
                            nowSubLinePar[sublineAy[0]][sublineAy[1]].UILabel.config(text =nowSubLinePar[sublineAy[0]][sublineAy[1]].LineFormat.GetFinalLine(),fg="white")
                        if idx == 1:
                            nowSubLinePar[sublineAy[3]][sublineAy[4]].LineFormat.DelMainLine(sublineAy[5])
                            nowSubLinePar[sublineAy[3]][sublineAy[4]].UILabel.config(text =nowSubLinePar[sublineAy[3]][sublineAy[4]].LineFormat.GetFinalLine(),fg="white")
                        if idx == 2:
                            nowSubLinePar[sublineAy[6]][sublineAy[7]].LineFormat.DelMainLine(sublineAy[8])
                            nowSubLinePar[sublineAy[6]][sublineAy[7]].UILabel.config(text =nowSubLinePar[sublineAy[6]][sublineAy[7]].LineFormat.GetFinalLine(),fg="white")
                        if idx == 3:
                            nowSubLinePar[sublineAy[9]][sublineAy[10]].LineFormat.DelMainLine(sublineAy[11])
                            nowSubLinePar[sublineAy[9]][sublineAy[10]].UILabel.config(text =nowSubLinePar[sublineAy[9]][sublineAy[10]].LineFormat.GetFinalLine(),fg="white")
    
    def DelMainLine( self, lineType ):
        if( lineType == 1):
            self.pos[0] = ''
            self.pos[2] = ''
        if( lineType == 2):
            self.pos[3] = '　　'
        if( lineType == 3):
            self.pos[4] = ''
            self.pos[5] = ''
        if( lineType == 4):
            self.pos[1] = '　　'
        if( lineType == 5):
            self.pos[0] = ''
            self.pos[2] = ''
            self.pos[3] = '　　'
        if( lineType == 6):
            self.pos[3] = '　　'
            self.pos[4] = ''
            self.pos[5] = ''
        if( lineType == 7):
            self.pos[4] = ''
            self.pos[5] = ''
            self.pos[1] = '　　'
        if( lineType == 8):
            self.pos[0] = ''
            self.pos[2] = ''
            self.pos[1] = '　　'
        if( lineType == 9):
            self.pos[4] = ''
            self.pos[5] = ''
            self.pos[0] = ''
            self.pos[2] = ''
        if( lineType == 10):
            self.pos[1] = '　　'
            self.pos[3] = '　　'
        if( lineType == 11):
            self.pos[4] = ''
            self.pos[5] = ''
            self.pos[0] = ''
            self.pos[2] = ''
            self.pos[1] = '　　'
            self.pos[3] = '　　'
    def CheckIndexInRange ( self, row, col, lineType):
        if( lineType == 1):
            return str( row - 1 > 0)
        if( lineType == 2):
            return str( col + 1 < CONSTGridCol)
        if( lineType == 3):
            return str( row + 1 < CONSTGridRow)
        if( lineType == 4):
            return str( col - 1 > 0)
        if( lineType == 5):
            return str( row - 1 > 0),str( col + 1 < CONSTGridCol)
        if( lineType == 6):
            return str( col + 1 < CONSTGridCol),str( row + 1 < CONSTGridRow)
        if( lineType == 7):
            return str( row + 1 < CONSTGridRow),str( col - 1 > 0)
        if( lineType == 8):
            return str( row - 1 > 0),str( col - 1 > 0)
        if( lineType == 9):
            return str( row - 1 > 0), str( row + 1 < CONSTGridRow)
        if( lineType == 10):
            return str( col + 1 < CONSTGridCol), str( col - 1 > 0)
        if( lineType == 11):
            return str( row - 1 > 0), str( col + 1 < CONSTGridCol), str( row + 1 < CONSTGridRow), str( col - 1 > 0)

    def GetSubIndex ( self, row, col, lineType):
        if( lineType == 1):
            return ( row - 1 ) , col , 3
        if( lineType == 2):
            return row, ( col + 1 ), 4
        if( lineType == 3):
            return ( row + 1 ) , col , 1
        if( lineType == 4):
            return row, ( col - 1 ), 2
        if( lineType == 5):
            return ( row - 1 ),col, 3, row, ( col + 1 ),4
        if( lineType == 6):
            return row, ( col + 1 ), 4, ( row + 1 ), col, 1
        if( lineType == 7):
            return ( row + 1 ),col, 1, row, ( col - 1 ),2
        if( lineType == 8):
            return ( row - 1 ),col, 3, row, ( col - 1 ), 2
        if( lineType == 9):
            return ( row - 1 ),col, 3, ( row + 1 ), col, 1
        if( lineType == 10):
            return row, ( col + 1 ), 4, row, ( col - 1 ), 2
        if( lineType == 11):
            return ( row - 1 ),col, 3, row,  ( col + 1 ), 4, ( row + 1 ), col, 1, row,  ( col - 1 ), 2

    def AddMainPos (self,lineType):
        if( lineType == 1):
            self.pos[0] = '│'
            self.pos[2] = '│'
        if( lineType == 2):
            self.pos[3] = '＿＿'
        if( lineType == 3):
            self.pos[4] = '│'
            self.pos[5] = '│'
        if( lineType == 4):
            self.pos[1] = '＿＿'
        if( lineType == 5):
            self.pos[0] = '│'
            self.pos[2] = '│'
            self.pos[3] = '＿＿'
        if( lineType == 6):
            self.pos[3] = '＿＿'
            self.pos[4] = '│'
            self.pos[5] = '│'
        if( lineType == 7):
            self.pos[4] = '│'
            self.pos[5] = '│'
            self.pos[1] = '＿＿'
        if( lineType == 8):
            self.pos[0] = '│'
            self.pos[2] = '│'
            self.pos[1] = '＿＿'
        if( lineType == 9):
            self.pos[0] = '│'
            self.pos[2] = '│'
            self.pos[4] = '│'
            self.pos[5] = '│'
        if( lineType == 10):
            self.pos[3] = '＿＿'
            self.pos[1] = '＿＿'
        if( lineType == 11):
            self.pos[0] = '│'
            self.pos[2] = '│'
            self.pos[4] = '│'
            self.pos[5] = '│'
            self.pos[3] = '＿＿'
            self.pos[1] = '＿＿'


class SingleMission(object):

    UILabel = None
    UIText = None
    posRow = 0
    posCol = 0
    Data = None
    LineFormat = None

    def __init__(self, row, col):
        self.Data = [ 0,0,0,"",0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.posCol = col
        self.posRow = row
        self.Data[0] = ((self.posCol * CONSTGridRow) + (self.posRow + 1))
        self.LineFormat = LineFormatData ()
        # super(SingleMission, self).__init__()

    def SetLineType(self, lineType):
        if(self.Data[MissionEditorIndex.boxType] == 0):
            self.Data[MissionEditorIndex.boxType] = 2
        if(self.Data[MissionEditorIndex.boxType] == 1):
            self.Data[MissionEditorIndex.boxType] = 3
        if(self.Data[MissionEditorIndex.lineType] != 0):
            self.LineFormat.DelLine(self.Data[MissionEditorIndex.lineType], self.posRow, self.posCol)
            self.UILabel.config(text =self.LineFormat.GetFinalLine(),fg="white")
        self.Data[MissionEditorIndex.lineType]  = lineType

        self.LineFormat.AddLine(lineType, self.posRow, self.posCol)
        self.UILabel.config(text =self.LineFormat.GetFinalLine(),fg="white")
        missionEditorVar[MissionEditorIndex.boxType].set(self.Data[MissionEditorIndex.boxType])
        missionEditorVar[MissionEditorIndex.lineType].set(self.Data[MissionEditorIndex.lineType])
        missionEditorDes[MissionEditorIndex.boxType]["text"] = self.Data[MissionEditorIndex.boxType]

    def CleanLineType(self):
        if(self.Data[MissionEditorIndex.boxType] == 2):
            self.Data[MissionEditorIndex.boxType] = 0
        if(self.Data[MissionEditorIndex.boxType] == 3):
            self.Data[MissionEditorIndex.boxType] = 1
        self.Data[MissionEditorIndex.lineType]  = 0
        self.LineFormat.DelLine(lineType, self.posRow, self.posCol)
        self.UILabel.config(text =self.LineFormat.GetFinalLine(),fg="white")
        missionEditorVar[MissionEditorIndex.boxType].set(self.Data[MissionEditorIndex.boxType])
        missionEditorVar[MissionEditorIndex.lineType].set(self.Data[MissionEditorIndex.lineType])
        missionEditorDes[MissionEditorIndex.boxType]["text"] = self.Data[MissionEditorIndex.boxType]

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
    missionList = allMissionBigDict[nowBigPageNumber][nowSmallPageNumber]
    for x in range(CONSTEditorNumber):
        if x < 3:
            missionEditorDes[x]['text'] = str(missionList[nowSelectRow][nowSelectCol].Data[x])
            missionEditorVar[x].set(missionList[nowSelectRow][nowSelectCol].Data[x])
        else:
            missionEditorVar[x].set(missionList[nowSelectRow][nowSelectCol].Data[x])
    SetLabelBKHighLight(row, col)


def ClickArrow(arrorLinetype):
    allMissionBigDict[nowBigPageNumber][nowSmallPageNumber][nowSelectRow][nowSelectCol].SetLineType(arrorLinetype)


def SetLabelBKHighLight(row, col):
    missionList = allMissionBigDict[nowBigPageNumber][nowSmallPageNumber]
    for i in range(len(missionList)):
        for j in range(len(missionList[i])):
            if(i == row and j == col):
                missionList[i][j].UILabel.config(bg="red")
            else:
                missionList[i][j].UILabel.config(bg=_from_rgb((32, 100, 140)))

# ======================
# 任務預覽
def GentGridPanel():
    global allMissionBigDict
    global nowBigPageNumber
    global nowSmallPageNumber
    global CONSTGridCol
    global CONSTGridRow
    tmpDict = allMissionBigDict[nowBigPageNumber][nowSmallPageNumber]
    # for data in tmpDict:
    print("nowBigPageNumber" + str(nowBigPageNumber))
    CheckNowColNumber()
    print("CONSTGridCol" + str(CONSTGridCol))
    for x in range(CONSTGridRow):
        if(tmpDict[x] == None):
            print("X is Empty")
            tmpDict[x] = []
        for y in range(CONSTGridCol):
            if(tmpDict[x][y]==None):
                print("tmpDict[{0}][{1}] is empty".format(x, y))
                tmpDict[x][y] = SingleMission(x, y)
            missionBK = tk.Label(mighty,
                                text="{0}".format(((y * CONSTGridRow) + (x + 1))),
                                 bg=_from_rgb((32, 100, 140)),
                                 width=10, height=3,
                                 borderwidth=2, relief="groove",
                                 font=bkfont
                                 )
            missionBK.grid(row=x, column=y)
            missionBK.bind("<Button-1>", lambda e, col=y,
                           row=x: ClickLabel(col, row))
            tmpDict[x][y].UILabel = missionBK
            if(math.floor(tmpDict[x][y].Data[MissionEditorIndex.boxType] % 2) == 1):
                tmpDict[x][y].UIText = tk.Label(mighty,
                                       text=tmpDict[x][y].Data[MissionEditorIndex.name],
                                       bg="white",
                                       width=2, height=1
                                       )
                tmpDict[x][y].UIText.grid(row=x, column=y)
    for x in range(CONSTGridRow):
        for y in range(CONSTGridCol):
            if(tmpDict[x][y].Data[MissionEditorIndex.boxType] > 1 ):
                tmpDict[x][y].SetLineType(tmpDict[x][y].Data[MissionEditorIndex.lineType])

# ======================

def CheckNowColNumber ():
    global nowBigPageNumber
    global CONSTGridCol
    if (nowBigPageNumber == 1):
        CONSTGridCol = 5
        print("Change5")
    else:
        CONSTGridCol = 7
        print("Change7")

missionEditor = ttk.LabelFrame(tab2, text=' 任務編輯 ')
missionEditor.grid(column=0, row=0)

for x in range(CONSTEditorNumber):
    missionEditorLabel.append(
        ttk.Label(missionEditor, text=missionEditorText[x], font=desfont)
        )
    missionEditorLabel[x].grid(column=0, row=x)
    if( x == 3 ):
        missionEditorVar.append(tk.StringVar())
    else:
        missionEditorVar.append(tk.IntVar())
    if x < 3:
        missionEditorDes.append(ttk.Label(
        missionEditor, text=missionEditorVar[x], font=desfont))
        missionEditorDes[x].grid(column=1, row=x)
    else:
        missionEditorDes.append(ttk.Entry(
     missionEditor, width=12, textvariable=missionEditorVar[x], font=desfont)
    )
        missionEditorDes[x].grid(column=1, row=x)


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
    width=3,
    command=lambda: ClickArrow(5)
)
upRightButton.grid(column=0, row=1)

downRightButton = ttk.Button(
    arrowButtonPanel,
    text='┌',
    width=3,
    command=lambda: ClickArrow(6)
)
downRightButton.grid(column=1, row=1)

downLeftButton = ttk.Button(
    arrowButtonPanel,
    text='┐',
    width=3,
    command=lambda: ClickArrow(7)
)
downLeftButton.grid(column=2, row=1)

upLeftButton = ttk.Button(
    arrowButtonPanel,
    text='┘',
    width=3,
    command=lambda: ClickArrow(8)
)
upLeftButton.grid(column=3, row=1)

verticalButton = ttk.Button(
    arrowButtonPanel,
    text='│',
    width=3,
    command=lambda: ClickArrow(9)
)
verticalButton.grid(column=0, row=2)

horizontalButton = ttk.Button(
    arrowButtonPanel,
    text='—',
    width=3,
    command=lambda: ClickArrow(10)
)
horizontalButton.grid(column=1, row=2)

crossButton = ttk.Button(
    arrowButtonPanel,
    text='┼',
    width=3,
    command=lambda: ClickArrow(11)
)
crossButton.grid(column=2, row=2)

confirmSetting = ttk.Button(
    arrowButtonPanel,
    text='確認',
    command=SaveSetting)
confirmSetting.grid(column=0, row=5)

missionBigTypeDropdown = None
missionSmaillTypeDropdown = None
def GenPageSelectPanel ():
    global missionBigType
    global missionBigTypeDropdown
    global missionSmaillTypeDropdown
    # ======================
    # 任務類型選擇
    missionBigType = tk.StringVar(win)
    missionBigType.set(bigMissionType[0])  # default value
    missionBigTypeLabel = ttk.Label(pageSettingTab, text="任務類型選擇", font=desfont)
    missionBigTypeLabel.grid(column=0, row=0)
    missionBigTypeDropdown = ttk.Combobox(pageSettingTab, textvariable=missionBigType, 
         state='readonly')
    missionBigTypeDropdown['value'] = bigMissionType
    missionBigTypeDropdown.bind("<<ComboboxSelected>>", ChangeBigType)
    missionBigTypeDropdown.config(width=12)
    missionBigTypeDropdown.grid(column=1, row=0, sticky="n")
    # ======================

    global missionSmaillType
    # ======================
    # 分頁頁碼選擇
    missionSmaillType = tk.IntVar(win)
    missionSmaillType.set(smallMissionType[0])  # default value
    missionSmaillTypeLabel = ttk.Label(pageSettingTab, text="分頁頁碼選擇", font=desfont)
    missionSmaillTypeLabel.grid(column=0, row=1)
    missionSmaillTypeDropdown = ttk.Combobox(pageSettingTab, textvariable=smallMissionType[0], 
                                    state='readonly')
    missionSmaillTypeDropdown['values'] = smallMissionType
    missionSmaillTypeDropdown.current(0)
    missionSmaillTypeDropdown.config(width=12)
    missionSmaillTypeDropdown.bind("<<ComboboxSelected>>", ChangeSmallType)
    missionSmaillTypeDropdown.grid(column=1, row=1, sticky="n")
    # ======================

def ChangeBigType(event):
    global missionBigTypeDropdown
    global mighty
    global nowBigPageNumber
    global nowSmallPageNumber
    global CONSTGridCol
    nowNumber = bigMissionType.index(missionBigTypeDropdown.get())
    nowBigPageNumber = nowNumber
    if(nowBigPageNumber == 0):
        CONSTGridCol = 5
    else:
        CONSTGridCol = 7
    if(len(everyTypeContaionsPage[nowBigPageNumber]) > 0):
        nowSmallPageNumber = everyTypeContaionsPage[nowBigPageNumber][0]
    else:
        nowSmallPageNumber = 0
    if(nowSmallPageNumber not in allMissionBigDict[nowBigPageNumber]):
        allMissionBigDict[nowBigPageNumber][nowSmallPageNumber]=[[None for x in range(CONSTGridCol)] for y in range(CONSTGridRow)] 
    mighty.destroy()
    mighty = ttk.LabelFrame(tab1, text=' 任務預覽 ')
    mighty.grid(column=0, row=0)
    GentGridPanel()

def ChangeSmallType(event):
    global missionSmaillTypeDropdown
    global mighty
    global nowBigPageNumber
    global nowSmallPageNumber
    nowNumber = int(missionSmaillTypeDropdown.get())
    nowSmallPageNumber = nowNumber - 1
    if(nowSmallPageNumber not in allMissionBigDict[nowBigPageNumber]):
        allMissionBigDict[nowBigPageNumber][nowSmallPageNumber]=[[None for x in range(CONSTGridCol)] for y in range(CONSTGridRow)] 
    mighty.destroy()
    mighty = ttk.LabelFrame(tab1, text=' 任務預覽 ')
    mighty.grid(column=0, row=0)
    GentGridPanel()
# ======================
# 新增小頁籤按鈕

nowPopupWindow = None
popTop = None
popLabel = None
popEntry = None
popButton = None

def popupWindow (master):
    global popTop
    global popEntry
    popTop=tk.Toplevel(master)
    popLabel=ttk.Label(popTop,text="要新增的頁籤")
    popLabel.pack()
    popEntry=ttk.Entry(popTop)
    popEntry.pack()
    popButton=ttk.Button(popTop,text='確認',command=cleanup)
    popButton.pack()

def cleanup():
    global popTop
    global popEntry
    reflashComboBox(popEntry.get())
    popTop.destroy()

def popup( ):
    global popTop
    nowPopupWindow=popupWindow(pageSettingTab)
    confirmSetting["state"] = "disabled" 
    pageSettingTab.wait_window(popTop)
    confirmSetting["state"] = "normal"

def entryValue():
    return nowPopupWindow.value

def reflashComboBox ( typein ):
    global missionSmaillTypeDropdown
    smallMissionType.append(typein)
    missionSmaillTypeDropdown['values'] = smallMissionType

confirmSetting = ttk.Button(
    pageSettingTab,
    text='新增小頁籤',
    command=popup)
confirmSetting.grid(column=0, row=2)
# ======================


def _quit():
    win.quit()
    win.destroy()
    exit()


def ImportData():
    global CONSTGridCol
    global CONSTGridRow
    global nowBigPageNumber
    nowBigPageNumber = 1
    open(fileNmae, 'a').close()
    global allMissionBigDict
    everyTypeContaionsPage[0].append(0)
    smallMissionType.append(everyTypeContaionsPage[0][0] + 1)
    allMissionBigDict[0][0] = [[None for x in range(CONSTGridCol)] for y in range(CONSTGridRow)] 
    with open(fileNmae, newline='',encoding='utf-8-sig', 
        errors='ignore') as inputFile:
        rows = csv.reader(inputFile)
        for index, row in enumerate(rows):
            big = int(row[3]) - 1
            small = int(row[5]) - 1
            if ( int(row[4]) == 1 ):
                CONSTGridCol = 5
            else:
                CONSTGridCol = 7
            if(len(row) < loadingDataLen and index == 0):
                break
            if int(small) not in everyTypeContaionsPage[int(big)]:
                everyTypeContaionsPage[big].append(small)
                allMissionBigDict[big][small] = [[None for x in range(CONSTGridCol)] for y in range(CONSTGridRow)]
            loadRow = math.floor((int(row[6]) % CONSTGridRow) - 1)
            loadCol = math.floor((int(row[6]) / CONSTGridRow) )
            allMissionBigDict[big][small][loadRow][loadCol] = SingleMission(
                loadRow,
                loadCol
                )
            tmpData = allMissionBigDict[big][small][loadRow][loadCol]

            tmpData.Data[MissionEditorIndex.name] = str(row[0])
            tmpData.Data[MissionEditorIndex.boxPos] = int(row[6])
            tmpData.Data[MissionEditorIndex.boxType] = int(row[7])
            tmpData.Data[MissionEditorIndex.lineType] = int(row[8])
            tmpData.Data[MissionEditorIndex.nameID] = int(row[9])
            tmpData.Data[MissionEditorIndex.moveSignObj] = int(row[10])
            tmpData.Data[MissionEditorIndex.staticSignObj] = int(row[11])
            tmpData.Data[MissionEditorIndex.missionNeedLevelObj] = int(row[12])
            tmpData.Data[MissionEditorIndex.missionSceneIDObj] = int(row[13])
            tmpData.Data[MissionEditorIndex.missionTeacherNameBeginObj] = str(row[14])
            tmpData.Data[MissionEditorIndex.missionTeacherXObj] = int(row[15])
            tmpData.Data[MissionEditorIndex.missionTeacherYObj] = int(row[16])
            tmpData.Data[MissionEditorIndex.missionSpecialItemObj] = str(row[17])
            tmpData.Data[MissionEditorIndex.missionSpecialDesObj] = str(row[18])
            print("{2}:{3} - {0},{1} Add Data".format(tmpData.posRow, tmpData.posCol,
                    big,small
                ))


def ExportData():
    global exportIDHead
    with open(fileNmae, "w", newline='',encoding='utf-8-sig', 
        errors='ignore') as outputFile:
        writer = csv.writer(outputFile)
        for Bkey, Bdata in enumerate(allMissionBigDict):
            if(Bkey == 0):
                nowPageStype = 1
            else:
                nowPageStype = 2
            for Skey, Sdata in Bdata.items():
                for i in range(len(Sdata)):
                    for j in range(len(Sdata[0])):
                        if Sdata[i][j].Data[MissionEditorIndex.boxType] != 0:                   
                            writer.writerow([
                                Sdata[i][j].Data[MissionEditorIndex.name],
                                1,
                                exportIDHead,
                                Bkey + 1,
                                nowPageStype,
                                Skey + 1,
                                Sdata[i][j].Data[MissionEditorIndex.boxPos],
                                Sdata[i][j].Data[MissionEditorIndex.boxType],
                                Sdata[i][j].Data[MissionEditorIndex.lineType],
                                Sdata[i][j].Data[MissionEditorIndex.nameID],
                                Sdata[i][j].Data[MissionEditorIndex.moveSignObj],
                                Sdata[i][j].Data[MissionEditorIndex.staticSignObj],
                                Sdata[i][j].Data[MissionEditorIndex.missionNeedLevelObj],
                                Sdata[i][j].Data[MissionEditorIndex.missionSceneIDObj],
                                Sdata[i][j].Data[MissionEditorIndex.missionTeacherNameBeginObj],
                                Sdata[i][j].Data[MissionEditorIndex.missionTeacherXObj],
                                Sdata[i][j].Data[MissionEditorIndex.missionTeacherYObj],
                                Sdata[i][j].Data[MissionEditorIndex.missionSpecialItemObj],
                                Sdata[i][j].Data[MissionEditorIndex.missionSpecialDesObj]
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
GenPageSelectPanel()
# ======================


# ======================
# Start GUI
# ======================
win.mainloop()
