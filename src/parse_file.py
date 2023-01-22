import argparse, sys

my_parser = argparse.ArgumentParser(description='Search keywords using google dork')
my_parser.add_argument('-s', '--search', type=str, required=False, help="Search keyword with dork")
my_parser.add_argument('-r', '--result', type=int, default=10, help="Number of output result")
my_parser.add_argument('-dl', '--domlogin', type=str, help="Search domain(s) for login pages")
my_parser.add_argument('-da', '--domadmin', type=str, help="Search domain(s) for admin panels")
my_parser.add_argument('-wp', '--wpadmin', type=str, help="Search domain(s) for wordpress admin")
my_parser.add_argument('-lp', '--lpanel', type=str, help="Search domain(s) for login panels")
my_parser.add_argument('-sql', '--sqlfile', type=str, help="Search domain(s) for sql database files")
my_parser.add_argument('-cnf', '--confile', type=str, help="Search domain(s) for configuration files")
my_parser.add_argument('-log', '--logfile', type=str, help="Search domain(s) for log files")
my_parser.add_argument('-dash', '--dashboard', type=str, help="Search domain(s) for the dashboard")
my_parser.add_argument('-rsa', '--idrsa', type=str, help="Search domain(s) for id_rsa pub keys")
my_parser.add_argument('-ftp', '--ftpfile', type=str, help="Search domain(s) for FTP files")
my_parser.add_argument('-bck', '--backupfile', type=str, help="Search domain(s) for backup files")
my_parser.add_argument('-ma', '--mailarchive', type=str, help="Search domain(s) for mail archives")
my_parser.add_argument('-pw', '--password', type=str, help="Search domain(s) for passwords")
my_parser.add_argument('-pic', '--photos', type=str, help="Search domain(s) for DCIM/Photos")
my_parser.add_argument('-cam', '--cctvcam', type=str, help="Search domain(s) for CCTV/CAMs")
my_parser.parse_args(args=None if sys.argv[1:] else ['--help'])
args = my_parser.parse_args()

dork_search = args.search
dork_result = args.result
dork_domlogin = args.domlogin
dork_domadmin = args.domadmin
dork_wpadmin = args.wpadmin
dork_lpanel = args.lpanel
dork_sqlfile = args.sqlfile
dork_confile = args.confile
dork_logfile = args.logfile
dork_dashboard = args.dashboard
dork_idrsa = args.idrsa
dork_ftpfile = args.ftpfile
dork_backupfile = args.backupfile
dork_mailarchive = args.mailarchive
dork_password = args.password
dork_photos = args.photos
dork_cctvcam = args.cctvcam