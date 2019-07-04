import socket
from colorama import Fore

def print_success(message):
    print('{} [*] {}{}'.format(Fore.GREEN, message, Fore.RESET))

def print_error(message):
    print('{} [-] {}{}'.format(Fore.RED, message, Fore.RESET))

def print_info(message):
    print('{} [!] {}{}'.format(Fore.CYAN, message, Fore.RESET))

def print_warning(message):
    print('{} [!] {}{}'.format(Fore.YELLOW, message, Fore.RESET))

def check_up_services(lst):
	for i, url in enumerate(lst):
		socket.setdefaulttimeout(7)
		host, port = (url.split('://')[1].split(':')[0], url.split('://')[1].split(':')[1])
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			try:
				s.connect((host, int(port)))
			except:
				print_error('[%s] Host is down or communication is filtered...' % (url))
				lst.remove(url)
	return(lst)
