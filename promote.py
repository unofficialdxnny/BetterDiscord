from pypresence import Presence
import time

client_id = '947150788466200586'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

start_time=time.time() 
RPC.update(state="Beta", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", buttons=[{"label": "Github Repository", "url": "https://github.com/unofficialdxnny/BetterDiscord"}, {"label": "Owner Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)

    