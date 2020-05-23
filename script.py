''' Mr Silent's Pan Card PDF Password Cracker '''

import exrex
import subprocess
import sys
import os
import time
import platform

#  Month Pattern : (0[0-9])|(1[0-2])
#  Day Pattern   : (0[1-9])|(1[0-9])|(2[0-9])|(3[0-2])
#  Year Pattern  : (19[3-9][0-9])|(20[012][0-9])
#  Final Pattern : ((0[0-9])|(1[0-2]))((0[1-9])|(1[0-9])|(2[0-9])|(3[0-2]))((19[3-9][0-9])|(20[012][0-9]))
#                  ------------------  -----------------------------------  ------------------------------
#                            Day                       Month                               Year

filename = sys.argv[1]
tic = time.time()
with open("wordlist","w") as words:
    data = list(exrex.generate(r'((0[0-9])|(1[0-2]))((0[1-9])|(1[0-9])|(2[0-9])|(3[0-2]))((19[3-9][0-9])|(20[012][0-9]))'))   #Change Here To Get Other Wordlist
    for listitem in data:
        words.write('%s\n' % listitem)

if platform.system() == "Linux":
    if subprocess.call(["pdfcrack",filename,"--wordlist="+ os.path.join(os.getcwd(),"wordlist")]) > 0:
        subprocess.call(["sudo","apt-get","install","pdfcrack","-y"])
        output = subprocess.Popen(["pdfcrack",filename,"--wordlist="+ os.path.join(os.getcwd(),"wordlist")])
if platform.system() == "Windows":
    subprocess.call(["windows/pdfcrack.exe",filename,"--wordlist="+ os.path.join(os.getcwd(),"wordlist")])
toc = time.time()
print("Time Taken: " , str(toc - tic))