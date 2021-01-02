import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print(Fore.RED + 'I am Red')
print(Back.CYAN + 'I am Cyan')
print(Style.BRIGHT + "I am Bright")


