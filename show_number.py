from gpiozero import LED

class Show_Number:
    def __init__(self, sega_pin, segb_pin, segc_pin, segd_pin, sege_pin, segf_pin, segg_pin):
        self.sega = LED(sega_pin)
        self.segb = LED(segb_pin)
        self.segc = LED(segc_pin)
        self.segd = LED(segd_pin)
        self.sege = LED(sege_pin)
        self.segf = LED(segf_pin)
        self.segg = LED(segg_pin)
     
    def show_number(self, number):
        if number == 0:
            self.sega.off()
            self.segb.off()
            self.segc.off()
            self.segd.off()
            self.sege.off()
            self.segf.on()
            self.segg.off()
        elif number == 1:
            self.sega.on()
            self.segb.off()
            self.segc.off()
            self.segd.on()
            self.sege.on()
            self.segf.on()
            self.segg.on()
        
        elif number == 2:
            self.sega.off()
            self.segb.off()
            self.segc.on()
            self.segd.off()
            self.sege.off()
            self.segf.off()
            self.segg.on()
        
        elif number == 3:
            self.sega.off()
            self.segb.off()
            self.segc.off()
            self.segd.off()
            self.sege.on()
            self.segf.off()
            self.segg.on()
        
        elif number == 4:
            self.sega.on()
            self.segb.off()
            self.segc.off()
            self.segd.on()
            self.sege.on()
            self.segf.off()
            self.segg.off()
        
        elif number == 5:
            self.sega.off()
            self.segb.on()
            self.segc.off()
            self.segd.off()
            self.sege.on()
            self.segf.off()
            self.segg.off()
        
        elif number == 6:
            self.sega.off()
            self.segb.on()
            self.segc.off()
            self.segd.off()
            self.sege.off()
            self.segf.off()
            self.segg.off()
        
        elif number == 7:
            self.sega.off()
            self.segb.off()
            self.segc.off()
            self.segd.on()
            self.sege.on()
            self.segf.on()
            self.segg.on()
        
        elif number == 8:
            self.sega.off()
            self.segb.off()
            self.segc.off()
            self.segd.off()
            self.sege.off()
            self.segf.off()
            self.segg.off()
        
        elif number == 9:
            self.sega.off()
            self.segb.off()
            self.segc.off()
            self.segd.off()
            self.sege.on()
            self.segf.off()
            self.segg.off()
        
        elif number == 10:
            self.sega.off()
            self.segb.off()
            self.segc.off()
            self.segd.on()
            self.sege.off()
            self.segf.off()
            self.segg.off()