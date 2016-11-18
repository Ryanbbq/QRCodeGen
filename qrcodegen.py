#Unique QR Code Generator
#CST 205 Project 2
#Generates two different versions of QR Codes
#Authors- Ryan,Jason,Elias
#October 14 2016
import tkinter as tk
from tkinter import ttk
from MyQR import myqr
from tkinter import filedialog
import os
import qrcode
import struct
import statistics
import imghdr
from PIL import Image


LARGE_FONT = ("Verdana", 12)
small_font = ("Verdana",8)
#global values that will be used in QR Definitions...(qr_1 and qr_2)
#change with "global"
filePath = ''
version = 0
output=''
website=''
askUser=''
askVersion=0
#tkinter framework created by Elais
class QRgenerator(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        tk.Tk.wm_title(self,"QR Code Generator")
        container.pack(side = "top", fill  = "both", expand = True)

        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)

        self.frames = {}

        for f in (StartPage,PageOne,QR1,QR2):
        
            frame = f(container, self)
            
            self.frames[f] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

#QR Code 1 created by Jason
#uses myqr to generate a qr code
def qr_1(file,newurl,vers,output):

    num = vers
    # url = 
    url = newurl
    pic = file
    location=output
    print("Starting...")
    version, level, qr_name = myqr.run(
        words=url,
        version=num,
        level='H',
        picture=pic,
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name=None,
        save_dir=location,
        )
    print("Finished")
#QR Code 2 created by Ryan
#uses qrcode to generate a qr code, merges images together with commands
def qr_2(website,askUser,askVersion):
    qr=qrcode.QRCode(
    version=askVersion,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=8,
    border=2.5,
    )
    userImage=askUser
    userImage=Image.open(askUser)
 
    qr.add_data(website)
    qr.make(fit=True)
    
  
    
    #creates the Qr Code
    imgQr=qr.make_image()
    #converts the QR code so that we can have an alpha value
    imgQr=imgQr.convert("RGBA")
    #get the data of the qr Code
    dataQr=imgQr.getdata()

    newData2 = []
    for items in dataQr:
        if items[0] == 255 and items[1] == 255 and items[2] == 255:
            newData2.append((255, 255, 255,0))
        else:
            newData2.append(items)

    imgQr.putdata(newData2)
    pictureQRwidth=imgQr.size[0]
    pictureQRheight=imgQr.size[1]
    #creates a newUserImage and resizes it.
    newUserImage=userImage.resize((pictureQRwidth,pictureQRheight))
    #converts a newUserImage so that we can have an alpha value
    newUserImage=newUserImage.convert("RGBA")


    bands=list(newUserImage.split())
    if len(bands)==4:
        bands[3]=bands[3].point(lambda x: x*.3)
    newUserImage=Image.merge(newUserImage.mode,bands)

    imgQr.paste(newUserImage,(0,0),newUserImage)


    pictureWidth=newUserImage.size[0]
    pictureHeight=newUserImage.size[1]

  

    print("The size of the users image is: ",newUserImage.size)
    print("The size of the QR code is: ",imgQr.size)

    imgQr.show()
#Startpage created by Elias
#Basic startpage using tkinter allows you to pick pages
class StartPage(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "Project 2", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)
        
        button1 = ttk.Button(self,text = "Begin", command = lambda: controller.show_frame(PageOne))
        button1.pack()

        label2 = ttk.Label(self,text = "by Jason, Ryan, Elias", font = small_font)
        label2.pack(pady = 12, padx = 10)
#Page One created by Elias
#uses tkinter allows user to switch pages and pick options
class PageOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "Pick an Option", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)
        
        button1 = ttk.Button(self,text = "1", command = lambda: controller.show_frame(QR1))
        button1.place(x = 0, y = 0)
        
        button2 = ttk.Button(self,text = "2", command = lambda: controller.show_frame(QR2))
        button2.place(x = 425, y = 0)
#Page Two created by Elias
#uses tkinter allows user to switch pages and pick options
class PageTwo(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "Pick an Option", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)
        
        button1 = ttk.Button(self,text = "1", command = lambda: controller.show_frame(QR1))
        button1.place(x = 0, y = 0)
        
        button2 = ttk.Button(self,text = "2", command = lambda: controller.show_frame(QR2))
        button2.place(x = 425, y = 0)
#QR1 Page created by Elias,Jason,Ryan
#uses tkinter calls fucntion qr_1
class QR1(tk.Frame):
    
    def __init__(self,parent,controller):
        
        def submit():
            global URLin
            URLin = url_entry.get()
            print(URLin)
            
        def submit2():
            global version
            version = int(size_entry.get())
            print(version)

        def submit_Out():
            global output
            output=out_entry.get()
            print(output)
            

        def Browse():
            global filePath
            filename = filedialog.askopenfilename()
            filePath = filename
            file_label = ttk.Label(self,text = filePath, font = LARGE_FONT)
            file_label.place(x = 0, y = 200)

            print(filePath)

            
            
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "QR Code 1", font = LARGE_FONT)
        label.pack()

        label = ttk.Label(self,text = "QR Code 1", font = LARGE_FONT)
        button1 = ttk.Button(self,text = "Back", command = lambda: controller.show_frame(PageOne))
        button1.place(x = 0, y = 450)

        url_label = ttk.Label(self,text = "Enter URL in box", font = LARGE_FONT)
        url_label.place(x = 100, y = 25)
        
        submit1 = ttk.Button(self,text = "Submit", command = submit)
        submit1.place(x = 0, y = 25)

        url_entry = ttk.Entry(self,width = 50)
        url_entry.place(x = 0, y = 50)
        
         
        out_label = ttk.Label(self,text = "Enter file output directory", font = LARGE_FONT)
        out_label.place(x = 100, y = 75)

        submit_Out = ttk.Button(self,text = "Submit", command = submit_Out)
        submit_Out.place(x = 0, y = 75)

        out_entry=ttk.Entry(self,width=50)
        out_entry.place(x=0,y=100)

        submit2 = ttk.Button(self,text = "Submit", command = submit2)
        submit2.place(x = 0, y = 125)

        size_label = ttk.Label(self,text = "Enter the size of the QR code", font = LARGE_FONT)
        size_label.place(x = 100, y = 125)
        
        size_entry = ttk.Entry(self,width = 50)
        size_entry.place(x = 0, y = 150)

        file_label=ttk.Label(self,text="Choose a Picture",font=LARGE_FONT)
        file_label.place(x=100,y=175)

        FileBrowse = ttk.Button(self,text = "Browse",command = Browse)
        FileBrowse.place(x = 0, y= 175)



            
        run = ttk.Button(self,text = "Run", command = lambda: qr_1(filePath,URLin,version,output))
        run.place(x = 0, y = 400)



#QR2 Page created by Ryan
#uses tkinter calls function qr_2
class QR2(tk.Frame):

    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)


        def submit():
            global website
            website = url_entry.get()
            print(website)
        def Browse():
            global askUser
            filename = filedialog.askopenfilename()
            askUser = filename
            file_label = ttk.Label(self,text = askUser, font = LARGE_FONT)
            file_label.place(x = 0, y = 150)
            print(filePath)
            
        def submit2():
            global askVersion
            askVersion = int(size_entry.get())
            print(askVersion)

        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "QR Code 2", font = LARGE_FONT)
        label.pack()

        label = ttk.Label(self,text = "QR Code 1", font = LARGE_FONT)
        
        button1 = ttk.Button(self,text = "Back", command = lambda: controller.show_frame(PageOne))
        button1.place(x = 0, y = 450)

        url_label = ttk.Label(self,text = "Enter URL in box", font = LARGE_FONT)
        url_label.place(x = 100, y = 25)
        
        submit1 = ttk.Button(self,text = "Submit", command = submit)
        submit1.place(x = 0, y = 25)

        url_entry = ttk.Entry(self,width = 50)
        url_entry.place(x = 0, y = 50)
        
        #this would be an output label but it is not working... just going to show the image instead....
        #out_label = ttk.Label(self,text = "Enter file output directory", font = LARGE_FONT)
        #out_label.place(x = 100, y = 75)

        #submit_Out = ttk.Button(self,text = "Submit", command = submit_Out)
        #submit_Out.place(x = 0, y = 75)

        #out_entry=ttk.Entry(self,width=50)
        #out_entry.place(x=0,y=100)
        
        submit2 = ttk.Button(self,text = "Submit", command = submit2)
        submit2.place(x = 0, y = 75)

        size_label = ttk.Label(self,text = "Enter the size of the QR code", font = LARGE_FONT)
        size_label.place(x = 100, y = 75)
        
        size_entry = ttk.Entry(self,width = 50)
        size_entry.place(x = 0, y = 100)

        file_label=ttk.Label(self,text="Choose a Picture",font=LARGE_FONT)
        file_label.place(x=100,y=125)

        FileBrowse = ttk.Button(self,text = "Browse",command = Browse)
        FileBrowse.place(x = 0, y= 125)


            
        run = ttk.Button(self,text = "Run", command = lambda: qr_2(website,askUser,askVersion))
        run.place(x = 0, y = 400)


        
app = QRgenerator()
#creates a window thats 500x500
app.geometry("500x500")
app.mainloop()