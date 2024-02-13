# USM
Update Script Manager (USM) is a tool for use with Debian based Linux distributions. This tool runs in the terminal window, and provides a user friendly way of updating or installing either individual packages or a collection of packages. USMv1 supports 28 useful packages for a variety of purposes.

Experienced Linux users will likely find more streamlined practices by simply running terminal commands or writing custom bash scripts. This program was designed to be extremely user friendly for those with very limited experience or who are just getting into Linux operating systems, not to be the most streamlined tool for use by seasoned pros.

# How to install USM:
Clone the repository onto the user's device with the command:

**git clone https://github.com/C-Ogle/USM.git**

Next, run the setup script with:

**sudo python usm_setup.py**

The device should now contain a directory called "Bash" that is a child of the $HOME directory. Within this directory are a number of bash scripts that will be executed by the usm.py script. Please note that deleting or altering these scripts will directly impact USM's functionality. Now start USM by simply running:

**sudo python usm.py**

while in the same directory as the usm.py file.

## How it Works
USMv1 requires a specific directory structure in order to function properly. Rather than requiring the user to manage the directory structure for dependent files, the usm_setup.py program creates the necessary directory and dependent files for the user. This minimizes the number of files that must be downloaded by the user and allows usm.py to be run from any directory with full functionality, since the path to directory files is directly specified. This script updates/installs packages using apt and snap package managers, so sudo priveleges are required when running USM for the program to function properly.

Dependency files are generated in the ~/Bash/ directory generated by the setup program.

## About the packages included in USMv1


