# About this fork

It's using pushover notifications instead of Telegram.

# Installation

Install the dependencies

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 
pip3 install -r requirements.txt 
```

Optionally you can run it in venv

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 
sudo apt install python3-pip
pip3 install virtualenv
python3 -m virtualenv env
source env/bin/activate
pip3 install -r requirements.txt 
```

Rename config.example.py to config.py, add your requested Telegram TOKEN (It is requested from 
`BotFather`) and modify the bikes that you are looking for

```bash
mv config.example.py config.py
vim config.py
```

After installation is compelte, just run the main.py

```bash
python3 main.py
```