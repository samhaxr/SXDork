from src.colors import colors
from os import system, name
import sys, time, os
from src.type import writer

def banner():
    print(f'''
    +-+-+-+-+-+-+-+-+-+-+-+
    V : :.::.:........:.:  :V
   A  {colors.RED}A{colors.RESET}:    ..:...:...:.   {colors.RED}A{colors.RESET} A
  .V  {colors.RED}MA{colors.RESET}:.....:M.::.::. .:{colors.RED}AM{colors.RESET}.M
 A'  .{colors.RED}VMMMMMMMMM{colors.RESET}:.:{colors.RED}AMMMMMMMV{colors.RESET}: A
:M .  .`{colors.RED}VMMMMMMV{colors.RESET}.:A `{colors.RED}VMMMMV{colors.RESET} .:M:
 V.:.  ..`{colors.RED}VMMMV{colors.RESET}.:AM..`{colors.RED}VMV{colors.RESET}' .: V
  V.  .:. .....:AMMA. . .:. .V
   VMM...: ...:.MMMM.: .: MMV 
    -+-+-+-+-+-+-+-+-+-+-+-     
        ''')

def load():
    msg = 'Loading Please Wait '
    animation = [f"{msg}[{colors.RED}■□□□□□□□□□ 10%{colors.RESET}]",
                f"{msg}[{colors.RED}■■□□□□□□□□ 20%{colors.RESET}]", 
                f"{msg}[{colors.RED}■■■□□□□□□□ 30%{colors.RESET}]", 
                f"{msg}[{colors.YELLOW}■■■■□□□□□□ 40%{colors.RESET}]", 
                f"{msg}[{colors.YELLOW}■■■■■□□□□□ 50%{colors.RESET}]", 
                f"{msg}[{colors.YELLOW}■■■■■■□□□□ 60%{colors.RESET}]", 
                f"{msg}[{colors.GREEN}■■■■■■■□□□ 70%{colors.RESET}]", 
                f"{msg}[{colors.GREEN}■■■■■■■■□□ 80%{colors.RESET}]", 
                f"{msg}[{colors.GREEN}■■■■■■■■■□ 90%{colors.RESET}]", 
                f"{msg}[{colors.GREEN}■■■■■■■■■■ 100%{colors.RESET}]"]
    for i in range(len(animation)):
        time.sleep(.5)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")

def clear():
    if os.name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def start():
    clear()
    banner()
    writer()
    print('+' + ('=' * 35) + '+')