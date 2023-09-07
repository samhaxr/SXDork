from src.colors import colors
from os import system, name
import sys, time, os
from src.type import writer

def banner():
    banner_text = f"""
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
    """
    print(banner_text)

def load():
    msg = f'{colors.YELLOW}Loading Please Wait{colors.RESET} '
    bar_length = 10
    for i in range(bar_length + 1):
        progress = i / bar_length
        bar = f"[{colors.RED}{'■' * i}{colors.RESET}{'□' * (bar_length - i)}]"
        percentage = f"{int(progress * 100)}%"
        animation = f"{msg}{bar} {percentage}"
        time.sleep(0.5)
        sys.stdout.write("\r" + animation)
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