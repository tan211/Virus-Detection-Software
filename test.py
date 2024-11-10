from glob import glob
from tkinter import*
import psutil
import pystray
import PIL.Image
from screeninfo import get_monitors

#--------------------Global Variable ---------------------# 



#--------------------Global Variable End ---------------------# 


#--------------------Tkinter Base Setup ---------------------# 

 
 
# class GetGeometry:
#     def __init__(self):
#         self.geometry = []
 
#     def get_tkinter_geometry(self, percent_of_screen, xpad=None, ypad=None):
#         '''
 
#         returns: list holding tkinter geometry strings padded with xpad and ypad
#                 or centered if xpad is None.
                 
#                 None if bad pct passed
#         '''
 
#         if not isinstance(percent_of_screen, float):
#             print("requires float percent eg: 10.0 for 10%")
#             return
 
#         pct = percent_of_screen / 100
 
#         for size in get_monitors():
#             cwidth = int(size.width * pct)
#             cheight = int(size.height * pct)
 
#             xoff = xpad
#             yoff = ypad
#             if xpad is None:
#                 xoff = int((size.width - cwidth) / 2)
#                 yoff = int((size.height - cheight) / 2)
#             self.geometry.append(f"{cwidth}x{cheight}+{xoff}+{yoff}")


# gg = GetGeometry()
# # padding specified 10 % of screen dimensions
# gg.get_tkinter_geometry(10.0, 10, 10)
# geometry = gg.geometry
# print(f"\ngeometry - 10% of monitor size 10 pixel x and y padding:\n{geometry}")
 
# # padding not specified 60 % of screen dimensions
# gg.get_tkinter_geometry(60.0)
# geometry = gg.geometry
# print(f"\ngeometry - 60% of monitor size centered (no pading specified):\n{geometry}")


window = Tk()

window.title("BitLink End-Point")
window.geometry("1200x850")
window.minsize("1200","850")
window.maxsize("1200","850")

winFrame = Frame(window,width="1200",height="850",bg="gray17")
winFrame.pack()
winFrame.pack_propagate(0)

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

    global logoLabelImg
    logoLabelImg = PhotoImage(file='res\\Logo\\logo.png')
    logoLabel = Label(winFrame,image=logoLabelImg,bg='gray17')
    logoLabel.place(x=10,y=0)

    global nameLabelImg
    nameLabelImg = PhotoImage(file='res\\Logo\\b logo.png').subsample(2,2)
    nameLabel = Label(winFrame,image=nameLabelImg,bg='gray17')
    nameLabel.place(x=90,y=20)
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



    systemButton = Label(winFrame,image=systemButtonImg,bg="gray17",cursor="hand2")
    systemButton.place(x=515,y=570)

    systemButton.bind('<Enter>',SystemButtonEnterFrame)
    systemButton.bind('<Leave>',SystemButtonLeaveFrame)

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
    robotAnimation.place(x=405,y=150)

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

    ramBooster = Label(winFrame, image=ramBoosterImg, bg="gray17", cursor="hand2")
    ramBooster.place(x=840,y=280)
    ramBooster.bind('<Enter>',RamBoosterEnter)
    ramBooster.bind('<Leave>',RamBoosterLeave)


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

    global logoLabelImg
    logoLabelImg = PhotoImage(file='res\\Logo\\logo.png')
    logoLabel = Label(winFrame,image=logoLabelImg,bg='gray17')
    logoLabel.place(x=10,y=0)

    global nameLabelImg
    nameLabelImg = PhotoImage(file='res\\Logo\\b logo.png').subsample(2,2)
    nameLabel = Label(winFrame,image=nameLabelImg,bg='gray17')
    nameLabel.place(x=90,y=20)
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


    fullScanButton_1place = Label(winFrame,image=fullScanButton_1,bg='gray17', cursor="hand2")
    fullScanButton_1place.place(x=510,y=240)

    fullScanButton_1place.bind('<Enter>',fullScanButton_1_Enter)
    fullScanButton_1place.bind('<Leave>',fullScanButton_1_Leave)

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

    deepScanButton_1place = Label(winFrame,image=deepScanButton_1,bg='gray17', cursor="hand2")
    deepScanButton_1place.place(x=510,y=310)

    deepScanButton_1place.bind('<Enter>',deepScanButton_1_Enter)
    deepScanButton_1place.bind('<Leave>',deepScanButton_1_Leave)

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

    CustomScanButton_1place = Label(winFrame,image=CustomScanButton_1,bg='gray17', cursor="hand2")
    CustomScanButton_1place.place(x=530,y=380)

    CustomScanButton_1place.bind('<Enter>',CustomScanButton_1_Enter)
    CustomScanButton_1place.bind('<Leave>',CustomScanButton_1_Leave)

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

    systemButton = Label(winFrame,image=systemButtonImg,bg="gray17",cursor="hand2")
    systemButton.place(x=515,y=570)

    systemButton.bind('<Enter>',SystemButtonEnterFrame)
    systemButton.bind('<Leave>',SystemButtonLeaveFrame)

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


HomeFrame()



window.mainloop()