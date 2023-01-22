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
    try:
        if dork_result:
            amount = dork_result
        if dork_domlogin:
            login_search_dork = f'inurl:login site:{dork_domlogin}'
            headers = f'Searching login pages for the domain '
            headers += f'\"{colors.GREEN}{dork_domlogin}{colors.RESET}\"'
        if dork_domadmin:
            login_search_dork = f'inurl:admin site:{dork_domadmin}'
            headers = f'Searching admin panels for the domain '
            headers += f'\"{colors.GREEN}{dork_domadmin}{colors.RESET}\"'
        if dork_wpadmin:
            login_search_dork = f'inurl:wp-admin site:{dork_wpadmin}'
            headers = f'Searching wordpress admin panel for the domain '
            headers += f'\"{colors.GREEN}{dork_wpadmin}{colors.RESET}\"'
        if dork_lpanel:
            login_search_dork = f'inurl:loginpanel site:{dork_lpanel}'
            headers = f'Searching login panel for the domain '
            headers += f'\"{colors.GREEN}{dork_lpanel}{colors.RESET}\"'
        if dork_dashboard:
            login_search_dork = f'inurl:dashboard site:{dork_dashboard}'
            headers = f'Searching dashboard for the domain '
            headers += f'\"{colors.GREEN}{dork_dashboard}{colors.RESET}\"'
        if dork_idrsa:
            login_search_dork = f'index of:id_rsa id_rsa.pub site:{dork_idrsa}'
            headers = f'Searching for id_rsa pub keys on '
            headers += f'\"{colors.GREEN}{dork_idrsa}{colors.RESET}\"'
        if dork_sqlfile:
            login_search_dork = f'filetype:sql site:{dork_sqlfile}'
            headers = f'Searching for sql files on '
            headers += f'\"{colors.GREEN}{dork_sqlfile}{colors.RESET}\"'
        if dork_confile:
            login_search_dork = f'filetype:conf site:{dork_confile}'
            headers = f'Searching for configuration files on '
            headers += f'\"{colors.GREEN}{dork_confile}{colors.RESET}\"'
        if dork_logfile:
            login_search_dork = f'filetype:conf site:{dork_logfile}'
            headers = f'Searching for log files on '
            headers += f'\"{colors.GREEN}{dork_logfile}{colors.RESET}\"'
        if dork_ftpfile:
            login_search_dork = f'intitle:"index of" "ftp" site:{dork_ftpfile}'
            headers = f'Searching for FTP files on '
            headers += f'\"{colors.GREEN}{dork_ftpfile}{colors.RESET}\"'
        if dork_backupfile:
            login_search_dork = f'intitle:"index of" "backup" site:{dork_backupfile}'
            headers = f'Searching for backup files on '
            headers += f'\"{colors.GREEN}{dork_backupfile}{colors.RESET}\"'
        if dork_mailarchive:
            login_search_dork = f'intitle:"index of" "mail" site:{dork_mailarchive}'
            headers = f'Searching for mail archives on '
            headers += f'\"{colors.GREEN}{dork_mailarchive}{colors.RESET}\"'
        if dork_password:
            login_search_dork = f'intitle:"index of" "password" site:{dork_password}'
            headers = f'Searching passwords on '
            headers += f'\"{colors.GREEN}{dork_password}{colors.RESET}\"'
        if dork_photos:
            login_search_dork = f'intitle:"index of" "DCIM" site:{dork_photos}'
            headers = f'Searching DCIM/Photos on '
            headers += f'\"{colors.GREEN}{dork_photos}{colors.RESET}\"'
        if dork_cctvcam:
            login_search_dork = f'inurl:”CgiStart?page=” site:{dork_cctvcam}'
            headers = f'Searching CCTV/CAMs on '
            headers += f'\"{colors.GREEN}{dork_cctvcam}{colors.RESET}\"'
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