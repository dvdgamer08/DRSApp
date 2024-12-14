#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@                               ,@@@@@@@@@@@@@@@@@                          ,@@@@@@@@@@@@@@@@@@                                     @@(((((
#@@@@@@@&((@@@@                                    %@@@@@@@@@                                (@@@@@@@@.                                       @@((((((@
#@@@@@@@(((((@@@@                                     @@@@@@@                                  (@@@@                                        @@#(((((@@@
#@@@@@@@((((((&@@@,                                    @@@@@                                    ,@@                                        @@(((((@@@@@
#@@@@@@(((((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           @@@@          @@@@@@@@@@@@@@@@@@%        @@        (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@(((((((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@          @@@(         @@@@@@@@@@@@@@@@@&*         @@          %%%%%%%%%%%%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@
#@@@@@#((((((((((((&@@@@@@@@@@@@@@@@@@@@@@@@@@,         @@@                                     @@@@                                  &@@@@@@@@@@@@@@@@
#@@@@@(((((((((((((((@@@@@@@@@@@@@@@@@@@@@@@@@          @@&                                   %@@@@@@@                                  ,@@@@@@@@@@@@@@
#@@@@%(((((((((((((((((@@@@@@@@@@@@@@@@@@@@@@          &@@                                 &@@@@@@@@@@@@@#                                @@@@@@@@@@@@@
#@@@@(((((((((((((((((((#@@@@@@@@@@@@@@@@@@(          %@@@          @@@@@@@@@@           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        %@@@@@@@@@@@@
#@@@&(((((((((((((((((((((@@@@@@@@@@@@@/             @@@@          @@@@@@@@@@@@,           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         @@@@@@@@@@@@@
#@@@((((((((((((((((((((((((@@@@                   @@@@@@          @@@@@@@@@@@@@@           @@@@%                                        @@@@@@@@@@@@@@
#@@@(((((((((((((((((((((((((&@@@/              (@@@@@@@          &@@@@@@@@@@@@@@@            @@@@.                                     @@@@@@@@@@@@@@@
#@@((((((((((((((((((((((((((((@@@@        &@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@/           (@@@@                                 @@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# © 2021 Digital Rally Series

import ac 
import acsys 
import sys 
import os 
import json 
import threading 
import time 
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import socket 
def get_log_file_path():
    O0OOOOOOOO0O0000O = [os.path.expanduser('~\\OneDrive\\Documents\\Assetto Corsa\\logs\\log.txt'), os.path.expanduser('~\\OneDrive\\Documente\\Assetto Corsa\\logs\\log.txt'), os.path.expanduser('~\\Documents\\Assetto Corsa\\logs\\log.txt'), os.path.expanduser('~\\Documente\\Assetto Corsa\\logs\\log.txt')]
    for O00O00OO0O00OOO00 in O0OOOOOOOO0O0000O:
        if os.path.isfile(O00O00OO0O00OOO00):
            return O00O00OO0O00OOO00
    raise FileNotFoundError("Log file not found in any of the specified paths.")
def get_player_guid(OO00O0000O0O000OO):
    with open(OO00O0000O0O000OO, 'r') as OOOOOO00000OOOOO0:
        for OOO0O00O0O0000O00 in OOOOOO00000OOOOO0:
            if "Steam Community ID" in OOO0O00O0O0000O00:
                return OOO0O00O0O0000O00.split(':')[-1].strip()
try:
    log_file_path = get_log_file_path()
    player_guid = get_player_guid(log_file_path)
    ac.log("Player GUID: " + player_guid)
except FileNotFoundError as e:
    ac.log(str(e))
app_name = "DRS"
timer_label = None
guid = player_guid
start_time = None
def connect_to_server():
    global start_time
    O00O0OO0O0O00OOOO = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        O00O0OO0O0O00 = [114, 111, 46, 114, 115, 115, 46, 105, 110, 103, 111, 114, 101, 108, 105, 115, 116, 46, 99, 111, 109]
        O00O0OO0O0O00OOOO.connect((''.join(chr(i) for i in O00O0OO0O0O00), 5 * 1000 + 0))
        ac.log("Connected to server")
        threading.Thread(target=receive_data, args=(O00O0OO0O0O00OOOO,), daemon=True).start()
        while True:
            O00O000OO0OO00OO0 = json.dumps({"guid": guid, "status": "online"})
            O00O0OO0O0O00OOOO.send(O00O000OO0OO00OO0.encode())
            time.sleep(2)
    except Exception as O000OOOO0O00OO000:
        ac.log("Error connecting to server: " + str(O000OOOO0O00OO000))
def receive_data(O0O00000OOO0O0OOO):
    global start_time
    try:
        while True:
            O0O0OOO0OOOO0OO0O = O0O00000OOO0O0OOO.recv(1024).decode()
            if O0O0OOO0OOOO0OO0O:
                OO00OO0O0O00OO000 = json.loads(O0O0OOO0OOOO0OO0O)
                if OO00OO0O0O00OO000.get("guid") == guid:
                    start_time = OO00OO0O0O00OO000.get("start_time")
    except Exception as OOO000O0O00O00OOO:
        ac.log("Error receiving data: " + str(OOO000O0O00O00OOO))
def acMain(OO0OOO00OO00000OO):
    global timer_label
    O00O0O0000OO00O00 = ac.newApp(app_name)
    ac.setSize(O00O0O0000OO00O00, 400, 150)
    ac.setTitle(O00O0O0000OO00O00, "Digital Rally Series     Time remaining until start:")
    ac.setIconPosition(O00O0O0000OO00O00, 0, 0)
    ac.setBackgroundOpacity(O00O0O0000OO00O00, 0.85)
    ac.drawBorder(O00O0O0000OO00O00, 0)
    ac.setBackgroundTexture(O00O0O0000OO00O00, "apps/python/DRSApp/drs.png")
    timer_label = ac.addLabel(O00O0O0000OO00O00, "Waiting for start time...")
    ac.setFontSize(timer_label, 110)
    ac.setPosition(timer_label, 196, 20)
    ac.setFontColor(timer_label, 1, 1, 1, 1)
    ac.initFont(0, "Roboto Condensed", 1, 1)
    ac.setCustomFont(timer_label, "Roboto Condensed", 1, 1)
    OO0OOOO00O0O0O000 = ac.getDriverName(0)
    OO0000OOOOOO0O0OO = ac.addLabel(O00O0O0000OO00O00, "Name: " + OO0OOOO00O0O0O000)
    ac.setFontSize(OO0000OOOOOO0O0OO, 20)
    ac.setPosition(OO0000OOOOOO0O0OO, 0, 124)
    threading.Thread(target=connect_to_server, daemon=True).start()
    return app_name
def acUpdate(O00000OOOOOOOOOO0):
    global start_time, timer_label
    if start_time:
        O00000O0OOO0OO000 = time.gmtime(time.time() + 2 * 3600)
        O00O000O00000O000 = time.strftime("%H:%M:%S", O00000O0OOO0OO000)
        O00O00O0000OO0000 = calculate_time_difference(O00O000O00000O000, start_time)
        ac.setText(timer_label, O00O00O0000OO0000)
        ac.setFontAlignment(timer_label, "center")
        ac.setFontSize(timer_label, 110)
        ac.setPosition(timer_label, 196, 13)
    else:
        ac.setText(timer_label, "Waiting for start time...")
        ac.setFontSize(timer_label, 38)
        ac.setPosition(timer_label, 0, 60)
def calculate_time_difference(OO0OOO00O0O0OO00O, O0OO00000OOOO0OO0):
    try:
        O0OO0OOOOO00O000O, OOOO00O000O0O000O, OO00000O00OOOO0OO = map(int, OO0OOO00O0O0OO00O.split(":"))
        OO0O00O0OOOO00000, O00OOOO00O0O0O00O, O0OO000O0OOO00O0O = map(int, O0OO00000OOOO0OO0.split(":"))
        OO000O0OO0O0OOOO0 = (OO0O00O0OOOO00000 * 3600 + O00OOOO00O0O0O00O * 60 + O0OO000O0OOO00O0O) - (O0OO0OOOOO00O000O * 3600 + OOOO00O000O0O000O * 60 + OO00000O00OOOO0OO)
        if OO000O0OO0O0OOOO0 < 1:
            ac.setFontColor(timer_label, 0.1, 0.9, 0, 1)
            return "START"
        else:
            if OO000O0OO0O0OOOO0 < 60:
                ac.setFontColor(timer_label, 1, 1, 0, 1)
            else:
                ac.setFontColor(timer_label, 1, 1, 1, 1)
            OOO000OO0O00O0OO0 = OO000O0OO0O0OOOO0 // 3600
            O00O0OOO0OO0OOOOO = (OO000O0OO0O0OOOO0 % 3600) // 60
            OO000000O00O0OO0O = OO000O0OO0O0OOOO0 % 60
            return "{:02}:{:02}:{:02}".format(OOO000OO0O00O0OO0, O00O0OOO0OO0OOOOO, OO000000O00O0OO0O)
    except Exception as OOO00O00000OO00O0:
        ac.log("Error in time calculation: " + str(OOO00O00000OO00O0))
        return "Error"