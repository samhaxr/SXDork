from __future__ import print_function
from googlesearch import search, get_random_user_agent
from tabulate import tabulate as tab
import time, sys, urllib
from src.colors import colors
from src.type import writer
from src.load import load
from src.parse_file import *

src = ['pastebin.com', 'controlc.com']

def tbody(*x):
    print(tab(x[0], headers=x[1], tablefmt='fancy_grid'))

def Keyword_dorks(dork_search):
    for x in src:
        try:
            if dork_result:
                amount = dork_result
            word_search_dork = f'site:{x} "{dork_search}"'
            __req = 0
            body = []
            headers = f'Keyword(s) \"{colors.GREEN}{dork_search}{colors.RESET}'
            headers += f'\" in {colors.RED}{x}{colors.RESET}'
            head = [headers]
            for results in search(word_search_dork, tld="com", lang="en", 
                num=int(amount), start=0, stop=None, pause=2, 
                user_agent=get_random_user_agent()):
                body.append([results])
                __req += 1
                if __req >= int(amount):
                    break
                time.sleep(0.1)
            load()
            tbody(body, head)
        except KeyboardInterrupt:
                print ("\n")
                sys.exit(1)
                
def run_dorks():
    search_map = {
        "dork_domlogin": "inurl:login site:{}",
        "dork_domadmin": "inurl:admin site:{}",
        "dork_wpadmin": "inurl:wp-admin site:{}",
        "dork_lpanel": "inurl:loginpanel site:{}",
        "dork_dashboard": "inurl:dashboard site:{}",
        "dork_idrsa": "index of:id_rsa id_rsa.pub site:{}",
        "dork_sqlfile": "filetype:sql site:{}",
        "dork_confile": "filetype:conf site:{}",
        "dork_logfile": "filetype:conf site:{}",
        "dork_ftpfile": 'intitle:"index of" "ftp" site:{}',
        "dork_backupfile": 'intitle:"index of" "backup" site:{}',
        "dork_mailarchive": 'intitle:"index of" "mail" site:{}',
        "dork_password": 'intitle:"index of" "password" site:{}',
        "dork_photos": 'intitle:"index of" "DCIM" site:{}',
        "dork_cctvcam": 'inurl:"CgiStart?page=" site:{}'
    }
    try:
        if dork_result:
            amount = dork_result
        for key, value in search_map.items():
            if vars().get(key):
                login_search_dork = value.format(vars().get(key))
                headers = f'Searching {" ".join(key.split("_")[1:])} for the domain '
                headers += f'\"{colors.GREEN}{vars().get(key)}{colors.RESET}\"'
                break
        __req = 0
        body = []
        head = [headers]
        for results in search(login_search_dork, tld="com", lang="en", num=int(amount),
            start=0, stop=None, pause=2,
            user_agent=get_random_user_agent()):
            body.append([results])
            __req += 1
            if __req >= int(amount):
                break
            time.sleep(0.1)
        load()
        tbody(body, head)
    except KeyboardInterrupt:
        print("\n")
        sys.exit(1)
