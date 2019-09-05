import os
import subprocess
import filecmp

A = (os.listdir('/root/Desktop/nitish/'))
print A
B1 = (os.listdir('/root/SmartFoxServer_2X/SFS2X/extensions/Allpoker_SLC/'))
print B1
B2 = (os.listdir('/root/SmartFoxServer_2X/SFS2X/extensions/BJTGames/'))
print B2
B3 = (os.listdir('/root/SmartFoxServer_2X/SFS2X/extensions/Casino_Game/'))
print B3
B4 = (os.listdir('/root/SmartFoxServer_2X/SFS2X/extensions/Dragon_Tiger/'))
print B4
B5 = (os.listdir('/root/SmartFoxServer_2X/SFS2X/extensions/JackPotKing/'))
print B5
B6 = (os.listdir('/root/SmartFoxServer_2X/SFS2X/extensions/Poker_King/'))
print B6
#B4 = (os.listdir('/root/SmartFoxServer_2X/SFS2X/extensions/BJTGames/'))
#print B4
#B4 = (os.listdir('/root/SmartFoxServer_2X/SFS2X/extensions/BJTGames/'))
#print B4

if A==B1:
   subprocess.call("mv /root/Desktop/nitish/*  /root/SmartFoxServer_2X/SFS2X/extensions/Allpoker_SLC", shell=True)
elif A==B2:
   subprocess.call("mv /root/Desktop/nitish/*  /root/SmartFoxServer_2X/SFS2X/extensions/BJTGames", shell=True)
elif A==B3:
   subprocess.call("mv /root/Desktop/nitish/*  /root/SmartFoxServer_2X/SFS2X/extensions/Casino_Game", shell=True)
elif A==B4:
   subprocess.call("mv /root/Desktop/nitish/*  /root/SmartFoxServer_2X/SFS2X/extensions/Dragon_Tiger", shell=True)
elif A==B5:
   subprocess.call("mv /root/Desktop/nitish/*  /root/SmartFoxServer_2X/SFS2X/extensions/JackPotKing", shell=True)
elif A==B6:
   subprocess.call("mv /root/Desktop/nitish/*  /root/SmartFoxServer_2X/SFS2X/extensions/Poker_King", shell=True)

else:
   print("JAR NOT MATCHED")
if __name__ == '__main__':
    os.chdir("SmartFoxServer_2X/SFS2X/")
    os.system("./sfs2x-service restart")
    print 'dir changed'













