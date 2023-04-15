import tkinter as tk
import tkinter.font as tkFont
from converter import transcript
from result import output, abort
class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=995
        height=650
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_807=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=60)
        GLabel_807["font"] = ft
        GLabel_807["fg"] = "#333333"
        GLabel_807["justify"] = "center"
        GLabel_807["text"] = "SpeechBot "
        GLabel_807.place(x=20,y=0,width=397,height=83)

        GButton_620=tk.Button(root)
        GButton_620["bg"] = "#f0f0f0"
        GButton_620["borderwidth"] = "2px"
        ft = tkFont.Font(family='Helvetica',size=10)
        GButton_620["font"] = ft
        GButton_620["fg"] = "#000000"
        GButton_620["justify"] = "center"
        GButton_620["text"] = ""
        GButton_620["relief"] = "flat"
        GButton_620.place(x=0,y=90,width=994,height=0)

        GButton_352=tk.Button(root)
        GButton_352["bg"] = "#01aaed"
        ft = tkFont.Font(family='Helvetica',size=30)
        GButton_352["font"] = ft
        GButton_352["fg"] = "#000000"
        GButton_352["justify"] = "center"
        GButton_352["text"] = "Chat"
        GButton_352["relief"] = "flat"
        GButton_352.place(x=30,y=110,width=525,height=90)
        GButton_352["command"] = self.thingy

        GButton_4=tk.Button(root)
        GButton_4["bg"] = "#ff5722"
        ft = tkFont.Font(family='Helvetica',size=30)
        GButton_4["font"] = ft
        GButton_4["fg"] = "#000000"
        GButton_4["justify"] = "center"
        GButton_4["text"] = "Abort"
        GButton_4["relief"] = "flat"
        GButton_4.place(x=590,y=110,width=372,height=90)
        GButton_4["command"] = self.abort2

        GButton_757=tk.Button(root)
        GButton_757["bg"] = "#f0f0f0"
        GButton_757["borderwidth"] = "2px"
        ft = tkFont.Font(family='Helvetica',size=10)
        GButton_757["font"] = ft
        GButton_757["fg"] = "#000000"
        GButton_757["justify"] = "center"
        GButton_757["text"] = ""
        GButton_757["relief"] = "flat"
        GButton_757.place(x=0,y=220,width=995,height=1)

        GButton_251=tk.Button(root)
        GButton_251["bg"] = "#f0f0f0"
        GButton_251["borderwidth"] = "2px"
        ft = tkFont.Font(family='Helvetica',size=10)
        GButton_251["font"] = ft
        GButton_251["fg"] = "#000000"
        GButton_251["justify"] = "center"
        GButton_251["text"] = ""
        GButton_251.place(x=500,y=230,width=1,height=363)

        GLabel_845=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=20)
        GLabel_845["font"] = ft
        GLabel_845["fg"] = "#333333"
        GLabel_845["justify"] = "center"
        GLabel_845["text"] = "You said: "
        GLabel_845.place(x=30,y=250,width=159,height=41)

        GLabel_382=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=20)
        GLabel_382["font"] = ft
        GLabel_382["fg"] = "#333333"
        GLabel_382["justify"] = "center"
        GLabel_382["text"] = "The Bot Says: "
        GLabel_382.place(x=530,y=240,width=197,height=58)


        GLabel_248=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=10)
        GLabel_248["font"] = ft
        GLabel_248["fg"] = "#333333"
        GLabel_248["justify"] = "center"
        GLabel_248["text"] = "Creator: Nikhil"
        GLabel_248.place(x=870,y=0,width=125,height=30)

        GLabel_822=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=10)
        GLabel_822["font"] = ft
        GLabel_822["fg"] = "#333333"
        GLabel_822["justify"] = "center"
        GLabel_822["text"] = "(c) 2023 Nikhil"
        GLabel_822.place(x=880,y=30,width=101,height=30)

    def thingy(self):
        print("here")
        trans = transcript()
        GLabel_571=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=16)
        GLabel_571["font"] = ft
        GLabel_571["fg"] = "#333333"
        GLabel_571["justify"] = "center"
        a = trans.split("|")
        str69 = ""
        for elm in a:
            str69 += elm + " "
        print(str69)
        GLabel_571["text"] = str69.lower()
        GLabel_571.place(x=50,y=310,width=395,height=259)
        asdasd = output(trans)

        try:
            e69 = asdasd.split("by")[0]
            f69 = "by " + asdasd.split("by")[1].split("on Nikhilodeon Music")[0]
        except:
            try:
                e69 = asdasd.split("date")[0] + "date"
                f69 = asdasd.split("date")[1]
            except:
                try:
                    e69 = asdasd.split("is currently")[0] + "is currently"
                    f69 = asdasd.split("is currently")[1]
                except:
                    try:
                        e69 = asdasd.split("companies")[0]
                        f69 = "companies" + asdasd.split("companies")[1]
                    except:
                        e69 = asdasd
                        f69 = " "
        
        GLabel_836=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=14)
        GLabel_836["font"] = ft
        GLabel_836["fg"] = "#333333"
        GLabel_836["justify"] = "center"
        print("thing ->" + asdasd)
        GLabel_836["text"] = e69
        GLabel_836.place(x=550,y=350,width=402,height=100)

        GLabel_694=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=14)
        GLabel_694["font"] = ft
        GLabel_694["fg"] = "#333333"
        GLabel_694["justify"] = "center"
        print("thing ->" + asdasd)
        GLabel_694["text"] = f69
        GLabel_694.place(x=550,y=450,width=402,height=100)


    def abort2(self):
        abort()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
