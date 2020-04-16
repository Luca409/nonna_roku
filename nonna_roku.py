from __future__ import print_function
import datetime
import random
import subprocess
import time
import keyboard

roku_ip_address = "10.0.0.65"
roku_curl_command_template = "curl -d '' [roku_ip_address]:8060/[command]"

def constructBashCommandString(command):
    """Construct a bash command string using the input command and the roku's ip Aaddress"""
    bash_command = roku_curl_command_template
    bash_command = bash_command.replace("[roku_ip_address]", roku_ip_address)
    bash_command = bash_command.replace("[command]", command)
    return bash_command

pressHome = constructBashCommandString("keypress/home")
pressSelect = constructBashCommandString("keypress/select")
pressRight = constructBashCommandString("keypress/right")
keyDownRight = constructBashCommandString("keydown/right")
keyUpRight = constructBashCommandString("keyup/right")
pressLeft = constructBashCommandString("keypress/left")
pressDown = constructBashCommandString("keypress/down")
pressUp = constructBashCommandString("keypress/up")
pressBack = constructBashCommandString("keypress/back")
launchItaliaFilm = constructBashCommandString("launch/142121")
launchCatholicChurch = constructBashCommandString("launch/40407")
launchNewsApp = constructBashCommandString("launch/180336")

def executeBashcommand(commandString):
    """Execute given bash comman using subprocess library"""
    subprocess.Popen(commandString.split(), stdout=subprocess.PIPE).communicate()

def playCatholicChurch():
    """Put on random catholic church channel"""
    # First key press is just to awaken Roku
    executeBashcommand(pressHome)
    time.sleep(2)
    executeBashcommand(launchCatholicChurch)
    time.sleep(5)
    executeBashcommand(pressDown)
    time.sleep(2)
    # go right for some random amount of time less than 10 seconds
    executeBashcommand(keyUpRight)
    random_number = random.randint(0, 10)
    time.sleep(random_number)
    executeBashcommand(keyDownRight)
    time.sleep(2)
    executeBashcommand(pressSelect)
    time.sleep(2)
    executeBashcommand(pressSelect)

def playNews():
    """Put on news (I forget the name of it)"""
    # First key press is just to awaken Roku
    executeBashcommand(pressHome)
    time.sleep(2)
    executeBashcommand(launchNewsApp)
    time.sleep(60)
    executeBashcommand(pressSelect)
    time.sleep(2)
    executeBashcommand(pressSelect)
    time.sleep(2)
    executeBashcommand(pressSelect)
    time.sleep(2)
    executeBashcommand(pressSelect)
    time.sleep(2)
    executeBashcommand(pressSelect)
    time.sleep(2)
    executeBashcommand(pressSelect)

def goToHomescreen():
    """Go to the roku's homescreen"""
    # First key press is just to awaken Roku
    executeBashcommand(pressHome)
    time.sleep(2)
    executeBashcommand(pressHome)

def playRandomFilm():
    """Currently, play random top 10 film on Italia's Cinema app"""
    # First key press is just to awaken Roku
    executeBashcommand(pressHome)
    time.sleep(2)
    executeBashcommand(launchItaliaFilm)
    time.sleep(20)
    executeBashcommand(pressBack)
    time.sleep(2)
    executeBashcommand(pressSelect)
    time.sleep(2)
    # Go all the way to the left of top 10 films so you can randomly go right
    for _ in range(10):
        executeBashcommand(pressLeft)
        time.sleep(1)
    random_number = random.randint(0, 10)
    for _ in range(random_number):
        executeBashcommand(pressRight)
        time.sleep(1)
    executeBashcommand(pressSelect)
    time.sleep(2)
    # Go down to the bottom then back up 1 so you're always choosing 'Play' OR
    # 'Play from beginning'
    executeBashcommand(pressDown)
    time.sleep(1)
    executeBashcommand(pressDown)
    time.sleep(1)
    executeBashcommand(pressUp)
    time.sleep(1)
    executeBashcommand(pressSelect)

keyboard.add_hotkey('0', lambda: goToHomescreen())
keyboard.add_hotkey('3', lambda: playRandomFilm())
keyboard.add_hotkey('6', lambda: playCatholicChurch())
keyboard.add_hotkey('9', lambda: playNews())
keyboard.wait()
