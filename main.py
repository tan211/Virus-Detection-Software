from glob import glob
from tkinter import*
from tkinter import filedialog
import psutil
import pystray
import PIL.Image
from screeninfo import get_monitors
import os
import random
import engine
import time
import subprocess


window = Tk()

window.title("AntiVirus-4T")
window.geometry("1200x850")
window.minsize("1200","850")
window.maxsize("1200","850")

winFrame = Frame(window,width="1200",height="850",bg="gray17")
winFrame.pack()
winFrame.pack_propagate(0)


os.startfile("real-time-protection_setting.bat")

#--------------------Tkinter Base Setup End ------------------# 

def HomeFrame():


    #--------------------Global Var --------------------#  
    global winFrame
    

    #--------------------Global Var End -----------------# 

    winFrame.destroy()



    #--------------------Main Frame ---------------------# 

    winFrame = Frame(window,width="1200",height="850",bg="gray17")
    winFrame.pack()
    winFrame.pack_propagate(0)

    #--------------------Main Frame End ------------------# 

    #--------------------Footer Frame --------------------#

    #--------------------Footer Frame End ----------------#

    #--------------------Logo Frame start --------------#

    #--------------------Logo Frame End ----------------#

    #--------------------Home Button --------------------#
    global homeButtonImg

    homeButtonImg = PhotoImage(file="res\\Home Frame\\Current\\Home.png")


    homeButton = Label(winFrame,image=homeButtonImg,bg="gray17",cursor="hand2")
    homeButton.place(x=155,y=570)


    #--------------------Home Button End------------------#

    #--------------------Scan Button ---------------------#

    scanButtonImg = PhotoImage(file="res\\Scan Frame\\Non-Hoved\\Scan.png")
    hovScanButtonImg = PhotoImage(file="res\\Scan Frame\\Hoved\\Scan.png")
    def ScanButtonEnterFrame(event):
        scanButton.config(image=hovScanButtonImg)

    def ScanButtonLeaveFrame(event):
        scanButton.config(image=scanButtonImg)
    
    def ScanButtonCall(event):
        ScanFrame()


    scanButton = Label(winFrame,image=scanButtonImg,bg="gray17",cursor="hand2")
    scanButton.place(x=335,y=570)

    scanButton.bind('<Enter>',ScanButtonEnterFrame)
    scanButton.bind('<Leave>',ScanButtonLeaveFrame)
    scanButton.bind('<Button-1>',ScanButtonCall)

    # #--------------------Scan Button End------------------#

    # #--------------------System Button -------------------#

    systemButtonImg = PhotoImage(file="res\\System Frame\\Non-Hoved\\System.png")
    hovsystemButtonImg = PhotoImage(file="res\\System Frame\\Hoved\\System.png")

    def SystemButtonEnterFrame(event):
        systemButton.config(image=hovsystemButtonImg)

    def SystemButtonLeaveFrame(event):
        systemButton.config(image=systemButtonImg)
    def SystemButtonCall(event):
        SystemFrame()


    systemButton = Label(winFrame,image=systemButtonImg,bg="gray17",cursor="hand2")
    systemButton.place(x=515,y=570)

    systemButton.bind('<Enter>',SystemButtonEnterFrame)
    systemButton.bind('<Leave>',SystemButtonLeaveFrame)
    systemButton.bind('<Button-1>',SystemButtonCall)

    # #--------------------System Button End ---------------#

    #--------------------Web Button -----------------#

    webButtonImg = PhotoImage(file="res\\Web Frame\\Non-Hoved\\Web.png")
    hovWebButtonImg = PhotoImage(file="res\\Web Frame\\Hoved\\Web.png")

    def WebButtonEnterFrame(event):
        webButton.config(image=hovWebButtonImg)

    def WebButtonLeaveFrame(event):
        webButton.config(image=webButtonImg)


    webButton = Label(winFrame,image=webButtonImg,bg="gray17",cursor="hand2")
    webButton.place(x=695,y=570)

    webButton.bind('<Enter>',WebButtonEnterFrame)
    webButton.bind('<Leave>',WebButtonLeaveFrame)

    #--------------------Web Button End -------------#

    # #--------------------Tools Button -----------------#

    toolsButtonImg = PhotoImage(file="res\\Tools Frame\\Non-Hoved\\Tools.png")
    hovToolsButtonImg = PhotoImage(file="res\\Tools Frame\\Hoved\\Tools.png")

    def ToolsButtonEnterFrame(event):
        toolsButton.config(image=hovToolsButtonImg)

    def ToolsButtonLeaveFrame(event):
        toolsButton.config(image=toolsButtonImg)



    toolsButton = Label(winFrame,image=toolsButtonImg,bg="gray17",cursor="hand2")
    toolsButton.place(x=875,y=570)

    toolsButton.bind('<Enter>',ToolsButtonEnterFrame)
    toolsButton.bind('<Leave>',ToolsButtonLeaveFrame)

    # #--------------------Tools Button End -------------#


    # #--------------------Animation --- ----------------#

    global robotImg
    robotImg = PhotoImage(file='res\\Home Frame\\Animation\\robotlink.png')

    robotAnimation = Label(winFrame,image=robotImg,bg="gray17")
    robotAnimation.place(x=475,y=150)

    global ani
    ani = 0
    def RobotAnimation():
        global ani

        if ani == 4:
            robotAnimation.place_configure(y=153)
            ani = 0
        
        elif ani == 2:
            robotAnimation.place_configure(y=150)


        ani += 1

        robotAnimation.after(200,RobotAnimation)

    RobotAnimation()

    # #--------------------Animation End ----------------#

    # #--------------------Sub-Frame --- ----------------#

    # #--------------------Proction-Frame --- ----------------#

    global protectionOn0Img

    protectionOn0Img = PhotoImage(file="res\\Home Frame\\Non-Hoved\\protection on0.png").subsample(2,2)
    protectionOn0ImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\protection on.png").subsample(2,2)

    def ProtectionEnter(event):
        protectionOn0.config(image=protectionOn0ImgHov)
    
    def ProtectionLeave(event):
        protectionOn0.config(image = protectionOn0Img)

    protectionOn0 = Label(winFrame, image=protectionOn0Img, bg="gray17", cursor="hand2")
    protectionOn0.place(x=180,y=160)
    protectionOn0.bind('<Enter>',ProtectionEnter)
    protectionOn0.bind('<Leave>',ProtectionLeave)

    # #--------------------Proction-Frame End ----------------#




    # #--------------------Web-Frame --- ----------------#

    global webShieldImg

    webShieldImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\web sh.png").subsample(2,2)
    webShieldImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\web shield.png").subsample(2,2)

    def WebShieldEnter(event):
        webShield.config(image=webShieldImgHov)
    
    def WebShieldLeave(event):
        webShield.config(image=webShieldImg)

    webShield = Label(winFrame, image=webShieldImg, bg="gray17", cursor="hand2")
    webShield.place(x=810,y=160)
    webShield.bind('<Enter>',WebShieldEnter)
    webShield.bind('<Leave>',WebShieldLeave)


    # #--------------------Web-Frame End ----------------#

    # #--------------------FireWall-Frame --- ----------------#

    global fireWallOnImg

    fireWallOnImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\fire wall on.png").subsample(2,2)
    fireWallOnImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\firewall.png").subsample(2,2)

    def FireWallEnter(event):
        fireWallOn.config(image=fireWallOnImgHov)

    def FireWallLeave(event):
        fireWallOn.config(image=fireWallOnImg)

    fireWallOn = Label(winFrame, image=fireWallOnImg, bg="gray17", cursor="hand2")
    fireWallOn.place(x=160,y=220)

    fireWallOn.bind('<Enter>',FireWallEnter)
    fireWallOn.bind('<Leave>',FireWallLeave)
    

    # #--------------------FireWall-Frame End ----------------#


    # #--------------------FullScan-Frame --- ----------------#

    global fullScanImg

    fullScanImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\full scan.png").subsample(2,2)
    fullScanImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\full scan.png").subsample(2,2)

    def FullScanEnter(e):
        fullScan.config(image=fullScanImgHov)
    
    def FullScanLeave(e):
        fullScan.config(image=fullScanImg)

    fullScan = Label(winFrame, image=fullScanImg, bg="gray17", cursor="hand2")
    fullScan.place(x=830,y=220)
    fullScan.bind('<Enter>',FullScanEnter)
    fullScan.bind('<Leave>',FullScanLeave)

    # #--------------------FullScan-Frame End ----------------#
    

    # #--------------------QuickScan-Frame --- ----------------#

    global quickScanImg

    quickScanImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\quick scan.png").subsample(2,2)
    quickScanImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\Quck Scan.png").subsample(2,2)

    def QuickScanEnter(e):
        quickScan.config(image=quickScanImgHov)

    def QuickScanLeave(e):
        quickScan.config(image=quickScanImg)


    quickScan = Label(winFrame, image=quickScanImg, bg="gray17", cursor="hand2")
    quickScan.place(x=150,y=280)
    quickScan.bind('<Enter>',QuickScanEnter)
    quickScan.bind('<Leave>',QuickScanLeave)

    # #--------------------QuickScan-Frame End ----------------#


    # #--------------------RamBooster-Frame --- ----------------#

    global ramBoosterImg

    ramBoosterImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\ram boost.png").subsample(2,2)
    ramBoosterImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\ram boost.png").subsample(2,2)

    def RamBoosterEnter(e):
        ramBooster.config(image=ramBoosterImgHov)

    def RamBoosterLeave(e):
        ramBooster.config(image=ramBoosterImg)
        
    def RamBootsterCall(e):
        ramBoosterFunc()

    ramBooster = Label(winFrame, image=ramBoosterImg, bg="gray17", cursor="hand2")
    ramBooster.place(x=840,y=280)
    ramBooster.bind('<Enter>',RamBoosterEnter)
    ramBooster.bind('<Leave>',RamBoosterLeave)
    ramBooster.bind('<Button-1>',RamBootsterCall)


    # #--------------------RamBooster-Frame End ----------------#


    # #--------------------Smart Scan-Frame --- ----------------#

    global smartScanLblImg

    smartScanLblImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\smart scan.png").subsample(2,2)
    smartScanLblImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\smart scan.png").subsample(2,2)

    def smartScanLblEnter(e):
        smartScanLbl.config(image=smartScanLblImgHov)
    
    def smartScanLblLeave(e):
        smartScanLbl.config(image=smartScanLblImg)

    smartScanLbl = Label(winFrame, image=smartScanLblImg, bg="gray17", cursor="hand2")
    smartScanLbl.place(x=160,y=340)
    smartScanLbl.bind('<Enter>',smartScanLblEnter)
    smartScanLbl.bind('<Leave>',smartScanLblLeave)


    # #--------------------Smart Scan-Frame End ----------------#


    # #--------------------Deep Scan-Frame --- ----------------#

    global deepScanImg

    deepScanImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\deep scan.png").subsample(2,2)
    deepScanImgHov = PhotoImage(file='res\\Home Frame\\Hoved\\deep scan.png').subsample(2,2)

    def DeepScanEnter(e):
        deepScan.config(image=deepScanImgHov)

    def DeepScanLeave(e):
        deepScan.config(image=deepScanImg)

    deepScan = Label(winFrame, image=deepScanImg, bg="gray17", cursor="hand2")
    deepScan.place(x=830,y=340)
    deepScan.bind("<Enter>",DeepScanEnter)
    deepScan.bind("<Leave>",DeepScanLeave)

    # #--------------------Deep Scan-Frame End ----------------#



    # #--------------------Help-Frame --- ----------------#

    global helpNsupportImg

    helpNsupportImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\help & support.png").subsample(2,2)
    helpNsupportImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\help.png").subsample(2,2)

    def HelpEnter(e):
        helpNsupport.config(image=helpNsupportImgHov)
    
    def HelpLeave(e):
        helpNsupport.config(image=helpNsupportImg)

    helpNsupport = Label(winFrame, image=helpNsupportImg, bg="gray17", cursor="hand2")
    helpNsupport.place(x=180,y=400)
    helpNsupport.bind("<Enter>",HelpEnter)
    helpNsupport.bind("<Leave>",HelpLeave)

    # #--------------------Help-Frame End ----------------#


    # #--------------------Driver Update-Frame --- ----------------#

    global driverUpdateImg

    driverUpdateImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\driver update.png").subsample(2,2)
    driverUpdateImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\driver update.png").subsample(2,2)

    def DriverUpdateEnter(e):
        driverUpdate.config(image=driverUpdateImgHov)

    def DriverUpdateLeave(e):
        driverUpdate.config(image=driverUpdateImg)

    driverUpdate = Label(winFrame, image=driverUpdateImg, bg="gray17", cursor="hand2")
    driverUpdate.place(x=810,y=400)
    driverUpdate.bind("<Enter>",DriverUpdateEnter)
    driverUpdate.bind("<Leave>",DriverUpdateLeave)

    # #--------------------Driver Update-Frame End ----------------#

    # #--------------------Sub-Frame End ----------------#

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################


def ScanFrame():

    #--------------------Global Var --------------------#  
    global winFrame
    

    #--------------------Global Var End -----------------# 

    winFrame.destroy()



    #--------------------Main Frame ---------------------# 

    winFrame = Frame(window,width="1200",height="850",bg="gray17")
    winFrame.pack()
    winFrame.pack_propagate(0)

    #--------------------Main Frame End ------------------# 

    #--------------------Footer Frame --------------------#

    #--------------------Footer Frame End ----------------#

    #--------------------Logo Frame start --------------#
    #--------------------Logo Frame End ----------------#


    #--------------------Quick_Scan --------------------#

    global quickScanButton_1
    global quickScanButton_1_Hoved

    quickScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\Quick Scan.png').subsample(2,2)
    quickScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\Quick Scan.png').subsample(2,2)

    def quickScanButton_1_Enter(e):
        quickScanButton_1place.config(image=quickScanButton_1_Hoved)
    
    def quickScanButton_1_Leave(e):
        quickScanButton_1place.config(image=quickScanButton_1)

    quickScanButton_1place = Label(winFrame,image=quickScanButton_1,bg='gray17', cursor="hand2")
    quickScanButton_1place.place(x=530,y=100)

    quickScanButton_1place.bind('<Enter>',quickScanButton_1_Enter)
    quickScanButton_1place.bind('<Leave>',quickScanButton_1_Leave)

    #--------------------Quick_Scan End ----------------#

    #--------------------Smart_Scan --------------------#

    global smartScanButton_1
    global smartScanButton_1_Hoved

    smartScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\smart Scan.png').subsample(2,2)
    smartScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\smart Scan.png').subsample(2,2)

    def smartScanButton_1_Enter(e):
        smartScanButton_1place.config(image=smartScanButton_1_Hoved)
    
    def smartScanButton_1_Leave(e):
        smartScanButton_1place.config(image=smartScanButton_1)

    smartScanButton_1place = Label(winFrame,image=smartScanButton_1,bg='gray17', cursor="hand2")
    smartScanButton_1place.place(x=510,y=170)

    smartScanButton_1place.bind('<Enter>',smartScanButton_1_Enter)
    smartScanButton_1place.bind('<Leave>',smartScanButton_1_Leave)

    #--------------------Smart_Scan End ----------------#

    #--------------------Full_Scan --------------------#

    global fullScanButton_1
    global fullScanButton_1_Hoved

    fullScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\Full Scan.png').subsample(2,2)
    fullScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\Full Scan.png').subsample(2,2)

    def fullScanButton_1_Enter(e):
        fullScanButton_1place.config(image=fullScanButton_1_Hoved)
    
    def fullScanButton_1_Leave(e):
        fullScanButton_1place.config(image=fullScanButton_1)
    def ShowDataButtonCallFullScan(e):
        showData()

    fullScanButton_1place = Label(winFrame,image=fullScanButton_1,bg='gray17', cursor="hand2")
    fullScanButton_1place.place(x=510,y=240)

    fullScanButton_1place.bind('<Enter>',fullScanButton_1_Enter)
    fullScanButton_1place.bind('<Leave>',fullScanButton_1_Leave)
    fullScanButton_1place.bind('<Button-1>',ShowDataButtonCallFullScan)

    #--------------------Full_Scan End ----------------#

    #--------------------Deep_Scan --------------------#

    global deepScanButton_1
    global deepScanButton_1_Hoved

    deepScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\Deep Scan.png').subsample(2,2)
    deepScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\Deep Scan.png').subsample(2,2)

    def deepScanButton_1_Enter(e):
        deepScanButton_1place.config(image=deepScanButton_1_Hoved)
    
    def deepScanButton_1_Leave(e):
        deepScanButton_1place.config(image=deepScanButton_1)
    def ShowDataButtonCall(e):
        showData()

    deepScanButton_1place = Label(winFrame,image=deepScanButton_1,bg='gray17', cursor="hand2")
    deepScanButton_1place.place(x=510,y=310)
    

    deepScanButton_1place.bind('<Enter>',deepScanButton_1_Enter)
    deepScanButton_1place.bind('<Leave>',deepScanButton_1_Leave)
    deepScanButton_1place.bind('<Button-1>',ShowDataButtonCall)


    #--------------------Deep_Scan End ----------------#

    #--------------------Custom_Scan --------------------#

    global CustomScanButton_1
    global CustomScanButton_1_Hoved

    CustomScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\Custom Scan.png').subsample(2,2)
    CustomScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\Custom Scan.png').subsample(2,2)

    def CustomScanButton_1_Enter(e):
        CustomScanButton_1place.config(image=CustomScanButton_1_Hoved)
    
    def CustomScanButton_1_Leave(e):
        CustomScanButton_1place.config(image=CustomScanButton_1)
        
    def ShowDataButtonCallCustomScan(e):
        customScanFunc()

    CustomScanButton_1place = Label(winFrame,image=CustomScanButton_1,bg='gray17', cursor="hand2")
    CustomScanButton_1place.place(x=530,y=380)

    CustomScanButton_1place.bind('<Enter>',CustomScanButton_1_Enter)
    CustomScanButton_1place.bind('<Leave>',CustomScanButton_1_Leave)
    CustomScanButton_1place.bind('<Button-1>',ShowDataButtonCallCustomScan)

    #--------------------Custom_Scan End ----------------#

    #--------------------Main Logo ----------------------#

    global scanFrameMainLogo
    global scanFrameMainLogoHoved
    scanFrameMainLogo = PhotoImage(file='res\\Scan Frame\\main logo.png')
    scanFrameMainLogoHoved = PhotoImage(file='res\\Scan Frame\\main logo hoved.png')

    def scanFrameMainLogoEnter(event):
        scanFrameMainLogoPlace.config(image=scanFrameMainLogoHoved)
    
    def scanFrameMainLogoLeave(event):
        scanFrameMainLogoPlace.config(image=scanFrameMainLogo)

    
    scanFrameMainLogoPlace = Label(winFrame,image=scanFrameMainLogo,bg='gray17', cursor="hand2")
    scanFrameMainLogoPlace.place(x=772,y=100)

    scanFrameMainLogoPlace.bind('<Enter>',scanFrameMainLogoEnter)
    scanFrameMainLogoPlace.bind('<Leave>',scanFrameMainLogoLeave)

    #--------------------Main Logo End-------------------#

    #--------------------Home Button --------------------#

    homeButtonImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\Home.png")
    hovHomeButtonImg = PhotoImage(file="res\\Home Frame\\Hoved\\Home.png")

    def HomeButtonEnterFrame(event):
        homeButton.config(image=hovHomeButtonImg)

    def HomeButtonLeaveFrame(event):
        homeButton.config(image=homeButtonImg)
    
    def HomeButtonCall(event):
        HomeFrame()

    homeButton = Label(winFrame,image=homeButtonImg,bg="gray17",cursor="hand2")
    homeButton.place(x=155,y=570)

    homeButton.bind('<Enter>',HomeButtonEnterFrame)
    homeButton.bind('<Leave>',HomeButtonLeaveFrame)
    homeButton.bind('<Button-1>',HomeButtonCall)


    #--------------------Home Button End------------------#

    #--------------------Scan Button ---------------------#

    global scanButtonImg

    scanButtonImg = PhotoImage(file="res\\Scan Frame\\Current\\Scan.png")


    scanButton = Label(winFrame,image=scanButtonImg,bg="gray17",cursor="hand2")
    scanButton.place(x=335,y=570)

    # #--------------------Scan Button End------------------#

    # #--------------------System Button -------------------#

    systemButtonImg = PhotoImage(file="res\\System Frame\\Non-Hoved\\System.png")
    hovsystemButtonImg = PhotoImage(file="res\\System Frame\\Hoved\\System.png")

    def SystemButtonEnterFrame(event):
        systemButton.config(image=hovsystemButtonImg)

    def SystemButtonLeaveFrame(event):
        systemButton.config(image=systemButtonImg)
        
    def SystemButtonCall(event):
        SystemFrame()

    systemButton = Label(winFrame,image=systemButtonImg,bg="gray17",cursor="hand2")
    systemButton.place(x=515,y=570)

    systemButton.bind('<Enter>',SystemButtonEnterFrame)
    systemButton.bind('<Leave>',SystemButtonLeaveFrame)
    systemButton.bind('<Button-1>',SystemButtonCall)


    # #--------------------System Button End ---------------#

    #--------------------Web Button -----------------#

    webButtonImg = PhotoImage(file="res\\Web Frame\\Non-Hoved\\Web.png")
    hovWebButtonImg = PhotoImage(file="res\\Web Frame\\Hoved\\Web.png")

    def WebButtonEnterFrame(event):
        webButton.config(image=hovWebButtonImg)

    def WebButtonLeaveFrame(event):
        webButton.config(image=webButtonImg)


    webButton = Label(winFrame,image=webButtonImg,bg="gray17",cursor="hand2")
    webButton.place(x=695,y=570)

    webButton.bind('<Enter>',WebButtonEnterFrame)
    webButton.bind('<Leave>',WebButtonLeaveFrame)

    #--------------------Web Button End -------------#

    # #--------------------Tools Button -----------------#

    toolsButtonImg = PhotoImage(file="res\\Tools Frame\\Non-Hoved\\Tools.png")
    hovToolsButtonImg = PhotoImage(file="res\\Tools Frame\\Hoved\\Tools.png")

    def ToolsButtonEnterFrame(event):
        toolsButton.config(image=hovToolsButtonImg)

    def ToolsButtonLeaveFrame(event):
        toolsButton.config(image=toolsButtonImg)


    toolsButton = Label(winFrame,image=toolsButtonImg,bg="gray17",cursor="hand2")
    toolsButton.place(x=875,y=570)

    toolsButton.bind('<Enter>',ToolsButtonEnterFrame)
    toolsButton.bind('<Leave>',ToolsButtonLeaveFrame)

    # #--------------------Tools Button End -------------#

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################



def SystemFrame():

    #--------------------Global Var --------------------#  
    global winFrame
    

    #--------------------Global Var End -----------------# 

    winFrame.destroy()



    #--------------------Main Frame ---------------------# 

    winFrame = Frame(window,width="1200",height="850",bg="gray17")
    winFrame.pack()
    winFrame.pack_propagate(0)

    #--------------------Main Frame End ------------------# 

    #--------------------Footer Frame --------------------#

    global footerImg
    footerImg = PhotoImage(file='res\\footer.png')

    footerLabel = Label(winFrame,image=footerImg,bg="gray17")
    footerLabel.place(x=310,y=773)

    #--------------------Footer Frame End ----------------#

    #--------------------Logo Frame start --------------#

    global logoLabelImg
    logoLabelImg = PhotoImage(file='res\\Logo\\logo.png')
    logoLabel = Label(winFrame,image=logoLabelImg,bg='gray17')
    logoLabel.place(x=10,y=0)

    global nameLabelImg
    nameLabelImg = PhotoImage(file='res\\Logo\\b logo.png').subsample(2,2)
    nameLabel = Label(winFrame,image=nameLabelImg,bg='gray17')
    nameLabel.place(x=90,y=20)
    #--------------------Logo Frame End ----------------#

    #--------------------Protection --------------------#

    global protectionButton_1
    global protectionButton_1_Hoved

    protectionButton_1 = PhotoImage(file='res\\System Frame\\Non-Hoved\\protection.png').subsample(2,2)
    protectionButton_1_Hoved = PhotoImage(file='res\\System Frame\\Hoved\\protection.png').subsample(2,2)

    def protectionButton_1_Enter(e):
        protectionButton_1place.config(image=protectionButton_1_Hoved)
    
    def protectionButton_1_Leave(e):
        protectionButton_1place.config(image=protectionButton_1)

    protectionButton_1place = Label(winFrame,image=protectionButton_1,bg='gray17', cursor="hand2")
    protectionButton_1place.place(x=530,y=100)

    protectionButton_1place.bind('<Enter>',protectionButton_1_Enter)
    protectionButton_1place.bind('<Leave>',protectionButton_1_Leave)

    #--------------------Protection End ----------------#   

    #--------------------Firewall --------------------#

    global firewallButton_1
    global firewallButton_1_Hoved

    firewallButton_1 = PhotoImage(file='res\\System Frame\\Non-Hoved\\firewall.png').subsample(2,2)
    firewallButton_1_Hoved = PhotoImage(file='res\\System Frame\\Hoved\\firewall.png').subsample(2,2)

    def firewallButton_1_Enter(e):
        firewallButton_1place.config(image=firewallButton_1_Hoved)
    
    def firewallButton_1_Leave(e):
        firewallButton_1place.config(image=firewallButton_1)

    firewallButton_1place = Label(winFrame,image=firewallButton_1,bg='gray17', cursor="hand2")
    firewallButton_1place.place(x=510,y=170)

    firewallButton_1place.bind('<Enter>',firewallButton_1_Enter)
    firewallButton_1place.bind('<Leave>',firewallButton_1_Leave)

    #--------------------Firewall End ----------------#  

    #--------------------System Health --------------------#

    global systemHealthButton_1
    global systemHealthButton_1_Hoved

    systemHealthButton_1 = PhotoImage(file='res\\System Frame\\Non-Hoved\\system health.png').subsample(2,2)
    systemHealthButton_1_Hoved = PhotoImage(file='res\\System Frame\\Hoved\\system health.png').subsample(2,2)

    def systemHealthButton_1_Enter(e):
        systemHealthButton_1place.config(image=systemHealthButton_1_Hoved)
    
    def systemHealthButton_1_Leave(e):
        systemHealthButton_1place.config(image=systemHealthButton_1)
        
    def SystemHeathButtonCall(e):
        junkFileRemoverFunc()

    systemHealthButton_1place = Label(winFrame,image=systemHealthButton_1,bg='gray17', cursor="hand2")
    systemHealthButton_1place.place(x=510,y=240)

    systemHealthButton_1place.bind('<Enter>',systemHealthButton_1_Enter)
    systemHealthButton_1place.bind('<Leave>',systemHealthButton_1_Leave)
    systemHealthButton_1place.bind('<Button-1>',SystemHeathButtonCall)


    #--------------------System Health End ----------------#  

    #--------------------System Report --------------------#

    global systemReportButton_1
    global systemReportButton_1_Hoved

    systemReportButton_1 = PhotoImage(file='res\\System Frame\\Non-Hoved\\system report.png').subsample(2,2)
    systemReportButton_1_Hoved = PhotoImage(file='res\\System Frame\\Hoved\\system report.png').subsample(2,2)

    def systemReportButton_1_Enter(e):
        systemReportButton_1place.config(image=systemReportButton_1_Hoved)
    
    def systemReportButton_1_Leave(e):
        systemReportButton_1place.config(image=systemReportButton_1)

    systemReportButton_1place = Label(winFrame,image=systemReportButton_1,bg='gray17', cursor="hand2")
    systemReportButton_1place.place(x=530,y=310)

    systemReportButton_1place.bind('<Enter>',systemReportButton_1_Enter)
    systemReportButton_1place.bind('<Leave>',systemReportButton_1_Leave)

    #--------------------System Report End ----------------#  


    #--------------------Main Logo ----------------------#

    global systemFrameMainLogo
    global systemFrameMainLogoHoved
    systemFrameMainLogo = PhotoImage(file='res\\System Frame\\main frame logo.png')
    systemFrameMainLogoHoved = PhotoImage(file='res\\System Frame\\main frame logo hoved.png')

    def systemFrameMainLogoEnter(event):
        systemFrameMainLogoPlace.config(image=systemFrameMainLogoHoved)
    
    def systemFrameMainLogoLeave(event):
        systemFrameMainLogoPlace.config(image=systemFrameMainLogo)

    
    systemFrameMainLogo = PhotoImage(file='res\\System Frame\\main frame logo.png')
    systemFrameMainLogoPlace = Label(winFrame,image=systemFrameMainLogo,bg='gray17')
    systemFrameMainLogoPlace.place(x=772,y=100)

    systemFrameMainLogoPlace.bind('<Enter>',systemFrameMainLogoEnter)
    systemFrameMainLogoPlace.bind('<Leave>',systemFrameMainLogoLeave)


    #--------------------Main Logo End-------------------#

    #--------------------Home Button --------------------#

    homeButtonImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\Home.png")
    hovHomeButtonImg = PhotoImage(file="res\\Home Frame\\Hoved\\Home.png")

    def HomeButtonEnterFrame(event):
        homeButton.config(image=hovHomeButtonImg)

    def HomeButtonLeaveFrame(event):
        homeButton.config(image=homeButtonImg)
    
    def HomeButtonCall(event):
        HomeFrame()

    homeButton = Label(winFrame,image=homeButtonImg,bg="gray17",cursor="hand2")
    homeButton.place(x=155,y=570)

    homeButton.bind('<Enter>',HomeButtonEnterFrame)
    homeButton.bind('<Leave>',HomeButtonLeaveFrame)
    homeButton.bind('<Button-1>',HomeButtonCall)


    #--------------------Home Button End------------------#

    #--------------------Scan Button ---------------------#

    scanButtonImg = PhotoImage(file="res\\Scan Frame\\Non-Hoved\\Scan.png")
    hovScanButtonImg = PhotoImage(file="res\\Scan Frame\\Hoved\\Scan.png")
    def ScanButtonEnterFrame(event):
        scanButton.config(image=hovScanButtonImg)

    def ScanButtonLeaveFrame(event):
        scanButton.config(image=scanButtonImg)
    
    def ScanButtonCall(event):
        ScanFrame()


    scanButton = Label(winFrame,image=scanButtonImg,bg="gray17",cursor="hand2")
    scanButton.place(x=335,y=570)

    scanButton.bind('<Enter>',ScanButtonEnterFrame)
    scanButton.bind('<Leave>',ScanButtonLeaveFrame)
    scanButton.bind('<Button-1>',ScanButtonCall)

    # #--------------------Scan Button End------------------#

    # #--------------------System Button -------------------#

    global systemButtonImg

    systemButtonImg = PhotoImage(file="res\\System Frame\\Current\\System.png")


    systemButton = Label(winFrame,image=systemButtonImg,bg="gray17",cursor="hand2")
    systemButton.place(x=515,y=570)

    # #--------------------System Button End ---------------#

    #--------------------Web Button -----------------#

    webButtonImg = PhotoImage(file="res\\Web Frame\\Non-Hoved\\Web.png")
    hovWebButtonImg = PhotoImage(file="res\\Web Frame\\Hoved\\Web.png")

    def WebButtonEnterFrame(event):
        webButton.config(image=hovWebButtonImg)

    def WebButtonLeaveFrame(event):
        webButton.config(image=webButtonImg)


    webButton = Label(winFrame,image=webButtonImg,bg="gray17",cursor="hand2")
    webButton.place(x=695,y=570)

    webButton.bind('<Enter>',WebButtonEnterFrame)
    webButton.bind('<Leave>',WebButtonLeaveFrame)

    #--------------------Web Button End -------------#

    # #--------------------Tools Button -----------------#

    toolsButtonImg = PhotoImage(file="res\\Tools Frame\\Non-Hoved\\Tools.png")
    hovToolsButtonImg = PhotoImage(file="res\\Tools Frame\\Hoved\\Tools.png")

    def ToolsButtonEnterFrame(event):
        toolsButton.config(image=hovToolsButtonImg)

    def ToolsButtonLeaveFrame(event):
        toolsButton.config(image=toolsButtonImg)


    toolsButton = Label(winFrame,image=toolsButtonImg,bg="gray17",cursor="hand2")
    toolsButton.place(x=875,y=570)

    toolsButton.bind('<Enter>',ToolsButtonEnterFrame)
    toolsButton.bind('<Leave>',ToolsButtonLeaveFrame)

    # #--------------------Tools Button End -------------#


##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################



def showData():    
    
    global winFrame
    global backButtonImg
    global prog0
    global prog1
    global prog2
    global prog3
    global prog4
    global prog5
    global io
    global ranHashShower
    global samB
    global rMVirus
    
    with open("virusHash.unibit", "r") as nr:
        samB = nr.readlines()
        nr.close()

    winFrame.destroy()

    winFrame = Frame(window, width=1100, height = 600)
    winFrame.pack()
    winFrame.pack_propagate(0)

    io = 0

    def removeVirusBtn():
        try : 
            with open("switch_virusscanner.bb","r") as bb:
                io = list(bb.readlines())
                bb.close()
        except:pass

        try:
            for i in io:
                i = i[0:len(i)-1]
                print(i," Removed")
                os.remove(i)
        except:pass


    def progressBarAni():
        global io
        
        progLabel.configure(image = progList[io])

        io += 1

        

        id = progLabel.after(500, progressBarAni)

        if io == 5:
            io = 0
            try : 
                with open("switch_io.bb","r") as nri:
                    xxc = nri.read()
                    nri.close()
                
                if xxc == "1" or xxc == 1:
                    progLabel.after_cancel(id)
            
            except:pass

    def textShower():
        global samB

        ranHashShower.configure(state='normal')
        ranHashShower.delete("1.0",END)
        ranHashShower.insert(INSERT,samB[random.randint(0,len(samB)-1)])

        id = ranHashShower.after(100, textShower)

        try : 
            with open("switch_io.bb","r") as nri:
                xxc = nri.read()
                nri.close()
                
            if xxc == "1" or xxc == 1:
                ranHashShower.after_cancel(id)
            
        except:pass

    def VirusFoundPathX():

        try:
            with open ("switch_virusscanner.bb","r") as X:
                cc = X.readlines()
                X.close()
        

            virusFoundPaths.configure(state='normal')
            virusFoundPaths.delete("1.0",END)
            virusFoundPaths.insert(INSERT,cc)


        except:pass

        id = virusFoundPaths.after(200, VirusFoundPathX)

    backButtonImg = PhotoImage(file = "res\\back button.png").subsample(4,4)
    prog0 = PhotoImage( file = "res\\progress bar\\0.png").subsample(1,3)
    prog1 = PhotoImage( file = "res\\progress bar\\1.png").subsample(1,3)
    prog2 = PhotoImage( file = "res\\progress bar\\2.png").subsample(1,3)
    prog3 = PhotoImage( file = "res\\progress bar\\3.png").subsample(1,3)
    prog4 = PhotoImage( file = "res\\progress bar\\4.png").subsample(1,3)
    prog5 = PhotoImage( file = "res\\progress bar\\5.png").subsample(1,3)
    progList = [prog0,prog1,prog2,prog3,prog4,prog5]

    bitLinkMainLabel = Label(winFrame, text = "Full Scanning", font = "Times 21 bold")
    bitLinkMainLabel.pack(side = TOP, pady = 20)

    backButton = Button(winFrame, image = backButtonImg, command = HomeFrame)
    backButton.place(x = 10 , y = 10)

    progLabel = Label(winFrame, image = prog0)
    progLabel.place(x = 250, y = 70)


    pathLabel = Label(winFrame, text = "Virus Scanner", font = "Times 20 bold")
    pathLabel.place(x = 350, y = 130)

    ranHashShower = Text(winFrame, width=50, height=1, font= ('Sans Serif', 13, 'bold'),foreground="green")
    ranHashShower.place( x = 350 , y = 170)
    ranHashShower.insert(INSERT, "Write Something About Yourself")
    ranHashShower.configure(state='disabled')

    virusDetet = Label(winFrame, text = "Virus Found", font = "Times 20 bold")
    virusDetet.place(x = 350, y = 230)

    virusFoundPaths = Text(winFrame, width=100, height=10, bd = 0, font= ('Sans Serif', 13, 'bold'),foreground="red")
    virusFoundPaths.place( x = 50 , y = 290)
    virusFoundPaths.insert(INSERT, "No Virus Found")
    virusFoundPaths.configure(state='disabled')

    rMVirus = Button(winFrame, text = "Remove Virus", font = "Times 20 bold", command = removeVirusBtn)
    rMVirus.place(x = 350, y = 230)

    textShower()

    progressBarAni()

    os.startfile("scannerStartQuick.bat")

    VirusFoundPathX()


def customScanFunc():
    global winFrame
    global backButtonImg
    global prog0
    global prog1
    global prog2
    global prog3
    global prog4
    global prog5
    global io
    global ranHashShower
    global samB
    global rMVirus
    source_path = filedialog.askdirectory(title='Select the Parent Directory')
    
    with open("virusHash.unibit", "r") as nr:
        samB = nr.readlines()
        nr.close()

    winFrame.destroy()

    winFrame = Frame(window, width=1100, height = 600)
    winFrame.pack()
    winFrame.pack_propagate(0)

    io = 0

    def removeVirusBtn():
        global io
        io = []

        try:
            with open("switch_virusscanner.bb", "r", encoding="utf-8") as bb:
                io = bb.readlines()
        except FileNotFoundError:
            print("File 'switch_virusscanner.bb' not found")
        except Exception as e:
            print(f"Error reading file: {e}")

        try:
            for i in io:
                file_to_remove = i.strip()
                if os.path.exists(file_to_remove):
                    print(f"Removing {file_to_remove}")
                    os.remove(file_to_remove)
                else:
                    print(f"File not found: {file_to_remove}")
        except Exception as e:
            print(f"Error removing file: {e}")



    def progressBarAni():
        global io
        
        progLabel.configure(image = progList[io])

        io += 1

        

        id = progLabel.after(500, progressBarAni)

        if io == 5:
            io = 0
            try : 
                with open("switch_io.bb","r") as nri:
                    xxc = nri.read()
                    nri.close()
                
                if xxc == "1" or xxc == 1:
                    progLabel.after_cancel(id)
            
            except:pass

    def textShower():
        global samB

        ranHashShower.configure(state='normal')
        ranHashShower.delete("1.0",END)
        ranHashShower.insert(INSERT,samB[random.randint(0,len(samB)-1)])

        id = ranHashShower.after(100, textShower)

        try : 
            with open("switch_io.bb","r") as nri:
                xxc = nri.read()
                nri.close()
                
            if xxc == "1" or xxc == 1:
                ranHashShower.after_cancel(id)
            
        except:pass

    def VirusFoundPathX():

        try:
            with open ("switch_virusscanner.bb","r") as X:
                cc = X.readlines()
                X.close()
        

            virusFoundPaths.configure(state='normal')
            virusFoundPaths.delete("1.0",END)
            virusFoundPaths.insert(INSERT,cc)


        except:pass

        id = virusFoundPaths.after(200, VirusFoundPathX)

    backButtonImg = PhotoImage(file = "res\\back button.png").subsample(4,4)
    prog0 = PhotoImage( file = "res\\progress bar\\0.png").subsample(1,3)
    prog1 = PhotoImage( file = "res\\progress bar\\1.png").subsample(1,3)
    prog2 = PhotoImage( file = "res\\progress bar\\2.png").subsample(1,3)
    prog3 = PhotoImage( file = "res\\progress bar\\3.png").subsample(1,3)
    prog4 = PhotoImage( file = "res\\progress bar\\4.png").subsample(1,3)
    prog5 = PhotoImage( file = "res\\progress bar\\5.png").subsample(1,3)
    progList = [prog0,prog1,prog2,prog3,prog4,prog5]

    bitLinkMainLabel = Label(winFrame, text = "Custom Scanning", font = "Times 21 bold")
    bitLinkMainLabel.pack(side = TOP, pady = 20)

    backButton = Button(winFrame, image = backButtonImg, command = ScanFrame)
    backButton.place(x = 10 , y = 10)

    progLabel = Label(winFrame, image = prog0)
    progLabel.place(x = 250, y = 70)


    pathLabel = Label(winFrame, text = "Virus Scanner", font = "Times 20 bold")
    pathLabel.place(x = 350, y = 130)

    ranHashShower = Text(winFrame, width=50, height=1, font= ('Sans Serif', 13, 'bold'),foreground="green")
    ranHashShower.place( x = 350 , y = 170)
    ranHashShower.insert(INSERT, "Write Something About Yourself")
    ranHashShower.configure(state='disabled')

    virusDetet = Label(winFrame, text = "Virus Found", font = "Times 20 bold")
    virusDetet.place(x = 350, y = 230)

    virusFoundPaths = Text(winFrame, width=100, height=10, bd = 0, font= ('Sans Serif', 13, 'bold'),foreground="red")
    virusFoundPaths.place( x = 50 , y = 290)
    virusFoundPaths.insert(INSERT, "No Virus Found")
    virusFoundPaths.configure(state='disabled')

    rMVirus = Button(winFrame, text = "Remove Virus", font = "Times 20 bold", command = removeVirusBtn)
    rMVirus.place(x = 350, y = 230)

    textShower()

    progressBarAni()
    
    subprocess.run(["customScanner.bat", source_path], shell=True)

    VirusFoundPathX()


def junkFileRemoverFunc():
        ri = engine.juckFileRemover
        ri()

def ramBoosterFunc():
    ri = engine.ramBooster
    ri()
HomeFrame()



window.mainloop()