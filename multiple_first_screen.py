from tkinter import *
from tkinter import messagebox
import multiple_second_screen


def main():
    root = Tk()
    #App Styling
    root.title("Scheduling Algorithm Visualizer")
    root.geometry('500x350+550+200')
    root.resizable(1, 1)
    Tops = Frame(root, height=50, bd=8, relief="raise")
    Tops.pack(side=TOP)
    Label(Tops, font=('arial', 20, 'bold'),
          text="Scheduling Algorithm Visualizer", bd=5).grid(row=0, column=0)

    def iExit():
        qExit = messagebox.askyesno("CPU Scheduling", "Do you want to exit?")
        if qExit > 0:
            root.destroy()
            return

    def go():
        f = open('fl.txt', 'w')
    #     fcfs=IntVar()
    # sjf=IntVar()
    # srtf=IntVar()
    # pp=IntVar()
    # pnp=IntVar()
    # rr=IntVar()
        selection = str(fcfs.get())
        f.write(selection)
        selection = str(sjf.get())
        f.write(selection)
        selection = str(srtf.get())
        f.write(selection)
        selection = str(pp.get())
        f.write(selection)
        selection = str(pnp.get())
        f.write(selection)
        selection = str(rr.get())
        f.write(selection)
        f.close()
        root.destroy()
        multiple_second_screen.sec_main()

    v = IntVar()
    fcfs=IntVar()
    sjf=IntVar()
    srtf=IntVar()
    pp=IntVar()
    pnp=IntVar()
    rr=IntVar()

    f1 = Frame(root, height=10, width=10, bd=4, relief="ridge")
    f1.pack(side=TOP)

    f2 = Frame(root, height=10, width=100, bd=4, relief="raise")
    f2.pack(side=RIGHT)

    Label(f1, font=('arial', 15, 'bold'),
          text="Choose a scheduling algorithm:",
          justify=LEFT, padx=20).pack(side=LEFT)

    fcfs_rbtn = Checkbutton(f1, text="FCFS", padx=20,
                            variable=fcfs, onvalue=1).pack(anchor=W)
    sjf_rbtn = Checkbutton(f1, text="SJF", padx=20,
                           variable=sjf, onvalue=2).pack(anchor=W)
    srtf_rbtn = Checkbutton(f1, text="SRTF", padx=20,
                            variable=srtf, onvalue=3).pack(anchor=W)
    pp_rbtn = Checkbutton(f1, text="Priority(Preemptive)",
                          padx=20, variable=pp, onvalue=4).pack(anchor=W)
    pnp_rbtn = Checkbutton(f1, text="Priority(Non-Preemptive)",
                           padx=20, variable=pnp, onvalue=5).pack(anchor=W)
    rr_rbtn = Checkbutton(f1, text="Round Robin", padx=20,
                          variable=rr, onvalue=6).pack(anchor=W)
    # fcfs_btn=Checkbutton(f1, text="FCFS", padx=20,variable=v, value=1).pack(anchor=W)


    btnGo = Button(f2, text="Go", padx=6, pady=6, bd=2, fg="black", font=(
        'arial', 12, 'bold'), width=14, height=1, command=go).grid(row=0,
                                                                   column=0)
    btnExit = Button(f2, text="Exit", padx=6, pady=6, bd=2, fg="black", font=(
        'arial', 12, 'bold'), width=14, height=1, command=iExit).grid(row=0,
                                                                      column=1)

    root.mainloop()


if __name__ == "__main__":
    print("Run cpu_sheduler.py")
