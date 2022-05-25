## Merge linux and windows script togather.

import os 
import time 
import keyboard as kb
import webbrowser as wb
import sys
import pyautogui as pag
import win32gui, win32con
import getpass


from pypresence import Presence
import time

client_id = '947150788466200586'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

start_time=time.time() 
RPC.update(state="Loading", details="By unofficialdxnny", large_image="https://preview.redd.it/jv3uniz52vo51.gif?format=png8&s=9a4b9d2674e3ef51640097e11dcb59e979427a46", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

    
from win10toast import ToastNotifier
  
n = ToastNotifier()
  
n.show_toast("BetterDiscord - unofficialdxnny", 
"BetterDiscord is a terminal interface where you can make Discord themes quickly with no prior CSS knowledge", duration = 3 )

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


hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

os.system("cls")
print(banner)

import playsound
playsound.playsound('moosiq.mp3', False)

os.system("cls")
print(banner)

#import winsound
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
                                      .,,cccd$$$$$$$$$$$ccc,
                                    ,cc$$$$$$$$$$$$$$$$$$$$$$$$$cc,
                                  ,d$$$$$$$$$$$$$$$$"J$$$$$$$$$$$$$$c,
                                d$$$$$$$$$$$$$$$$$$,$" ,,`?$$$$$$$$$$$$L
                              ,$$$$$$$$$$$$$$$$$$$$$',J$$$$$$$$$$$$$$$$$b
                             ,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i `$h
                             $$$$$$$$$$$$$$$$$$$$$$$$$P'  "$$$$$$$$$$$h $$
                            ;$$$$$$$$$$$$$$$$$$$$$$$$F,$$$h,?$$$$$$$$$$h$F
                            `$$$$$$$$$$$$$$$$$$$$$$$F:??$$$:)$$$$P",. $$F
                             ?$$$$$$$$$$$$$$$$$$$$$$(   `$$ J$$F"d$$F,$F
                              ?$$$$$$$$$$$$$$$$$$$$$h,  :P'J$$F  ,$F,$"
                               ?$$$$$$$$$$$$$$$$$$$$$$$ccd$$`$h, ",d$
                                "$$$$$$$$$$$$$$$$$$$$$$$$",cdc $$$$"
                       ,uu,      `?$$$$$$$$$$$$$$$$$$$$$$$$$$$c$$$$h
                   .,d$$$$$$$cc,   `$$$$$$$$$$$$$$$$??$$$$$$$$$$$$$$$,
                 ,d$$$$$$$$$$$$$$$bcccc,,??$$$$$$ccf `"??$$$$??$$$$$$$
                d$$$$$$$$$$$$$$$$$$$$$$$$$h`?$$$$$$h`:...  d$$$$$$$$P
               d$$$$$$$$$$$$$$$$$$$$$$$$$$$$`$$$$$$$hc,,cd$$$$$$$$P"
           =$$?$$$$$$$$P' ?$$$$$$$$$$$$$$$$$;$$$$$$$$$???????",,
              =$$$$$$F       `"?????$$$$$$$$$$$$$$$$$$$$$$$$$$$$$bc
              d$$F"?$$k ,ccc$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i
       .     ,ccc$$c`""u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P",$$$$$$$$$$$$h
    ,d$$$L  J$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" `""$$$??$$$$$$$
  ,d$$$$$$c,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F       `?J$$$$$$$'
 ,$$$$$$$$$$h`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F           ?$$$$$$$P""=,
,$$$F?$$$$$$$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F              3$$$$II"?$h,
$$$$$`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P"               ;$$$??$$$,"?"
$$$$F ?$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P",z'                3$$h   ?$F
       `?$$$$$$$$$$$$$$$??$$$$$$$$$PF"',d$P"                  "?$F
          """""""         ,z$$$$$$$$$$$$$P
                         J$$$$$$$$$$$$$$F
                        ,$$$$$$$$$$$$$$F
                        :$$$$$c?$$$$PF'
                        `$$$$$$$P
                         `?$$$$F
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

username = getpass.getuser()

while True:
    RPC.update(state="Main Menu", details="By unofficialdxnny", large_image="https://preview.redd.it/jv3uniz52vo51.gif?format=png8&s=9a4b9d2674e3ef51640097e11dcb59e979427a46", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)


    
    os.system("cls")
    print(banner)
    print("")
    print("\033[93m")
    print(MM)
    
    
    opt = int(input("Select an option : "))
    
    if opt == 1:
        RPC.update(state="Creating Theme", details="By unofficialdxnny", large_image="https://preview.redd.it/jv3uniz52vo51.gif?format=png8&s=9a4b9d2674e3ef51640097e11dcb59e979427a46", large_text="Editing a CSS3 file", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
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

          "   When the program is finished you will have a .theme.css file with your discord theme in " + cwd)
          

        print('')
        
       

        print("")

        def print_slow(str):
            for char in str:
              time.sleep(.1)
              sys.stdout.write(char)
              sys.stdout.flush()
        print("")
        print_slow('If you want help with hex code than please type -hex otherwise press enter')
        print("")

        hexhelp = input(' : ')

        if hexhelp == '-hex':
          wb.open('https://htmlcolorcodes.com/')






        print("")



        name = input("Name your theme : ")
        

        RPC.update(state="Just created " + name + ".theme.theme.css", details="By unofficialdxnny", large_image="https://www.w3.org/html/logo/img/class-header-css3.jpg", small_image="https://preview.redd.it/jv3uniz52vo51.gif?format=png8&s=9a4b9d2674e3ef51640097e11dcb59e979427a46", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

    
        import sys
        import time

        def print_slow(str):
            for char in str:
              time.sleep(.1)
              sys.stdout.write(char)
              sys.stdout.flush()
        print("")
        print_slow('\033[91m  I will guide you through the steps below and give you all possible options')

        os.system("cls")
        print(banner)
        
        print("")
        RPC.update(state="Workspace: " + name + ".theme.css", details="By unofficialdxnny", large_image="https://www.w3.org/html/logo/img/class-header-css3.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

        print("")
        print("")
        
        print("\033[93m" + name + ".theme.css File has been created  ")

        time.sleep(3)

        print("")
        print("Importing Necaserry Libraries... ")

        time.sleep(3)

        os.system("cls")
        print(banner)


        print("")

        author = input('What would you like to be called as the author of this Theme : ')  
        print("")

        version = input('What is this themes version : ')
        print("")

        description = input('Give your theme a nice description : ')
        print("")

        source = input('Paste the source code link here (leave empty if none) : ')
        print("")

        website = input('Link your website here (leave empty if none) : ')
        print("")

        invite = input('Add your discord server invite code here (leave empty if none) : ')
        print("")

        maincolour = input('Please type in the main colour of your client in hex without the # : ')
        print("")

        hovercolour = input('Please type in the hover colour of your client in hex without the # : ')
        print("")

        successcolour = input('Please type in the success colour of your client in hex without the # : ')
        print("")

        dangercolour = input('Please type in the danger colour of your client in hex without the # : ')
        print("")

        urlcolour = input('Please type in the url colour of your client in hex without the # : ')
        print("")

        onlinecolour = input('Please type in the colour for online user in hex without the # : ')
        print("")

        idlecolour = input('Please type in the colour for idle user in hex without the # : ')
        print("")

        dndcolour = input('Please type in the colour for dnd user in hex without the # : ')
        print("")

        streamingcolour = input('Please type in the colour for streaming user in hex without the # : ')
        print("")

        offlinecolour = input('Please type in the colour for offline user in hex without the # : ')
        print("")

        normaltext = input('Please type in the colour for normal text in hex without the # : ')
        print("")

        textmuted = input('Please type in the colour for muted text in hex without the # : ')
        print("")

        channelwidth = input('Please type in the size number for channel width without the px [default: 220px] : ')
        print("")

        memberswidth = input('Please type in the size number for members width without the px [default: 240px] : ')
        print("")

        bgshading = input('Please type in the number for background shading without the % [default: 100%] : ')
        print("")

        bgoverlay = input('Please type in the hex colour for background gradient without the # : ')
        print("")

        bgimage = input('Please paste the link to your desired image for the background : ')
        print("")

        bgposition = input('Please type in the bg position [default: center] : ')
        print("")

        bgsize = input('Please type in the background size [default: cover] : ')
        print("")

        bgrepeat = input('Type repeat or no-repeat here for a bgrepeat or not [default: no-repeat] : ')
        print("")

        bgcontrast = input('Type in a number between 0 - 100 for bg contrast without the % [default: 100%] : ')
        print("")

        bgsaturation = input('Type in a number between 0 - 100 for bg saturation without the % [default: 100%] : ')
        print("")

        bginvert = input('Type in a number between 0 - 100 according to how much you want to invert your background without % [default: 0%] : ')
        print("")

        bggrayscale = input('Type in a number between 0 - 100 according to how much grayscale you want your background to have without % [default: 0%] : ')
        print("")

        bgsepia = input('Type in a number between 0 - 100 according to how much sepia you want without % [default: 0%] : ')
        print("")

        bgblur = input('Type in a number between 0 - 100 according to how much blur you want your background to have without % [default: 0px] : ')
        print("")

        homeicon = input('Include a https link for your image you would like to use for the home button : ')
        print("")

        homeposition = input('home button icon position [default: center] : ')
        print("")

        homesize = input('Type in the number for home size without px [default: 40px] : ')
        print("")

        channelunread = input('Please type in the hex colour for unread channel without the # : ')
        print("")

        channelcolor = input('Please type in the hex colour for readchannel without the # : ')
        print("")

        channeltextselected = input('Please type in the hex colour for curren channel without the # : ')
        print("")

        mutedcolor = input('Please type in the hex colour for mutedchannel without the # : ')
        print("")

        
        

        

        with open(f'C:/Users/{username}/AppData/Roaming/BetterDiscord/themes/{name} + '.theme.css', 'a') as f:
            f.write(f"""/**
 * @name {author}
 * @version {version}
 * @description {description}
 * @source {source}
 * @website {website}
 * @invite {invite}
 */

  @import url('https://unofficialdxnny.github.io/main.css');



  
  """ 
  
  
  """

	/* ACCENT COLORS */

:root{
  --main-color: #""" + maincolour +"""; 
	--hover-color: #""" + hovercolour +""";
	--success-color: #""" + successcolour +"""; 
	--danger-color: #""" + dangercolour +""";
	--url-color: #(""" + urlcolour + """); 

	/* STATUS COLORS */
	--online-color: #""" + onlinecolour +"""; 
	--idle-color: #""" + idlecolour +"""; 
	--dnd-color: #""" + dndcolour + """; 
	--streaming-color: #""" + streamingcolour + """; 
	--offline-color: #""" + offlinecolour + """; 

	/* GENERAL */
	--main-font: Whitney, Helvetica Neue, Helvetica, Arial, sans-serif; 
	--code-font: Consolas, Liberation Mono, Menlo, Courier, monospace; 
	--text-normal: #""" + normaltext + """; 
	--text-muted:  #""" + textmuted + """; 
	--channels-width: """ + channelwidth + """px; 
	--members-width: """ + memberswidth +"""px; 

	/* APP BACKGROUND */
	--background-shading: """ + bgshading +"""%; 
	--background-overlay: #""" + bgoverlay +"""; 
	--background-image: url(""" + bgimage +"""); 
	--background-position: """ + bgposition +"""; 
	--background-size: """ + bgsize +"""; 
	--background-repeat: """ + bgrepeat +"""; 
	--background-attachment: fixed; 
	--background-brightness: 100%;
	--background-contrast: """ + bgcontrast +"""%;
	--background-saturation: """ + bgsaturation +"""%;
	--background-invert: """ + bginvert +"""%; 
	--background-grayscale: """ + bggrayscale +"""%;
	--background-sepia: """ + bgsepia +"""%;
	--background-blur: """ + bgblur +"""px;
	
	/* HOME BUTTON ICON */
	--home-icon: url(""" + homeicon +"""); 
	--home-position: """ + homeposition +""";
	--home-size: """ + homesize +"""px;
		
	/* CHANNEL COLORS */
	--channel-unread: #""" + channelunread +"""; 
	--channel-color:  #""" + channelcolor +"""; 
	--channel-text-selected: #""" + channeltextselected +"""; 
	--muted-color: #""" + mutedcolor +""";}



            """)

        
        
    elif opt == 2:
        RPC.update(state="Setting Up", details="By unofficialdxnny", large_image="https://preview.redd.it/jv3uniz52vo51.gif?format=png8&s=9a4b9d2674e3ef51640097e11dcb59e979427a46", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
        os.system('choco install betterdiscord')

        
        
        input("Press Enter to continue...")
   
        
    elif opt == 3:
        RPC.update(state="Watching Tutorial", details="By unofficialdxnny", large_image="https://preview.redd.it/jv3uniz52vo51.gif?format=png8&s=9a4b9d2674e3ef51640097e11dcb59e979427a46", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
        tutorial = "https://www.instagram.com/p/CbvCryajTSQ/"
        wb.open(tutorial)
        input("press enter to continue...")



    
        
    elif opt == 4:
        RPC.update(state="Contributers", details="By unofficialdxnny", large_image="https://preview.redd.it/jv3uniz52vo51.gif?format=png8&s=9a4b9d2674e3ef51640097e11dcb59e979427a46", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

        os.system("cls")
        print(banner)
        print("")
        print("#  Name              Roles")
        print("")
        print("1. unofficialdxnny - Owner")
        print("2. Dx_Deathstrike - Gfx")
        print("3. pain hours - Music")
        print("4. patorjk - Asscii Art")

        print("")


        visit = int(input("Please Type in the number of the user whom you'd like to visit : "))

        if visit == 1:
          RPC.update(state="Visiting unofficialdxnny", details="By unofficialdxnny", large_image="https://preview.redd.it/jv3uniz52vo51.gif?format=png8&s=9a4b9d2674e3ef51640097e11dcb59e979427a46", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
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
            RPC.update(state="Visiting unofficialdxnny", details="By unofficialdxnny", large_image="https://preview.redd.it/jv3uniz52vo51.gif?format=png8&s=9a4b9d2674e3ef51640097e11dcb59e979427a46", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
            wb.open("https://instagram.com/unofficialdxnny")
            input("press enter to continue...")
          elif opt == 2:
            RPC.update(state="Visiting unofficialdxnny", details="By unofficialdxnny", large_image="https://preview.redd.it/jv3uniz52vo51.gif?format=png8&s=9a4b9d2674e3ef51640097e11dcb59e979427a46", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
            wb.open("https://github.com/unofficialdxnny")
            input("press enter to continue...")

          elif opt == 3:
            RPC.update(state="Visiting unofficialdxnny", details="By unofficialdxnny", large_image="https://preview.redd.it/jv3uniz52vo51.gif?format=png8&s=9a4b9d2674e3ef51640097e11dcb59e979427a46", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
            wb.open("https://www.youtube.com/channel/UCCP1p4ZG5KmLnnJhIm0KEXg")
            input("press enter to continue...")

          elif opt == 4:
            RPC.update(state="Visiting unofficialdxnny", details="By unofficialdxnny", large_image="https://preview.redd.it/jv3uniz52vo51.gif?format=png8&s=9a4b9d2674e3ef51640097e11dcb59e979427a46", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
            wb.open("https://instagram.com/unofficialdxnny")
            wb.open("https://github.com/unofficialdxnny")
            wb.open("https://www.youtube.com/channel/UCCP1p4ZG5KmLnnJhIm0KEXg")
            wb.open("https://www.youtube.com/channel/UCCP1p4ZG5KmLnnJhIm0KEXg")

            
          
            input("press enter to continue...")

            
        
        if visit == 2:
          RPC.update(state="Visiting Dx_Deathstrike", details="By unofficialdxnny", large_image="https://preview.redd.it/jv3uniz52vo51.gif?format=png8&s=9a4b9d2674e3ef51640097e11dcb59e979427a46", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

          os.system("cls")
          print(banner)
          print("")
          print("1. Instagram")
          print("2. Back")
          print("")
          opt = int(input("Select an options : "))
          if opt == 1:
            RPC.update(state="Visiting Dx_Deathstrike", details="By unofficialdxnny", large_image="https://preview.redd.it/jv3uniz52vo51.gif?format=png8&s=9a4b9d2674e3ef51640097e11dcb59e979427a46", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

            wb.open("https://instagram.com/Dx_Deathstrike")
            input("press enter to continue...")

        if visit == 3:
          RPC.update(state="Listening to pain hours", details="By unofficialdxnny", large_image="https://preview.redd.it/jv3uniz52vo51.gif?format=png8&s=9a4b9d2674e3ef51640097e11dcb59e979427a46", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

          wb.open("https://www.youtube.com/watch?v=YIkuLXr-UTY&ab_channel=painhours")

          input("Press enter to continue...")

        if visit == 4:
          RPC.update(state="Viewing Asscii Art", details="By unofficialdxnny", large_image="https://preview.redd.it/jv3uniz52vo51.gif?format=png8&s=9a4b9d2674e3ef51640097e11dcb59e979427a46", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

          wb.open("https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20")

          input("Press enter to continue...")
          
       




    elif opt != [1, 2, 3, 4]:
        RPC.update(state="He cant read", details="By unofficialdxnny", large_image="https://preview.redd.it/jv3uniz52vo51.gif?format=png8&s=9a4b9d2674e3ef51640097e11dcb59e979427a46", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

        import getpass
        import time
        os.system("cls")
        
        name = getpass.getuser()
        print("Pick a number between 1 and 4 " +  name )

        print("")

      
        print(eyes)
        
        input("Press enter to continue...")        
	
 

	
    
