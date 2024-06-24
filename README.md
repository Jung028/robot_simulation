#Documentation 

Installed ubuntu 20.04 server. Which is arm architecture, as UTM, a virtual machine for mac, supports arm architecture. There is no arm for desktop, therefore I installed server, and sudo apt install ubuntu-desktop. 

The process is quite tricky. When installing the server, make sure you remember your username and password. Or have to restart the installation. So once its installed, eject the iso from the top right, and restart. Then it will display the terminal for the server. Install the ubuntu-desktop and you are set. 

To integrate vs code in ubuntu for github push and pull. Download vscode .arm from the website, and extract the files by going to the cd Downloads, then sudo dpkg -i code_1.90.2-1718750608_arm64.deb. Then type code. Go to github and create a new repo, go to the ubuntu and create the same repo name using mkdir name_of_project. Create a new python file by typing touch name_of_file.py. 

##In vs code 
```
# Initialize Git repository
git init
git add .
git commit -m "Initial commit"

# Add remote repository
git remote add origin https://github.com/Jung028/robot_simulation.git

# Push to GitHub
git push -u origin master
```

##In ubuntu terminal 
```
# Clone the repository
git clone https://github.com/Jung028/robot_simulation.git
cd robot_simulation

# Ensure dependencies are installed
sudo apt update
sudo apt install python3 python3-pip
pip3 install matplotlib

# Run the simulation
python3 simulate.py
```

##To create a file : 
```touch name.py```

##To open the file : 
```gedit name.py```


##To add source : 
```gedit ~/.bashrc```
