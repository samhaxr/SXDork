[![GitHub release](https://img.shields.io/badge/release-v1.0.0-brightgreen?style=flat-square)](https://github.com/samhaxr/SXDork/releases/tag/v1.0.0)
[![GitHub stars](https://img.shields.io/github/stars/samhaxr/SXDork?style=flat-square)](https://github.com/samhaxr/SXDork/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/samhaxr/SXDork?style=flat-square)](https://github.com/samhaxr/SXDork/network)
[![GitHub issues](https://img.shields.io/github/issues/samhaxr/SXDork?style=flat-square)](https://github.com/samhaxr/SXDork/issues)
[![GitHub license](https://img.shields.io/github/license/samhaxr/SXDork?style=flat-square)](https://github.com/samhaxr/SXDork/blob/main/LICENSE)

# SXDork v1.0

SXDork is a powerful tool that utilizes the technique of google dorking to search for specific information on the internet. Google dorking is a method of using advanced search operators and keywords to uncover sensitive information that is publicly available on the internet. SXDork offers a wide range of options to search for different types of dorks, such as domain login dork, wpadmin dork, SQL dork, configuration file dorks, logfile dorks, dashboard dork, id_rsa dorks, ftp dorks, backup file dorks, mail archive dorks, password dorks, DCIM photos dork, and CCTV dorks.

One of the key features of SXDork is its ability to search dorks using the -s flag. This function allows users to retrieve a significant amount of information related to search keywords. Users can specify specific keywords and the tool will search for all the related information available on the internet. Additionally, users can use the -r flag to set the number of results that will be displayed. The default setting is 10 results, however, users can increase or decrease the number of results as per their requirement. This feature is useful for users who are looking for specific information and want to filter through the results quickly.

SXDork also allows users to search wildcard domains and find a wide range of information. This feature is particularly useful for security researchers, penetration testers and other professionals who need to find sensitive information on the internet. With the ability to search for different types of dorks, wildcard domains and filter through results, SXDork is a powerful tool that can help users find information that is publicly available on the internet.

SXDork has the ability to search for information on multiple domains. By default, the tool searches for information on pastebin.com and controlc.com, but you can easily add more domains to search against. To do this, you can navigate to the src directory and edit the dorks.py file, where you will see an array called src that contains the default domains. Simply add more domains to this array, and the next time you run a search query, SXDork will check all the domains in the array for the keyword you are searching for. This allows you to easily find information across multiple domains.

## Installation
```
git clone https://github.com/samhaxr/SXDork.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python SXDork.py

```
## Usage
```
usage: SXDork.py [-h] [-s SEARCH] [-r RESULT] [-dl DOMLOGIN] [-da DOMADMIN]
                 [-wp WPADMIN] [-lp LPANEL] [-sql SQLFILE] [-cnf CONFILE]
                 [-log LOGFILE] [-dash DASHBOARD] [-rsa IDRSA] [-ftp FTPFILE]
                 [-bck BACKUPFILE] [-ma MAILARCHIVE] [-pw PASSWORD]
                 [-pic PHOTOS] [-cam CCTVCAM]

Search keywords using google dork

optional arguments:
  -h, --help            show this help message and exit
  -s SEARCH, --search SEARCH
                        Search keyword with dork
  -r RESULT, --result RESULT
                        Number of output result
  -dl DOMLOGIN, --domlogin DOMLOGIN
                        Search domain(s) for login pages
  -da DOMADMIN, --domadmin DOMADMIN
                        Search domain(s) for admin panels
  -wp WPADMIN, --wpadmin WPADMIN
                        Search domain(s) for wordpress admin
  -lp LPANEL, --lpanel LPANEL
                        Search domain(s) for login panels
  -sql SQLFILE, --sqlfile SQLFILE
                        Search domain(s) for sql database files
  -cnf CONFILE, --confile CONFILE
                        Search domain(s) for configuration files
  -log LOGFILE, --logfile LOGFILE
                        Search domain(s) for log files
  -dash DASHBOARD, --dashboard DASHBOARD
                        Search domain(s) for the dashboard
  -rsa IDRSA, --idrsa IDRSA
                        Search domain(s) for id_rsa pub keys
  -ftp FTPFILE, --ftpfile FTPFILE
                        Search domain(s) for FTP files
  -bck BACKUPFILE, --backupfile BACKUPFILE
                        Search domain(s) for backup files
  -ma MAILARCHIVE, --mailarchive MAILARCHIVE
                        Search domain(s) for mail archives
  -pw PASSWORD, --password PASSWORD
                        Search domain(s) for passwords
  -pic PHOTOS, --photos PHOTOS
                        Search domain(s) for DCIM/Photos
  -cam CCTVCAM, --cctvcam CCTVCAM
                        Search domain(s) for CCTV/CAMs

```
## Demo
![SXDorks](Img/SXDork.gif)
