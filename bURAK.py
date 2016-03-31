from tkinter import *
import  os
import getpass

from orca.scripts.apps import soffice

pencere=Tk()
pencere.title("BAŞLAT MENÜSÜ")
pencere.tk_setPalette("#FFFFFF")
#başlıksız...pencere.overrideredirect(1)
pencere.wm_iconbitmap("hourglass")
menu = Menu(pencere)
#pencere.geometry("400x300")
#pencere.state("iconic")

#kullanici bilgi getir
deneme= PhotoImage(file="users.png")
foto=Label(pencere,image=deneme,width=100)
foto.pack(anchor="e")
kullanici = Label(pencere, text=getpass.getuser(), width=15)
kullanici.pack(anchor="e")




#Belge
def belge_ac():
    import  os
    os.system("nautilus /home/"+getpass.getuser()+"/Belgeler")

btn_belge = Button(text="Belgeler",command=belge_ac,width=10)
btn_belge.pack(anchor="e")

#Resimler
def resim_ac():
    import  os
    os.system("nautilus /home/"+getpass.getuser()+"/Resimler")

btn_resim = Button(text="Resimler",command=resim_ac,width=10)
btn_resim.pack(anchor="e")

#Muzik
def muzik_ac():
    import  os
    os.system("nautilus /home/"+getpass.getuser()+"/Muzik")

btn_muzik = Button(text="Müzikler",command=muzik_ac,width=10)
btn_muzik.pack(anchor="e")

#Videolar
def video_ac():
    import  os
    os.system("nautilus /home/"+getpass.getuser()+"/Videolar")

btn_video = Button(text="Videolar",command=video_ac,width=10)
btn_video.pack(anchor="e")


#Bilgisayar
def disk_ac():
    import  os
    os.system("nautilus /")

btn_disk = Button(text="Bilgisayarım",command=disk_ac,width=10)
btn_disk.pack(anchor="e")

#DENETİM MASASI AÇMA
def calistir():
    import  os
    os.system("unity-control-center")

btn_denetim = Button(text="Denetim Masası",command=calistir,width=10)
btn_denetim.pack(anchor="e")

#terminal
def terminal():
    import  os
    os.system("gnome-terminal")

btn_terminal = Button(text="Terminal",command=terminal,width=10)
btn_terminal.pack(anchor="e")


def yardımMerkezi():
    os.system("gnome-help")
btn_help = Button(text="Yardım ve Destek",command=yardımMerkezi,width=10)
btn_help.pack(anchor="e")



#Arama
#def search():
    #veri=entry.get()
    #print(veri)

#entry = Entry()
#entry.pack(side="left")
#entry.pack(anchor="sw")


#btn_ara = Button(text="ARA",command=search)
#btn_ara.pack(side="left")
#btn_ara.pack(anchor="sw")
#pencere.geometry("400x300")
#pencere.state("iconic")

#kapatma...

def kapatma():
    os.system("shutdown -h now")

btn_kapat = Button(text="kapat",
                   command=kapatma)
btn_kapat.pack(side="right")
btn_kapat.pack(anchor="sw")

#reset

def resetle():
    os.system("shutdown -r now")

btn_reset = Button(text="reset",
                   command=resetle)
btn_reset.pack(side="right")
btn_reset.pack(anchor="sw")



tummenu= Menu(pencere)
pencere.config(menu=tummenu)

def calistir():
    os.system("unity-control-center")

#Donatılar
def hesapMakinesi():
    os.system("gnome-calculator")

#oyunlar
def mayin():
    os.system("gnome-mines")
def pisti():
    os.system("gnome-mahjongg")
def sudoku():
    os.system("gnome-sudoku")

#ubuntuYazılımMerkezi
def software():
    os.system("software-center")



pencere.config(menu=menu)
dosya = Menu(menu, tearoff=0,)
menu.add_cascade(label="Donatılar",menu=dosya)
dosya.add_command(label="Hesap Makinesi",command=hesapMakinesi )
dosya.add_command(label="Ubuntu Yazılım Merkezi",command=software )



oyun = Menu(dosya,tearoff=0)
dosya.add_cascade(label="OYUNLAR",menu=oyun)
oyun.add_command(label="Mayın Tarlası", command=mayin)
oyun.add_command(label="Pişti",command=pisti)
oyun.add_command(label="Sudoku",command=sudoku)


mainloop()