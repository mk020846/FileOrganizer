# import os module for executing commands
import os 

# initializing some used vaiables
store = False
exten = ""
# initializing all extensions and folder to which they belong
extentions = {
	"py":"Python",
	"jpeg":"Photos",
	"jpg": "Photos",
	"png":"Photos",
	"pyc":"Python",
	"cpp":"C++",
	"deb":"DebianPackage",
	"sh":"LinuxShellScript",
	"gif":"Photos",
	"mp3":"Music",
	"mp4":"Videos",
	"m4a":"Music",
	"mkv":"Videos"
}
# making folder if it dosen't exists
for folder in extentions:
	cmd = "mkdir " + extentions[folder]
	try:
		os.system(cmd)
	except:
		print("Skipping as folder already exists")
'''using os.listdir() to generate a list of all files present 
in the directory '''

items = os.listdir()

# cycling through the items

for filename in items:
# cycling through each character of the filename
	for charac in filename:
		if store == True :
			exten += charac
		if charac == "." :
			store = True #if character is "." then store the rest part
	print(exten)
	try:
		if ( exten != "") :
			cmd = "mv " + filename + " " + "./" + extentions[exten] 
			os.system(cmd)
	except:
		print("ERROR")
	store = False
	exten=""







