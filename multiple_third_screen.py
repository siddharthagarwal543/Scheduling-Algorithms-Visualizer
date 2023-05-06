from tkinter import *
from tkinter import messagebox
import multiple_connector
import Process_Table

def Table():
      Process_Table.sec_main()


def main():
    root = Tk()
    root.title("CPU Scheduling")
    root.geometry('1000x500+1100+400')
    root.resizable(1, 1)
    Tops = Frame(root, height=50, bd=8, relief="flat")
    Tops.pack(side=TOP)
    Label(Tops, font=('arial', 30, 'bold'),
          text="  Results  ", bd=5).grid(row=0, column=0)

    f1 = Frame(root, height=10, width=10, bd=4, relief="flat")
    f1.pack(side=TOP)
    av = multiple_connector.main()
    av_tat = "  Average Turn around time = {}".format(av['avg_tat'])
    av_wt = "  Average Waiting time =  {}".format(av['avg_wt'])
    Label(f1, font=('arial', 15, 'bold'),
          text=av_tat, bd=5).grid(row=0, column=0)
    Label(f1, font=('arial', 15, 'bold'),
          text=av_wt, bd=5).grid(row=1, column=0)

    f2 = Frame(root, height=10, width=100, bd=4, relief="flat")
    f2.pack(side=TOP)

# Label(f1, font=('arial', 20, 'bold'),
# text="    Gantt Chart   ", bd=5).grid(row=3, column=0)
# Label(f2, text=t1).grid(row=2, column=1)
# Label(f2, text=t2).grid(row=3, column=1)

    btnchart = Button(f2, text="Process Table", padx=6, pady=6, bd=2, fg="black",
                      font=('arial', 12, 'bold'), width=14, height=1,
                      command=Table).grid(row=0, column=0)

    root.mainloop()


if __name__ == "__main__":
    print("Run cpu_sheduler.py")
    main()
