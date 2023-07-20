import tkinter as tk
from system_alarm import Alam  
from show_number import Show_Number






class View(tk.Tk):
    def __init__(self):
        super().__init__()
        #self.alert = Alert(self) 
        
        
        self.al = Alam(11, 9, 10, 22, 27)  
        self.al.armer.when_pressed = self.al.lancement
        self.al.zone1.when_pressed = self.al.check_zone1
        self.al.zone2.when_pressed = self.al.check_zone2
        self.al.zone3.when_pressed = self.al.check_zone3
        self.al.zone4.when_pressed = self.al.check_zone4
        self.geometry("300x200")
        
        self.zone1 = tk.Label(self, text="zone1", fg="green", bg="#3CED75")
        self.zone1.place(x=20, y=30, width=120, height=25)
        self.zone1.bind("<Button-1>", self.on_zone1_clicked)
        
        self.zone2 = tk.Label(self, text="zone2", fg="green", bg="#3CED75")
        self.zone2.place(x=20, y=60, width=120, height=25)
        self.zone2.bind("<Button-1>", self.on_zone2_clicked)
        
        self.zone3 = tk.Label(self, text="zone3", fg="green", bg="#3CED75")
        self.zone3.place(x=20, y=90, width=120, height=25)
        self.zone3.bind("<Button-1>", self.on_zone3_clicked)
        
        self.zone4 = tk.Label(self, text="zone4", fg="green", bg="#3CED75")
        self.zone4.place(x=20, y=120, width=120, height=25)
        self.zone4.bind("<Button-1>", self.on_zone4_clicked)
        
        button1 = tk.Button(self, text="Activate", command=self.arm_system)
        button1.place(x=200, y=30, width=90, height=25)
        
        button2 = tk.Button(self, text="Deactivate", command=self.disarm_system)
        button2.place(x=200, y=70, width=90, height=25)
        
        button3 = tk.Button(self, text="Reset Alarm") 
        button3.place(x=200, y=100, width=90, height=25)
        
    def arm_system(self):
        self.al.arm_system()  
    def disarm_system(self):
        self.al.disarm_system()
    def on_zone1_clicked(self, event):
        self.al.check_zone1()
        #self.alert.stop_flag = False  #
        #self.alert.toggle_color()
    def on_zone2_clicked(self, event):
        self.al.check_zone2()
        #self.alert.stop_flag = False  
        #self.alert.toggle_color()
    def on_zone3_clicked(self, event):
        self.al.check_zone3()
        #self.alert.stop_flag = False  
        #self.alert.toggle_color()
    def on_zone4_clicked(self, event):
        self.al.check_zone4()
        #self.alert.stop_flag = False  t
        #self.alert.toggle_color()
root = View()
        #pull_up=True is_active=False
root.mainloop()

