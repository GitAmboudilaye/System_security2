from time import sleep
from gpiozero import LED, Button
from show_number import Show_Number 
#from view import View

"""class Alert():
    def __init__(self, root):
        self.root = root
        self.stop_flag = True  
        self.toggle_color()  
    
    def toggle_color(self):
        if not self.stop_flag:
            if self.root.zone1.cget("bg") == "#3CED75":
                self.root.zone1.config(bg="red")
            else:
                self.root.zone1.config(bg="#3CED75")
            self.root.after(500, self.toggle_color)

    
    def stop_clignotement(self):
        self.stop_flag = True
view = View()"""

class Alam:
    def __init__(self, zone1, zone2, zone3, zone4, armer):
        self.__zone1 = Button(zone1)
        self.__zone2 = Button(zone2)
        self.__zone3 = Button(zone3)
        self.__zone4 = Button(zone4)
        self.__armer = Button(armer)
        self.status = False
        self.show_numb = Show_Number(14, 15, 18, 23, 24, 25, 8)  
        #self.alert = Alert

    @property
    def armer(self):
        return self.__armer

    @armer.setter
    def zone1(self, armer):
        self.__armer = armer    
    @property
    def zone1(self):
        return self.__zone1

    @zone1.setter
    def zone1(self, zone1):
        self.__zone1 = zone1

    @property
    def zone2(self):
        return self.__zone2

    @zone2.setter
    def zone2(self, zone2):
        self.__zone2 = zone2

    @property
    def zone3(self):
        return self.__zone3

    @zone3.setter
    def zone3(self, zone3):
        self.__zone3 = zone3

    @property
    def zone4(self):
        return self.__zone4

    @zone4.setter
    def zone4(self, zone4):
        self.__zone4 = zone4

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    def arm_system(self):
        if self.status == False:
            for i in range(10):
                self.show_numb.show_number(i)
                sleep(0.5)  # Pause pendant 0.5 seconde
            self.show_numb.show_number(10)
            self.status = True

    def disarm_system(self):
        if self.status == True:
            for i in range(10, -1, -1):
                self.show_numb.show_number(i)
                sleep(0.5)  # Pause pendant 0.5 seconde
            self.show_numb.show_number(0)
            self.status = False
    def lancement(self):
        if self.status == False:
            self.arm_system()
        else:
            self.disarm_system()
    def check_zone1(self):
        if self.status == True and self.zone1.is_pressed:
            self.show_numb.show_number(1)
            self.alert.toggle_color
        elif self.status == True:
            self.show_numb.show_number(1)
    def check_zone2(self):
        if self.status == True and self.zone2.is_pressed:
            self.show_numb.show_number(2)
        elif self.status == True:
            self.show_numb.show_number(2)
    def check_zone3(self):
        if self.status == True and self.zone3.is_pressed:
            self.show_numb.show_number(3)
        elif self.status == True:
            self.show_numb.show_number(3)
    def check_zone4(self):
        if self.status == True and self.zone4.is_pressed:
            self.show_numb.show_number(4)
        elif self.status == True:
            self.show_numb.show_number(4)