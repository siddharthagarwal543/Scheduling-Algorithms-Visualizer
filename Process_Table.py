import json
import pandas as pd
data = []
from tkinter import *
from pandastable import Table, TableModel

class TestApp(Frame):
    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('600x400+200+100')
        self.main.title('Process Table')
        f = Frame(self.main)
        f.pack(fill=BOTH,expand=1)
        with open('data.json', "r") as read_file:
            data = json.load(read_file)
        df=pd.DataFrame(data)
        self.table = pt = Table(f, dataframe=df,
                                showtoolbar=True, showstatusbar=False)
        pt.show()
        return
def sec_main():
    app = TestApp()
    app.mainloop()
if __name__ == "__main__":
#     app = TestApp()
# #launch the app
#     app.mainloop()
    sec_main()

