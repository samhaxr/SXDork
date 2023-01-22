from src.colors import colors
import sys, time

msg = f"{colors.YELLOW}[+] SXDork {colors.GREEN}v1.0\n"
msg += f"{colors.YELLOW}[+] Author:{colors.RESET} Suleman Malik\n"
msg += f"{colors.YELLOW}[+] Github:{colors.RESET} github.com/samhaxr\n"
msg += f"{colors.YELLOW}[+] Twitter:{colors.RESET} @Sulemanmalik_3\n"

def writer():
    for char in msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)