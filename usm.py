#==========================================================
#BASH script manager for Debian Linux Machines

# All update bash scripts must have execute permission and be located in the ~/Bash/ directory
# Run this script as superuser with command 'sudo python usm.py'

#==========================================================

import os

def displayfull():
    print('''
[0] system reboot
[1] run system updates
[2] run pentesting tool updates
[3] run individual common package updates
[4] run package installer updates
[5] run txt editor updates
[6] run terminal tool updates
[7] run system info tool updates
[8] run ASCII banner generator update

''')
    
def displaypartial():
    print('''
[0] system reboot
[1] run system updates
[2] run pentesting tool updates
[3] run individual package updates
[4] run package installer updates
...
[99] display full options menu
''')
    
def packageMenu():
    print('Choose a package to update, or return to primary menu:')
    print('''
[0] nmap
[1] wireshark
[2] tor
[3] screen
[4] wifite
[5] hashcat
[6] john
[7] aircrack-ng
[8] hydra
[9] lynis
[10] netcat
[11] idle
[12] pip
[13] git
[14] joe
[15] tree
[16] nano
[17] emacs
[18] vim
[19] snap
[20] bpytop
[21] neofetch
[22] speedtest-cli
[23] ncdu
[24] bat
[25] lsd
[26] tldr
[27] figlet

[x] exit
''')
    
#Individual package install handler
def packageUpdate():
    commands = {0:'apt install nmap -y', 1:'apt install wireshark -y', 2:'apt install tor -y', 3: 'apt install screen -y',
                4: 'apt install wifite -y', 5:'apt install hashcat -y', 6:'apt install john -y', 7:'apt install aircrack-ng -y',
                8: 'apt install hydra -y', 9:'apt install lynis -y', 10:'apt install netcat -y', 11:'apt install idle -y',
                12:'apt install pip -y', 13:'apt install git -y', 14:'apt install joe -y', 15:'apt install tree -y',
                16:'apt install nano -y', 17:'apt install emacs -y', 18:'apt install vim -y',19:'apt install snap -y',
                20:'apt install snap -y;snap install bpytop',21:'apt install neofetch -y',22:'apt install speedtest-cli -y',
                23:'apt install ncdu -y',24:'apt install bat -y',25:'apt install snap -y; snap isntall lsd',26:'apt install tldr -y',
                27:'apt install figlet -y'}

    menuKey = {0:'nmap', 1:'wireshark',2:'tor',3:'screen',4:'wifite',5:'hashcat',6:'john',7:'aircrack-ng',8:'hydra',9:'lynis',
               10:'netcat',11:'idle', 12:'pip',13:'git', 14:'joe', 15:'tree',16:'nano',17:'emacs',18:'vim',19:'snap',
               20:'bpytop', 21:'neofetch',22:'speedtest-cli',23:'ncdu',24:'bat',25:'lsd',26:'tldr',27:'figlet'}
    while(1):
        package = input('-->')
        if package == 'x':
            print('Exiting to primary menu...')
            break
        elif package.isalpha():
            print('Invalid command character entered. Please select an option from the package menu above.')
            continue
        elif int(package) >= len(commands):
            print('Invalid command character entered. Please select an option from the package menu above.')
            continue
        else:
            print('Updating ' + menuKey[int(package)] + ' package....')
            os.system(commands[int(package)])
            packageMenu()
        
        
def txteditors():
        print(''' Please select a text editor, or return to primary menu.
[0] nano
[1] vim
[2] emacs
[3] joe
[4] update/install all

[x] exit
''')
   
#individual text editor install handler
def txteditorChoice():
    txteditors()
    
    commands = {0:'apt install nano -y', 1:'apt install vim -y', 2:'apt install emacs -y', 3:'apt install joe -y'}
    
    menuKey = {0:'nano',1:'vim',2:'emacs',3:'joe'}
    
    while(1):
        package = input('-->')
        if package == 'x':
            print('Exiting to primary menu...')
            break
        elif package.isalpha():
            print('Invalid command character entered. Please select an option from the package menu above.')
            continue
        elif int(package) > 4:
            print('Invalid command character entered. Please select an option from the package menu above.')
            continue
        
        if int(package) == 4:
            print('Updating all text editors....')
            os.system(commands[0])
            os.system(commands[1])
            os.system(commands[2])
            os.system(commands[3])
        else:
            print('Updating ' + menuKey[int(package)] + ' package....')
            os.system(commands[int(package)])
            txteditors()
    
    
def systemUpdate():
    print('You have selected System Updates. This requires a reboot for changes updates to take effect.')
    print('Rebooting the system will close all processes currently running, including USM.')
    print('It is recommended to reboot only if you are finished updating packages for this session. Reboot now? [y/n]\n')
    reboot = input('--> ')
    if reboot == 'n':
        print('Installing update packages without system reboot....')
    elif reboot != 'y':
        print('Invalid command character entered. Please perform system reboot manually.')
        print('Installing update packages without system reboot....')
    os.system('bash ~/Bash/update.sh')
    if reboot == 'y':
        os.system('reboot')
        
    
#==============================================
#==============================================
        #BEGIN MAIN#
    
if os.geteuid() != 0:
    exit('USM requires root priveleges. Try {sudo python usm.py} command. Exiting now...')
  
print('''
__/\\\________/\\\_____/\\\\\\\\\\\____/\\\\____________/\\\\_        
 _\/\\\_______\/\\\___/\\\/////////\\\_\/\\\\\\________/\\\\\\_       
  _\/\\\_______\/\\\__\//\\\______\///__\/\\\//\\\____/\\\//\\\_      
   _\/\\\_______\/\\\___\////\\\_________\/\\\\///\\\/\\\/_\/\\\_     
    _\/\\\_______\/\\\______\////\\\______\/\\\__\///\\\/___\/\\\_    
     _\/\\\_______\/\\\_________\////\\\___\/\\\____\///_____\/\\\_   
      _\//\\\______/\\\___/\\\______\//\\\__\/\\\_____________\/\\\_  
       __\///\\\\\\\\\/___\///\\\\\\\\\\\/___\/\\\_____________\/\\\_ 
        ____\/////////_______\///////////_____\///______________\///__
        
  __  __        __     __        ____        _      __    __  ___                           
 / / / /__  ___/ /__ _/ /____   / __/_______(_)__  / /_  /  |/  /__ ____  ___ ____ ____ ____
/ /_/ / _ \/ _  / _ `/ __/ -_) _\ \/ __/ __/ / _ \/ __/ / /|_/ / _ `/ _ \/ _ `/ _ `/ -_) __/
\____/ .__/\_,_/\_,_/\__/\__/ /___/\__/_/ /_/ .__/\__/ /_/  /_/\_,_/_//_/\_,_/\_, /\__/_/   
    /_/                                    /_/                               /___/          

''')

#user = os.environ('USER')
#user = 'user'
print('Hello, welcome to the Update Script Manager (USM)!')
print('USM is a Python-driven program that works in conjunction with bash scripts to provide an easy medium for updating or installing packages in Debian based Linux distributions')
print('Please select an option from the menu below, or enter q to quit.\n')
userchoice = 'b'

while(userchoice != 'q'):
    displaypartial()
    userchoice = input('--> ')
    if userchoice == 'q':
        continue
    elif userchoice.isalpha():
        print('Invalid command character entered. Please select an option from the menu above.')
        continue
    
    if int(userchoice) == 0:
        print('You are about to perform a system reboot. This will close all sessions actively running.')
        print('Reboot now? [y/n]\n')
        userchoice = input('--> ')
        if userchoice == 'y':
            os.system('reboot')
        elif userchoice == 'n':
            continue
        else:
            print('Invalid command character entered. Returning to primary menu...')
            continue
    if int(userchoice) == 1:
        systemUpdate()
    if int(userchoice) == 2:
        os.system('bash $HOME/Bash/pentesting_package.sh')
    if int(userchoice) == 3:
        packageMenu()
        packageUpdate()
    if int(userchoice) == 4:
        os.system('bash $HOME/Bash/managementTools.sh')
    if int(userchoice) == 5:
        txteditorChoice()
    if int(userchoice) == 6:
        os.system('bash $HOME/Bash/terminalTools.sh')
    if int(userchoice) == 7:
        os.system('bash $HOME/Bash/infoTools.sh')
    if int(userchoice) == 8:
        os.system('apt install figlet -y')    
    
    if int(userchoice) == 99:
        displayfull()
    
