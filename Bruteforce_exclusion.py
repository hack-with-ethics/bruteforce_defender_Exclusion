import os
import threading
from subprocess import * 

class bruteforce_exclusion:
    def __init__(self):
        self.brt_lst = []
        self.thread = []
    def filter_drives(self):
        return getoutput("wmic logicaldisk get caption").split()[1::]

    def execute_command(self,path):
        return getoutput(f'"c:\Program Files\Windows Defender\mpcmdrun.exe" -scan -scantype 3 -file "{path}\\|*"')

    def traverse_drives(self,div):
        for root,dirs,files in os.walk(div+"\\"):
            for d in dirs:
                path = os.path.join(root,d)
                if "was skipped" in self.execute_command(path):
                    print(" [ + ] ",path)
                    self.brt_lst.append(path)
        print(f"\n [ ! ] Scanning {div} finished")         
    def start_bruteforce(self):
        drives = self.filter_drives()
        for d in drives:
            th = threading.Thread(target=self.traverse_drives,args=(d,))
            th.start()
            self.thread.append(th)
        for thr in self.thread:
            thr.join()
        if len(self.brt_lst) == 0:
            print(" [ ! ] no Exclusion Found [ ! ]")
        else:
            print("exclusion Path Count :",len(self.brt_lst))
        print("Done [ ! ]")
        
b = bruteforce_exclusion()
b.start_bruteforce()

