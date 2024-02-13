import os

#make Bash directory as child of $HOME
os.system('mkdir ~/Bash')

#update.sh script generation
os.system('touch $HOME/Bash/update.sh')
os.system('chmod u+x $HOME/Bash/update.sh')
os.system('echo "#!/bin/bash\n\napt update\napt full-upgrade -y" >> $HOME/Bash/update.sh')

#pentesting_package.sh script generation
os.system('touch $HOME/Bash/pentesting_package.sh')
os.system('chmod u+x $HOME/Bash/pentesting_package.sh')
os.system('echo "#!/bin/bash\n\napt install wifite -y\napt install wireshark -y\napt install tor -y\napt install hashcat -y\napt install john -y\napt install aircrack-ng -y\napt install nmap -y\napt install hydra -y\napt install lynis -y\napt install netcat -y" >> $HOME/Bash/pentesting_package.sh')

#managementTools.sh script generation
os.system('touch $HOME/Bash/managementTools.sh')
os.system('chmod u+x $HOME/Bash/managementTools.sh')
os.system('echo "#!/bin/bash\n\napt install git -y\napt install pip -y\napt install snap -y\napt install snapd -y\napt install make -y" >> $HOME/Bash/managementTools.sh')
    
#terminalTools.sh script generation    
os.system('touch $HOME/Bash/terminalTools.sh')
os.system('chmod u+x $HOME/Bash/terminalTools.sh')
os.system('echo "#!/bin/bash\n\napt install tree -y\napt install bat -y\napt install snap -y\nsnap install lsd\napt install tldr -y" >> $HOME/Bash/terminalTools.sh')
    
#infoTools.sh script generation
os.system('touch $HOME/Bash/infoTools.sh')
os.system('chmod u+x $HOME/Bash/infoTools.sh')
os.system('echo "#!/bin/bash\n\napt install snap -y\nsnap install bpytop\napt install bpytop -y\napt install neofetch -y\napt install speedtest-cli -y\napt install ncdu -y" >> $HOME/Bash/infoTools.sh')



