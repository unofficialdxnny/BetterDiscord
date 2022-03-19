## Merge linux and windows script togather.

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
RPC.update(state="Beta", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

    
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

kb.press("F11")
os.system("cls")
print(banner)



import winsound
winsound.PlaySound("moosiq.wav", winsound.SND_ASYNC | winsound.SND_ALIAS | winsound.SND_LOOP + winsound.SND_ASYNC)

 
 
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


while True:
    RPC.update(state="Main Menu", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)


    
    os.system("cls")
    print(banner)
    print("")
    print("\033[93m")
    print(MM)
    
    
    opt = int(input("Select an option : "))
    
    if opt == 1:
        RPC.update(state="Creating Theme", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
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
        

        RPC.update(state="Just created " + name + ".css", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

    
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
        RPC.update(state="Workspace: " + name + ".css", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

        print("")
        print("")
        
        print("\033[93m" + name + ".css File has been created  ")

        time.sleep(3)

        print("")
        print("Importing Necaserry Libraries... ")

        time.sleep(3)

        os.system("cls")
        print(banner)


        print("")

        author = input('What would you like to be called as the author of this Theme : ')  

        version = input('What is this themes version : ')

        description = input('Give your theme a nice description : ')

        source = input('Paste the source code link here (leave empty if none) : ')

        website = input('Link your website here (leave empty if none) : ')

        invite = input('Add your discord server invite code here (leave empty if none) : ')


        with open(name + '.css', 'a') as f:
            f.write(f"""
            
/**
 * @name {author}
 * @version {version}
 * @description {description}
 * @source {source}
 * @website {website}
 * @invite {invite}
 */

@import url(https://clearvision.gitlab.io/v6/main.css);



	/* ACCENT COLORS */
	--main-color: {maincolour}; /* main accent color (hex, rgb or hsl) [default: #2780e6] */
	--hover-color: {hovercolour}; /* hover accent color (hex, rgb or hsl) [default: #1e63b3] */
	--success-color: #{successcolour}; /* success accent color (hex, rgb or hsl) [default: #43b581] */
	--danger-color: #{dangercolour}; /* danger accent color (hex, rgb or hsl) [default: #982929] */	
	--url-color: #({urlcolour}); /*The color of url links [default: var(--main-color)]*/

	/* STATUS COLORS */
	--online-color: #{onlinecolour}; /* online status color (hex, rgb or hsl) [default: #43b581] */
	--idle-color: #{idlecolour}; /* idle status color (hex, rgb or hsl) [default: #faa61a] */
	--dnd-color: #{dndcolour}; /* dnd status color (hex, rgb or hsl) [default: #982929] */
	--streaming-color: #{streamingcolour}; /* streaming status color (hex, rgb or hsl) [default: #593695] */
	--offline-color: #{offlinecolour}; /* offline/invisible status color (hex, rgb or hsl) [default: #808080] */

	/* GENERAL */
	--main-font: Whitney, Helvetica Neue, Helvetica, Arial, sans-serif; /* main font for app (font must be installed) [default: Whitney, Helvetica Neue, Helvetica, Arial, sans-serif] */
	--code-font: Consolas, Liberation Mono, Menlo, Courier, monospace; /* font for codeblocks (font must be installed) [default: Consolas, Liberation Mono, Menlo, Courier, monospace] */
	--text-normal: #{normaltext}; /* color of default discord text */
	--text-muted:  #{textmuted}; /* color of default discord muted text (e.g.text found in input fields before typing).*/
	--channels-width: {channelwidth}px; /* channel list width (240px for Discord default) [default: 220px] */
	--members-width: {memberswidth}px; /* member list width [default: 240px] */

	/* APP BACKGROUND */
	--background-shading: {bgshading}%; /* app background shading (0 for complete smoothness) [default: 100%] */
	--background-overlay: {bgoverlay}; /* app background overlay color/gradient [default: rgba(0, 0, 0, 0.6)] */
	--background-image: url({bgimage}); /* app background image (link must be HTTPS) [default: url(https://clearvision.gitlab.io/images/sapphire.jpg)]*/
	--background-position: {bgposition}; /* app background position [default: center] */
	--background-size: {bgsize}; /* app background size [default: cover] */
	--background-repeat: {bgrepeat}; /* app background repeat [default: no-repeat] */
	--background-attachment: {bgattachment}; /* app background attachment [default: fixed] */
	--background-brightness: {bgbrightness}%; /* app background brightness (< 100% for darken, > 100% for lighten) [default: 100%] */
	--background-contrast: {bgcontrast}%; /* app background contrast [default: 100%] */
	--background-saturation: {bgsaturation}%; /* app background saturation [default: 100%] */
	--background-invert: {bginvert}%; /* app background invert (0 - 100%)  [default: 0%] */
	--background-grayscale: {bggrayscale}%; /* app background grayscale ( 0 - 100%) [default: 0%] */
	--background-sepia: {bgsepia}%; /* app background sepia (0 - 100%) [default: 0%] */
	--background-blur: {bgblur}px; /* app background blur [default: 0px] */
	
	/* HOME BUTTON ICON */
	--home-icon: url(https://clearvision.gitlab.io/icons/discord.svg); /* home button icon (link must be HTTPS) [default: url(https://clearvision.gitlab.io/icons/discord.svg)]*/
	--home-position: center; /* home button icon position [default: center] */
	--home-size: 40px; /* home button icon size [default: 40px] */
		
	/* CHANNEL COLORS */
	--channel-unread: var(--main-color); /* Unread Server channel color. [default:  var(--main-color)] THIS OVERRIDES YOUR MAIN COLOR*/
	--channel-color:  rgba(255,255,255,0.3); /*Read Server channel color  [default: rgba(255,255,255,0.3);]*/
	--channel-text-selected: #fff; /* Selected channel text color, CV default is #fff */
	--muted-color: rgba(255,255,255,0.1); /*Muted channel color  [default: rgba(255,255,255,0.1);]*/
	
	/* MODAL BACKDROP */
	--backdrop-overlay: rgba(0, 0, 0, 0.8); /* modal backdrop overlay color/gradient [default: rgba(0, 0, 0, 0.8)] */
	--backdrop-image: var(--background-image); /* modal backdrop image (link must be HTTPS) [default: var(--background-image)] */
	--backdrop-position: var(--background-position); /* modal backdrop position [default: var(--background-position)] */
	--backdrop-size: var(--background-size); /* modal backdrop size [default: var(--background-size)] */
	--backdrop-repeat: var(--background-repeat); /* modal backdrop repeat [default: var(--background-repeat)] */
	--backdrop-attachment: var(--background-attachment); /* modal backdrop attachment [default: var(--background-attachment)] */
	--backdrop-brightness: var(--background-brightness); /* modal backdrop brightness (< 100% for darken, > 100% for lighten) [default: var(--background-brightness)] */
	--backdrop-contrast: var(--background-contrast); /* modal backdrop contrast [default: var(--background-contrast)] */
	--backdrop-saturation: var(--background-saturation); /* modal backdrop saturation [default: var(--background-saturation)] */
	--backdrop-invert: var(--background-invert); /* modal backdrop invert (0 - 100%)  [default: var(--background-invert)] */
	--backdrop-grayscale: var(--background-grayscale); /* modal backdrop grayscale ( 0 - 100%) [default: var(--background-grayscale)] */
	--backdrop-sepia: var(--background-sepia); /* modal backdrop sepia (0 - 100%) [default: var(--background-sepia)] */
	--backdrop-blur: var(--background-blur); /* modal backdrop blur [default: var(--background-blur)] */
	
	/* USER POPOUT BACKGROUND */
	--user-popout-image: var(--background-image); /* app background image (link must be HTTPS) [default: var(--background-image)] */
	--user-popout-position: var(--background-position); /* user popout background position [default: var(--background-position)] */
	--user-popout-size: var(--background-size); /* user popout background size [default: var(--background-size)] */
	--user-popout-repeat: var(--background-repeat); /* user popout background repeat [default: var(--background-repeat)] */
	--user-popout-attachment: var(--background-attachment); /* user popout background attachment [default: var(--background-attachment)] */
	--user-popout-brightness: var(--background-brightness); /* user popout background brightness (< 100% for darken, > 100% for lighten) [default: var(--background-brightness)] */
	--user-popout-contrast: var(--background-contrast); /* user popout background contrast [default: var(--background-contrast)] */
	--user-popout-saturation: var(--background-saturation); /* user popout background saturation [default: var(--background-saturation)] */
	--user-popout-invert: var(--background-invert); /* user popout background invert (0 - 100%) [default: var(--background-invert)] */
	--user-popout-grayscale: var(--background-grayscale); /* user popout background grayscale (0 - 100%) [default: var(--background-grayscale)] */
	--user-popout-sepia: var(--background-sepia); /* user popout background sepia (0 - 100%) [default: var(--background-sepia)] */
	--user-popout-blur: calc(var(--background-blur) + 3px); /* user popout background blur [default: calc(var(--background-blur) + 3px)] */
	--user-popout-overlay: rgba(0, 0, 0, .6); /* user popout overlay color [default: rgba(0, 0, 0, .6)] */
	
	/* USER MODAL BACKGROUND */
	--user-modal-image: var(--background-image); /* app background image (link must be HTTPS) [default: var(--background-image)] */
	--user-modal-position: var(--background-position); /* user modal background position [default: var(--background-position)] */
	--user-modal-size: var(--background-size); /* user modal background size [default: var(--background-size)] */
	--user-modal-repeat: var(--background-repeat); /* user modal background repeat [default: var(--background-repeat)] */
	--user-modal-attachment: var(--background-attachment); /* user modal background attachment [default: var(--background-attachment)] */
	--user-modal-brightness: var(--background-brightness); /* user modal background brightness (< 100% for darken, > 100% for lighten) [default: var(--background-brightness)] */
	--user-modal-contrast: var(--background-contrast); /* user modal background contrast [default: var(--background-contrast)] */
	--user-modal-saturation: var(--background-saturation); /* user modal background saturation [default: var(--background-saturation)] */
	--user-modal-invert: var(--background-invert); /* user modal background invert (0 - 100%) [default: var(--background-invert)] */
	--user-modal-grayscale: var(--background-grayscale); /* user modal background grayscale (0 - 100%) [default: var(--background-grayscale)] */
	--user-modal-sepia: var(--background-sepia); /* user modal background sepia (0 - 100%) [default: var(--background-sepia)] */
	--user-modal-blur: calc(var(--background-blur) + 3px); /* user modal background blur [default: calc(var(--background-blur) + 3px)] */
	
	/* THEME BD COLORS */
	--bd-blue: var(--main-color); /* betterdiscord main color [default: var(--main-color)] */
	--bd-blue-hover: var(--hover-color); /* betterdiscord hover color [default: var(--hover-color)] */
	--bd-blue-active: var(--hover-color); /* betterdiscord active color [default: var(--hover-color)] */


            """)
        




      


        time.sleep(5)
        
    elif opt == 2:
        RPC.update(state="Setting Up", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
        wb.open("https://betterdiscord.app")

        
        
        input("Press Enter to continue...")
   
        
    elif opt == 3:
        RPC.update(state="Watching Tutorial", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
        tutorial = "https://github.com"
        wb.open(tutorial)
        input("press enter to continue...")



    
        
    elif opt == 4:
        RPC.update(state="Contributers", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

        os.system("cls")
        print(banner)
        print("")
        print("#  Name              Roles")
        print("")
        print("1. unofficialdxnny - Owner")
        print("2. Dx_Deathstrike - Gfx")
        print("3. pain hours - Music")

        print("")


        visit = int(input("Please Type in the number of the user whom you'd like to visit : "))

        if visit == 1:
          RPC.update(state="Visiting unofficialdxnny", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
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
            RPC.update(state="Visiting unofficialdxnny", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
            wb.open("https://instagram.com/unofficialdxnny")
            input("press enter to continue...")
          elif opt == 2:
            RPC.update(state="Visiting unofficialdxnny", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
            wb.open("https://github.com/unofficialdxnny")
            input("press enter to continue...")

          elif opt == 3:
            RPC.update(state="Visiting unofficialdxnny", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
            wb.open("https://www.youtube.com/channel/UCCP1p4ZG5KmLnnJhIm0KEXg")
            input("press enter to continue...")

          elif opt == 4:
            RPC.update(state="Visiting unofficialdxnny", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
            wb.open("https://instagram.com/unofficialdxnny")
            wb.open("https://github.com/unofficialdxnny")
            wb.open("https://www.youtube.com/channel/UCCP1p4ZG5KmLnnJhIm0KEXg")
            wb.open("https://www.youtube.com/channel/UCCP1p4ZG5KmLnnJhIm0KEXg")

            
          
            input("press enter to continue...")

            
        
        if visit == 2:
          RPC.update(state="Visiting Dx_Deathstrike", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

          os.system("cls")
          print(banner)
          print("")
          print("1. Instagram")
          print("2. Back")
          print("")
          opt = int(input("Select an options : "))
          if opt == 1:
            RPC.update(state="Visiting Dx_Deathstrike", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

            wb.open("https://instagram.com/Dx_Deathstrike")
            input("press enter to continue...")

        if visit == 3:
          RPC.update(state="Listening to pain hours", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

          wb.open("https://www.youtube.com/watch?v=YIkuLXr-UTY&ab_channel=painhours")

          input("Press enter to continue...")





    elif opt != [1, 2, 3, 4]:
        RPC.update(state="He cant read", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", large_text="Logo By Dx_Deathstrike", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

        import getpass
        import time
        os.system("cls")
        
        name = getpass.getuser()
        print("Pick a number between 1 and 4 " +  name )

        print("")

      
        print(eyes)
        
        input("Press enter to continue...")        
	
 
    
    
