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
from src.colors import colors
from src.dorks import *
from src.type import writer
from src.load import load, banner, clear, start
from src.parse_file import *

def main():
    try:
        start()
        if dork_search is not None:
            Keyword_dorks(dork_search)
        elif dork_domlogin is not None:
            run_dorks()
        elif dork_domadmin is not None:
            run_dorks()
        elif dork_wpadmin is not None:
            run_dorks()
        elif dork_lpanel is not None:
            run_dorks()
        elif dork_dashboard is not None:
            run_dorks()
        elif dork_idrsa is not None:
            run_dorks()
        elif dork_sqlfile is not None:
            run_dorks()
        elif dork_confile is not None:
            run_dorks()
        elif dork_logfile is not None:
            run_dorks()
        elif dork_ftpfile is not None:
            run_dorks()
        elif dork_backupfile is not None:
            run_dorks()
        elif dork_mailarchive is not None:
            run_dorks()
        elif dork_password is not None:
            run_dorks()
        elif dork_photos is not None:
            run_dorks()
        elif dork_cctvcam is not None:
            run_dorks()
        else:
            print('ERROR!')
    except urllib.error.HTTPError as err:
        if err.code == 429:
            print(f"{colors.RED}[!]{colors.RESET} HTTP Error 429: Too Many Requests. Try again later.\n")
        else:
            print(f"{colors.RED}[!]{colors.RESET} An error occurred:\n", err)
    
if __name__ == "__main__":
    main()
