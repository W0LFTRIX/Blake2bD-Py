import os
import hashlib
from hashlib import blake2b
from termcolor import colored
from time import sleep

def main() :
	# The line below changes depending on the operating system
	os.system('clear')
	print(colored("This program is for educational purposes, I'm in no way responsible for your actions", "white"))
	print("")
	print(colored("""
 ____  _       _        ___  _     _____  
|  _ \| |     | |      |__ \| |   |  __ \ 
| |_) | | __ _| | _____   ) | |__ | |  | |
|  _ <| |/ _` | |/ / _ \ / /| '_ \| |  | |
| |_) | | (_| |   <  __// /_| |_) | |__| |
|____/|_|\__,_|_|\_\___|____|_.__/|_____/

	""", "cyan"))
	print(colored("Created By Wolftrix !! ", "red").center(110))
	print("")
	print(colored("Write [exit] to exit", "blue"))
	print("")

main()
choiceFile = input(colored("Enter the path of the file you want to encrypt : ", "yellow"))


while 1 :
	try :
		if choiceFile == "exit" :
			break
		else :
				file = open(choiceFile, "r")
				file.read()
				file.close()
				break
		
	except :
		print("")
		print(colored("This file does not exit !! ", "red"))
		sleep(1)
		main()
		choiceFile = input(colored("Enter the path of the file you want to encrypt : ", "yellow"))
		

		

def fileChange() :
	if choiceFile == "exit" :
		print(colored("Thank's for using this program", "magenta"))
	
	else :
			file = open(choiceFile, "r")
			content = file.read().encode()
			file.close()

			os.remove(choiceFile)

			file = open(choiceFile, "w")
			contentHash = file.write(hashlib.blake2b(content).hexdigest())
			file.close()
			print("")
			print(colored("Successfully executed !! ", "cyan"))
			print(colored("Thank's for using this program", "magenta"))



if choiceFile == "exit" :
	print(colored("Thank's for using this program", "magenta"))

else :
	fileChange()



