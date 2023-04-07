#!/bin/bash
#!Coded by Suleman Malik
#!www.sulemanmalik.com
#!Twitter: @sulemanmalik_3
#!Linkedin: http://linkedin.com/in/sulemanmalik03/
#
# Copyright (c) 2022 Suleman Malik
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from __future__ import print_function
from src.dorks import *
from src.load import start


dork_functions = {
    'dork_search': Keyword_dorks,
    'dork_domlogin': run_dorks,
    'dork_domadmin': run_dorks,
    'dork_wpadmin': run_dorks,
    'dork_lpanel': run_dorks,
    'dork_dashboard': run_dorks,
    'dork_idrsa': run_dorks,
    'dork_sqlfile': run_dorks,
    'dork_confile': run_dorks,
    'dork_logfile': run_dorks,
    'dork_ftpfile': run_dorks,
    'dork_backupfile': run_dorks,
    'dork_mailarchive': run_dorks,
    'dork_password': run_dorks,
    'dork_photos': run_dorks,
    'dork_cctvcam': run_dorks,
}

def main():
    try:
        start()
        for key, value in dork_functions.items():
            if vars().get(key):
                value()
                break
        else:
            print('ERROR!')
    except urllib.error.HTTPError as err:
        if err.code == 429:
            print(f"{colors.RED}[!]{colors.RESET} HTTP Error 429: Too Many Requests. Try again later.\n")
        else:
            print(f"{colors.RED}[!]{colors.RESET} An error occurred:\n", err)
    
if __name__ == "__main__":
    main()