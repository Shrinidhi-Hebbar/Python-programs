#Tkinter module
import tkinter as tk
import tkinter.messagebox as msgbox
form=tk.Tk()
form.geometry('500x500')

lbluno=tk.Label(form,text="UUCMS")
lbluno.grid(row=0,column=0,stick=tk.W,padx=10,pady=10)
etuno=tk.Entry(form,width=20)
etuno.grid(row=0,column=1,padx=5,pady=5)

lblname=tk.Label(form,text="NAME")
lblname.grid(row=1,column=0,stick=tk.W,padx=10,pady=10)
etname=tk.Entry(form,width=20)
etname.grid(row=1,column=1,padx=5,pady=5)

lblgender=tk.Label(form,text="GENDER")
lblgender.grid(row=2,column=0,stick=tk.W,padx=10,pady=10)
gendervar=tk.StringVar()
gendervar.set("Male")
rdmale=tk.Radiobutton(form,text="Male",value="male",variable=gendervar)
rdfemale=tk.Radiobutton(form,text="female",value="female",variable=gendervar)
rdmale.grid(row=2,column=1,padx=5,pady=5)
rdfemale.grid(row=2,column=2,padx=5,pady=5)

lblnotify=tk.Label(form,text="Notification cannel")
lblnotify.grid(row=3,column=0,stick=tk.W,padx=10,pady=10)
wappvar=tk.BooleanVar()
mailvar=tk.BooleanVar()
chkbwapp=tk.Checkbutton(form,text="Watsapp",variable=wappvar)
chkbmail=tk.Checkbutton(form,text="Email",variable=mailvar)
chkbwapp.grid(row=3,column=1,padx=5,pady=5)
chkbmail.grid(row=3,column=2,padx=5,pady=5)

def save():
    uno=etuno.get()
    name=etname.get()
    gender=gendervar.get()
    wapp=wappvar.get()
    mail=mailvar.get()
    row=f"{uno},{name},{gender}"
    if wapp:
        row=row+f"{wapp}"
        if mail:
            row=row+f"{mail}"
    file=open("student1.csv","a")
    file.write(row)
    file.close()
    msgbox.showinfo("message","Data saved successfully")
btnsave=tk.Button(form,text="save",command=save)
btnsave.grid(row=4,column=0,columnspan=3,padx=5,pady=5)
form.mainloop()

        





