from tkinter import *
from tkinter import messagebox
import multiple_connector
import Process_Table
import multiple_first_screen
import single_first_screen


def main():
    def multiple():
        root.destroy()
        multiple_first_screen.main()

    def single():
        root.destroy()
        single_first_screen.main()

    root = Tk()
    root.title("CPU Scheduling")
    root.geometry('1000x500+1100+400')
    root.resizable(1, 1)
    Tops = Frame(root, height=50, bd=8, relief="flat")
    Tops.pack(side=TOP)
    Label(Tops, font=('arial', 30, 'bold'),
          text="  Scheduling Algorithm Visualzier  ", bd=5).grid(row=0, column=0)

    f1 = Frame(root, height=10, width=10, bd=4, relief="flat")
    f1.pack(side=TOP)
    btnchart = Button(f1, text="Single mode", padx=6, pady=6, bd=2, fg="black",command=single,
                      font=('arial', 12, 'bold'), width=14, height=1,).grid(row=0, column=0)

    f2 = Frame(root, height=10, width=100, bd=4, relief="flat")
    f2.pack(side=TOP)
    btnchart = Button(f2, text="Multiple mode", padx=6, pady=6, bd=2, fg="black",command=multiple,
                      font=('arial', 12, 'bold'), width=14, height=1,).grid(row=0, column=0)

# Label(f1, font=('arial', 20, 'bold'),
# text="    Gantt Chart   ", bd=5).grid(row=3, column=0)
# Label(f2, text=t1).grid(row=2, column=1)
# Label(f2, text=t2).grid(row=3, column=1)
    root.mainloop()


if __name__ == "__main__":
    main()