import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import DashBoard_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    DashBoard_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    DashBoard_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+2035+135")
        top.minsize(120, 1)
        top.maxsize(3290, 1061)
        top.resizable(1,  1)
        top.title("DashBoard v.0")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.033, rely=0.089, relheight=0.789
                , relwidth=0.942)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Labelframe1 = tk.LabelFrame(self.Frame1)
        self.Labelframe1.place(relx=0.018, rely=0.028, relheight=0.31
                , relwidth=0.301)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Time''')
        self.Labelframe1.configure(background="#77bbff")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        self.Text1 = tk.Text(self.Labelframe1)
        self.Text1.place(relx=0.059, rely=0.545, relheight=0.309, relwidth=0.847
                , bordermode='ignore')
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        self.Text1.configure(wrap="word")

        self.Labelframe2 = tk.LabelFrame(self.Frame1)
        self.Labelframe2.place(relx=0.354, rely=0.028, relheight=0.31
                , relwidth=0.301)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''Temperature''')
        self.Labelframe2.configure(background="#ff6464")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")

        self.Text2 = tk.Text(self.Labelframe2)
        self.Text2.place(relx=0.059, rely=0.545, relheight=0.309, relwidth=0.847
                , bordermode='ignore')
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="blue")
        self.Text2.configure(selectforeground="white")
        self.Text2.configure(wrap="word")

        self.Labelframe3 = tk.LabelFrame(self.Frame1)
        self.Labelframe3.place(relx=0.69, rely=0.0, relheight=0.31
                , relwidth=0.301)
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(text='''Wind Direction''')
        self.Labelframe3.configure(background="#00ea00")
        self.Labelframe3.configure(highlightbackground="#d9d9d9")
        self.Labelframe3.configure(highlightcolor="black")

        self.Text3 = tk.Text(self.Labelframe3)
        self.Text3.place(relx=0.059, rely=0.545, relheight=0.309, relwidth=0.847
                , bordermode='ignore')
        self.Text3.configure(background="white")
        self.Text3.configure(font="TkTextFont")
        self.Text3.configure(foreground="black")
        self.Text3.configure(highlightbackground="#d9d9d9")
        self.Text3.configure(highlightcolor="black")
        self.Text3.configure(insertbackground="black")
        self.Text3.configure(selectbackground="blue")
        self.Text3.configure(selectforeground="white")
        self.Text3.configure(wrap="word")

        self.Labelframe4 = tk.LabelFrame(self.Frame1)
        self.Labelframe4.place(relx=0.018, rely=0.338, relheight=0.31
                , relwidth=0.301)
        self.Labelframe4.configure(relief='groove')
        self.Labelframe4.configure(foreground="black")
        self.Labelframe4.configure(text='''Longitute''')
        self.Labelframe4.configure(background="#ffff80")
        self.Labelframe4.configure(highlightbackground="#d9d9d9")
        self.Labelframe4.configure(highlightcolor="black")

        self.Text4 = tk.Text(self.Labelframe4)
        self.Text4.place(relx=0.059, rely=0.545, relheight=0.4, relwidth=0.847
                , bordermode='ignore')
        self.Text4.configure(background="white")
        self.Text4.configure(font="TkTextFont")
        self.Text4.configure(foreground="black")
        self.Text4.configure(highlightbackground="#d9d9d9")
        self.Text4.configure(highlightcolor="black")
        self.Text4.configure(insertbackground="black")
        self.Text4.configure(selectbackground="blue")
        self.Text4.configure(selectforeground="white")
        self.Text4.configure(wrap="word")

        self.Labelframe5 = tk.LabelFrame(self.Frame1)
        self.Labelframe5.place(relx=0.354, rely=0.338, relheight=0.31
                , relwidth=0.301)
        self.Labelframe5.configure(relief='groove')
        self.Labelframe5.configure(foreground="black")
        self.Labelframe5.configure(text='''Latitude''')
        self.Labelframe5.configure(background="#ff8000")
        self.Labelframe5.configure(highlightbackground="#d9d9d9")
        self.Labelframe5.configure(highlightcolor="black")

        self.Text5 = tk.Text(self.Labelframe5)
        self.Text5.place(relx=0.059, rely=0.455, relheight=0.4, relwidth=0.847
                , bordermode='ignore')
        self.Text5.configure(background="white")
        self.Text5.configure(font="TkTextFont")
        self.Text5.configure(foreground="black")
        self.Text5.configure(highlightbackground="#d9d9d9")
        self.Text5.configure(highlightcolor="black")
        self.Text5.configure(insertbackground="black")
        self.Text5.configure(selectbackground="blue")
        self.Text5.configure(selectforeground="white")
        self.Text5.configure(wrap="word")

        self.Labelframe6 = tk.LabelFrame(self.Frame1)
        self.Labelframe6.place(relx=0.69, rely=0.31, relheight=0.31
                , relwidth=0.301)
        self.Labelframe6.configure(relief='groove')
        self.Labelframe6.configure(foreground="black")
        self.Labelframe6.configure(text='''Altitude''')
        self.Labelframe6.configure(background="#8000ff")
        self.Labelframe6.configure(highlightbackground="#d9d9d9")
        self.Labelframe6.configure(highlightcolor="black")

        self.Text6 = tk.Text(self.Labelframe6)
        self.Text6.place(relx=0.059, rely=0.545, relheight=0.4, relwidth=0.847
                , bordermode='ignore')
        self.Text6.configure(background="white")
        self.Text6.configure(font="TkTextFont")
        self.Text6.configure(foreground="black")
        self.Text6.configure(highlightbackground="#d9d9d9")
        self.Text6.configure(highlightcolor="black")
        self.Text6.configure(insertbackground="black")
        self.Text6.configure(selectbackground="blue")
        self.Text6.configure(selectforeground="white")
        self.Text6.configure(wrap="word")

        self.Labelframe7 = tk.LabelFrame(self.Frame1)
        self.Labelframe7.place(relx=0.018, rely=0.648, relheight=0.31
                , relwidth=0.301)
        self.Labelframe7.configure(relief='groove')
        self.Labelframe7.configure(foreground="black")
        self.Labelframe7.configure(text='''Feature X''')
        self.Labelframe7.configure(background="#ff00ff")
        self.Labelframe7.configure(highlightbackground="#d9d9d9")
        self.Labelframe7.configure(highlightcolor="black")

        self.Text7 = tk.Text(self.Labelframe7)
        self.Text7.place(relx=0.059, rely=0.455, relheight=0.491, relwidth=0.906
                , bordermode='ignore')
        self.Text7.configure(background="white")
        self.Text7.configure(font="TkTextFont")
        self.Text7.configure(foreground="black")
        self.Text7.configure(highlightbackground="#d9d9d9")
        self.Text7.configure(highlightcolor="black")
        self.Text7.configure(insertbackground="black")
        self.Text7.configure(selectbackground="blue")
        self.Text7.configure(selectforeground="white")
        self.Text7.configure(wrap="word")

        self.Labelframe8 = tk.LabelFrame(self.Frame1)
        self.Labelframe8.place(relx=0.354, rely=0.662, relheight=0.31
                , relwidth=0.301)
        self.Labelframe8.configure(relief='groove')
        self.Labelframe8.configure(foreground="black")
        self.Labelframe8.configure(text='''Feature Y''')
        self.Labelframe8.configure(background="#408080")
        self.Labelframe8.configure(highlightbackground="#d9d9d9")
        self.Labelframe8.configure(highlightcolor="black")

        self.Text8 = tk.Text(self.Labelframe8)
        self.Text8.place(relx=0.059, rely=0.455, relheight=0.491, relwidth=0.906
                , bordermode='ignore')
        self.Text8.configure(background="white")
        self.Text8.configure(font="TkTextFont")
        self.Text8.configure(foreground="black")
        self.Text8.configure(highlightbackground="#d9d9d9")
        self.Text8.configure(highlightcolor="black")
        self.Text8.configure(insertbackground="black")
        self.Text8.configure(selectbackground="blue")
        self.Text8.configure(selectforeground="white")
        self.Text8.configure(wrap="word")

        self.Labelframe9 = tk.LabelFrame(self.Frame1)
        self.Labelframe9.place(relx=0.69, rely=0.662, relheight=0.31
                , relwidth=0.301)
        self.Labelframe9.configure(relief='groove')
        self.Labelframe9.configure(foreground="black")
        self.Labelframe9.configure(text='''Feature Z''')
        self.Labelframe9.configure(background="#ff8040")
        self.Labelframe9.configure(highlightbackground="#d9d9d9")
        self.Labelframe9.configure(highlightcolor="black")

        self.Text9 = tk.Text(self.Labelframe9)
        self.Text9.place(relx=0.059, rely=0.455, relheight=0.491, relwidth=0.906
                , bordermode='ignore')
        self.Text9.configure(background="white")
        self.Text9.configure(font="TkTextFont")
        self.Text9.configure(foreground="black")
        self.Text9.configure(highlightbackground="#d9d9d9")
        self.Text9.configure(highlightcolor="black")
        self.Text9.configure(insertbackground="black")
        self.Text9.configure(selectbackground="blue")
        self.Text9.configure(selectforeground="white")
        self.Text9.configure(wrap="word")

        self.TSeparator1 = ttk.Separator(self.Frame1)
        self.TSeparator1.place(relx=0.336, rely=0.0,  relheight=0.98)
        self.TSeparator1.configure(orient="vertical")

        self.TSeparator2 = ttk.Separator(self.Frame1)
        self.TSeparator2.place(relx=0.673, rely=-0.028,  relheight=1.008)
        self.TSeparator2.configure(orient="vertical")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.167, rely=0.022, height=21, width=414)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#80ffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Cooper Black} -size 20 -weight bold -underline 1")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Dash Board''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.1, rely=0.911, height=24, width=87)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Button''')

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.417, rely=0.911, height=24, width=87)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(cursor="fleur")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Button''')

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.7, rely=0.911, height=24, width=127)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Button''')

if __name__ == '__main__':
    vp_start_gui()






