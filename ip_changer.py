import os

ip = input('Give any static ip you want assigned ranging from (1, 253)--->> ')

os.system('networksetup -setmanualwithdhcprouter Wi-Fi '+ip)
