''' Mr Silent's Pan Card PDF Password Cracker '''

import exrex
import subprocess
import sys
import os
import time
import platform

#Linux:
#  To work in most of linux, i used APT Manager : "sudo apt-get install pdfcrack"
#  If your system not use APT Packate Manager Then Install "pdfcrack" from your packate manager
#Windows:
#  Windows User only have to install required library in Root Shell
#Wordlist Logic:
#  Month Pattern : (0[0-9])|(1[0-2])
#  Day Pattern   : (0[1-9])|(1[0-9])|(2[0-9])|(3[0-2])
#  Year Pattern  : (19[3-9][0-9])|(20[012][0-9])
#  Final Pattern : ((0[0-9])|(1[0-2]))((0[1-9])|(1[0-9])|(2[0-9])|(3[0-2]))((19[3-9][0-9])|(20[012][0-9]))
#                  ------------------  -----------------------------------  ------------------------------
#                            Day                       Month                               Year


try:
    filename = sys.argv[1]  #FileName
except Exception:
    print("<!> You Missed File Name\nPython3 script.py <PDF_Filenmae.pdf>")
    exit()


with open("wordlist","w") as words: #Generate WordList
    data = list(exrex.generate(r'((0[0-9])|(1[0-2]))((0[1-9])|(1[0-9])|(2[0-9])|(3[0-2]))((19[3-9][0-9])|(20[012][0-9]))'))   #Change Here To Get Diffrent Wordlist
    for listitem in data:
        words.write('%s\n' % listitem)
tic = time.time()
if platform.system() == "Linux":  #Crack In Linux
    if subprocess.call(["pdfcrack",filename,"--wordlist="+ os.path.join(os.getcwd(),"wordlist")]) > 0:
        subprocess.call(["sudo","apt-get","install","pdfcrack","-y"])
    output = subprocess.Popen(["pdfcrack",filename,"--wordlist="+ os.path.join(os.getcwd(),"wordlist")])
if platform.system() == "Windows": #Crack On Windows
    subprocess.call(["windows/pdfcrack.exe",filename,"--wordlist="+ os.path.join(os.getcwd(),"wordlist")])
toc = time.time()
print("Time Taken: " , str(toc - tic))
