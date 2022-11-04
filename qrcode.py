import os, sys, random, time
os.system("pip install pypng")
os.system("pip install pyqrcode")
class Color:
    black = "\033[0;30m"
    red = "\033[0;31m"
    green = "\033[0;32m"
    brown = "\033[0;33m"
    blue = "\033[0;34m"
    purple = "\033[0;35m"
    cyan = "\033[0;36m"
    light_gray = "\033[0;37m"
    dark_gray = "\033[1;30m"
    light_red = "\033[1;31m"
    light_green = "\033[1;32m"
    yellow = "\033[1;33m"
    light_blue = "\033[1;34m"
    light_purple = "\033[1;35m"
    light_cyan = "\033[1;36m"
    light_white = "\033[1;37m"
    bold = "\033[1m"
    faint = "\033[2m"
    italic = "\033[3m"
    underline = "\033[4m"
    blink = "\033[5m"
    negative = "\033[7m"
    crossed = "\033[9m"

class Main():
    def __init__(self):
        self.main()
    
    def main(self):
        os.system("clear")
        self.print_logo()
        print(Color.yellow + "Choose an option:")
        print("\t1 . Make a QR Code")
        print("\t99. Exit/Quit")
        
        option_select = input("\n  >> Select:  " + Color.light_white)
        
        if option_select == "1":
            self.qr_make()
        
        elif option_select == "99":
            print("Thanks for using this tool.")
            sys.exit()
        else:
            print(Color.red + " Wrong Input. Please select again...")
            time.sleep(3)
            self.main()
    
    def qr_make(self):
        import pyqrcode
        import png
        from pyqrcode import QRCode
        qrcode_text = input(Color.yellow + "  Enter Text:  " + Color.light_white)
        pyqrcode.create(qrcode_text).png("MyQR" + str(self.generate_key()) + ".png", scale = 6)
        print(Color.yellow + "  QR Code Generate Successfully")
        input(" Press enter to continue. ")
        self.main()

    def generate_key(self):
        return random.randint(100000,999999)

    def print_logo(self):
        print(Color.light_blue)
        print("""###########################################
  __  __    ___        _______ ___ ___ 
 |  \/  |  / \ \      / /  ___|_ _|_ _|
 | |\/| | / _ \ \ /\ / /| |_   | | | | 
 | |  | |/ ___ \ V  V / |  _|  | | | | 
 |_|  |_/_/   \_\_/\_/  |_|   |___|___|"""+Color.yellow+ """ v1.0"""+Color.light_blue+""" 
############################################""")
        print(Color.light_white + "Mawfi Islam")
        print()
    

Main()
