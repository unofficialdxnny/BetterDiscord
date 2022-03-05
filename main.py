import os 
import time 
import keyboard as kb
import webbrowser as wb
import sys




from pypresence import Presence
import time

client_id = '947150788466200586'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

start_time=time.time() 
RPC.update(state="Beta", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

    
from win10toast import ToastNotifier
  
# create an object to ToastNotifier class
n = ToastNotifier()
  
n.show_toast("BetterDiscord - unofficialdxnny", 
"About BetterDiscord is a terminal interface where you can make Discord themes quickly with no prior CSS knowledge", duration = 3 )

class bcolors:
    HEADER = '\033[32m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



banner = """
\033[96m                                                     ____       __  __            ____  _                          
\033[96m                                                    / __ )___  / /_/ /____  _____/ __ \(_)_______ By unofficialdxnny
\033[96m                                                   / __  / _ \/ __/ __/ _ \/ ___/ / / / / ___/ ___/ __ \/ ___/ __  / 
\033[96m                                                  / /_/ /  __/ /_/ /_/  __/ /  / /_/ / (__  ) /__/ /_/ / /  / /_/ /  
\033[96m                                                 /_____/\___/\__/\__/\___/_/  /_____/_/____/\___/\____/_/   \__,_/   
                                                        
                                                        The Only BetterDiscord Script To Make Custom Themes!
                                                                  
"""

kb.press("F11")
os.system("cls")
print(banner)



import winsound
# winsound.PlaySound("moosiq.wav", winsound.SND_ASYNC | winsound.SND_ALIAS | winsound.SND_LOOP + winsound.SND_ASYNC)

 
 
print("")
print("")


TF = """
1. Yes              2. No
"""

socials = """

1. Instagram

2. Github

3. Discord


"""

MM = """

1. Custom CSS Theme

2. Install BetterDiscord

3. Tutorial

4. Contributers

"""
eyes = """







             ..,,;;;;;;,,,,
       .,;'';;,..,;;;,,,,,.''';;,..
    ,,''                    '';;;;,;''
   ;'    ,;@@;'  ,@@;, @@, ';;;@@;,;';.
  ''  ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;;
     ;;@@@@@;    '''     .,,;;;@@@@@@@;;;
    ;;@@@@@@;           , ';;;@@@@@@@@;;;.
     '';@@@@@,.  ,   .   ',;;;@@@@@@;;;;;;
        .   '';;;;;;;;;,;;;;@@@@@;;' ,.:;'
          ''..,,     ''''    '  .,;'
               ''''''::''''''''
                                   ,;
                                  .;;
                                 ,;;;
                               ,;;;;:
                           ,;@@   .;
                           ;;@@'  ,;
                            ';;, ,;'

"""



import itertools
import threading
import time
import sys

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLaunching ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r     ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(5)
done = True


while True:
    RPC.update(state="Main Menu", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)


    
    os.system("cls")
    print(banner)
    print("")
    print("\033[93m")
    print(MM)
    
    
    opt = int(input("Select an option : "))
    
    if opt == 1:
        RPC.update(state="Creating Theme", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
        os.system("cls")
        print(banner)
        cwd = os.getcwd() 
        import sys
        import time

        def print_slow(str):
            for char in str:
              time.sleep(.1)
              sys.stdout.write(char)
              sys.stdout.flush()
        print("")
        print_slow('\033[91m Welcome To Designer! \n \n'

          "   When the program is finished you will have a .css file with your discord theme in ")

        print("'" + cwd + "'")

        print("")

        





        print("")

        name = input("Name your theme : ")
        

        RPC.update(state="Just created " + name + ".css", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

    
        import sys
        import time

        def print_slow(str):
            for char in str:
              time.sleep(.1)
              sys.stdout.write(char)
              sys.stdout.flush()
        print("")
        print_slow('\033[91m  I will guide you through the steps below and give you all possible options')
        
        print("")
        RPC.update(state="Workspace: " + name + ".css", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

        print("")
        print("")
        
        print("\033[93m" + name + ".css File has been created  ")

        time.sleep(3)

        print("")
        print("Importing Necaserry Libraries... ")

        print("")
        with open(name + '.css', 'a') as f:
            f.write("""
            
            
            
@import url('https://fonts.googleapis.com/css2?family=Karla:wght@400;500;600;700&display=swap');
@import url('https://mwittrien.github.io/BetterDiscordAddons/Themes/BlurpleRecolor/BlurpleRecolor.css');
@import url('https://discord-custom-covers.github.io/usrbg/dist/usrbg.css');

button {
	--accentcolor: var(--accent-alt);
}


/* Root Variables */

 :root {

            """)
        


         
        background = input("Enter your background image link with ('') at the start and the end (can be gif) : ")

        with open( name + ".css","a") as file:
            file.write(f"--background-image: url({background});"),

            print("")


        font = input("Enter font name : ")
            
        family = input("Enter the font family : ")
        
        file.write(f"--font-primary: {font}, {family};"),



        time.sleep(5)
        
    elif opt == 2:
        RPC.update(state="Setting Up", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
        wb.open("https://betterdiscord.app")

        
        
        input("Press Enter to continue...")
   
        
    elif opt == 3:
        RPC.update(state="Watching Tutorial", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
        tutorial = "https://github.com"
        wb.open(tutorial)
        input("press enter to continue...")



    
        
    elif opt == 4:
        RPC.update(state="Contributers", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

        os.system("cls")
        print(banner)
        print("")
        print("#  Name              Roles")
        print("")
        print("1. unofficialdxnny - Owner")
        print("2. Dx_Deathstrike - Gfx")

        print("")


        visit = int(input("Please Type in the number of the user whom you'd like to visit : "))

        if visit == 1:
          RPC.update(state="Visiting unofficialdxnny", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
          os.system("cls")
          print(banner)
          print("")
          print("1. Instagram")
          print("2. Github")
          print("3. Youtube")
          print("4. All")
          print("5. Back")
          print("")
          opt = int(input("Choose an option : "))
          if opt == 1:
            RPC.update(state="Visiting unofficialdxnny", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
            wb.open("https://instagram.com/unofficialdxnny")
            input("press enter to continue...")
          elif opt == 2:
            RPC.update(state="Visiting unofficialdxnny", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
            wb.open("https://github.com/unofficialdxnny")
            input("press enter to continue...")

          elif opt == 3:
            RPC.update(state="Visiting unofficialdxnny", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
            wb.open("https://www.youtube.com/channel/UCCP1p4ZG5KmLnnJhIm0KEXg")
            input("press enter to continue...")

          elif opt == 4:
            RPC.update(state="Visiting unofficialdxnny", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
            wb.open("https://instagram.com/unofficialdxnny")
            wb.open("https://github.com/unofficialdxnny")
            wb.open("https://www.youtube.com/channel/UCCP1p4ZG5KmLnnJhIm0KEXg")
            wb.open("https://www.youtube.com/channel/UCCP1p4ZG5KmLnnJhIm0KEXg")

            
          
            input("press enter to continue...")

            
        
        if visit == 2:
          RPC.update(state="Visiting Dx_Deathstrike", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

          os.system("cls")
          print(banner)
          print("")
          print("1. Instagram")
          print("2. Back")
          print("")
          opt = int(input("Select an options : "))
          if opt == 1:
            RPC.update(state="Visiting Dx_Deathstrike", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

            wb.open("https://instagram.com/Dx_Deathstrike")
            input("press enter to continue...")




        time.sleep(5)

    elif opt != [1, 2, 3, 4]:
        import getpass
        import time

        name = getpass.getuser()
        print("Pick a number between 1 and 4 " +  name )

        print("")

        print(eyes)
        
        time.sleep(3)
        
 
    
    