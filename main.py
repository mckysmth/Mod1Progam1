from settings import Settings
import threading
import time
import os, shutil
from pathlib import Path
import datetime
import sys

def thread_function(setting):

    while True:

        now = datetime.datetime.now()

        # shutil.copytree(setting.get_backup_location(), Path(setting.get_save_location(),"File Backup [" + now.strftime("%Y-%m-%d %H%M") + "]"))

        print("File have been copied to " + str(Path(setting.get_save_location(),"File Backup [" + now.strftime("%Y-%m-%d %H%M") + "]")))

        delete_oldies(setting, now)

        time.sleep(setting.get_time_between())
        # time.sleep(30)

def delete_oldies(setting, now):
    for filename in os.listdir(setting.get_save_location()):
        cDate = os.stat(os.path.join(setting.get_save_location(), filename)).st_ctime

        folderDate = datetime.date.fromtimestamp(cDate)
        nowDate = now.date()

        if (nowDate - folderDate).days >= setting.get_keep_backups():
            shutil.rmtree(os.path.join(setting.get_save_location(), filename))

        

        # for subfolder in subfolders:
        #     print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    
    


def main():

    setting = Settings()

    if not Path("settings.json").exists():
        while True:
            if setting.set_time_between(int(input("Frequency to between backups [Minutes]: "))):
                break

        while True:
            if setting.set_backup_location(str(Path(input("Source folder to backup: ")))):
                break

        while True:
            if setting.set_save_location(str(Path(input("Destination folder to save backup: ")))):
                break

        while True:
            if setting.set_keep_backups(int(input("Keep backups for [Days]: "))):
                break

        setting.save_settings()

    backupThread = threading.Thread(target=thread_function, args=(setting,), daemon=True)
    backupThread.start()

    while True:
        userInput = input()
        userInput.lower()
        if userInput == 'stop':
            sys.exit()
        elif userInput == 'c destination':
            setting.set_save_location(input("Source folder to backup: "))
            setting.save_settings()
        elif userInput == 'c source':
            setting.set_save_location(input("Destination folder to save backup: "))
            setting.save_settings()
        elif userInput == 'c time':
            setting.set_save_location(input("Frequency to between backups [Hours]: "))
            setting.save_settings()
        else:
            print ('Invalid Command')
        

if __name__ == "__main__":
    main()