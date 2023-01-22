# SXDork v1.0

SXDork is a powerful tool that utilizes the technique of google dorking to search for specific information on the internet. Google dorking is a method of using advanced search operators and keywords to uncover sensitive information that is publicly available on the internet. SXDork offers a wide range of options to search for different types of dorks, such as domain login dork, wpadmin dork, SQL dork, configuration file dorks, logfile dorks, dashboard dork, id_rsa dorks, ftp dorks, backup file dorks, mail archive dorks, password dorks, DCIM photos dork, and CCTV dorks.

One of the key features of SXDork is its ability to search dorks using the -s flag. This function allows users to retrieve a significant amount of information related to search keywords. Users can specify specific keywords and the tool will search for all the related information available on the internet. Additionally, users can use the -r flag to set the number of results that will be displayed. The default setting is 10 results, however, users can increase or decrease the number of results as per their requirement. This feature is useful for users who are looking for specific information and want to filter through the results quickly.

SXDork also allows users to search wildcard domains and find a wide range of information. This feature is particularly useful for security researchers, penetration testers and other professionals who need to find sensitive information on the internet. With the ability to search for different types of dorks, wildcard domains and filter through results, SXDork is a powerful tool that can help users find information that is publicly available on the internet.

SXDork has the ability to search for information on multiple domains. By default, the tool searches for information on pastebin.com and controlc.com, but you can easily add more domains to search against. To do this, you can navigate to the src directory and edit the dorks.py file, where you will see an array called src that contains the default domains. Simply add more domains to this array, and the next time you run a search query, SXDork will check all the domains in the array for the keyword you are searching for. This allows you to easily find information across multiple domains.

## Usage
```
git clone https://github.com/samhaxr/SXDork.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python SXDork.py

```

## Demo
![SXDorks](Img/SXDork.gif)
