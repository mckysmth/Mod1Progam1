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

        shutil.copytree(setting.get_backup_location(), Path(setting.get_save_location(),"File Backup [" + now.strftime("%Y-%m-%d %H%M") + "]"))

        print("File have been copied to " + str(Path(setting.get_save_location(),"File Backup [" + now.strftime("%Y-%m-%d %H%M") + "]")))

        time.sleep(setting.get_time_between())
        time.sleep(5)


    


def main():

    setting = Settings()

    if not Path("settings.json").exists():
        while True:
            if setting.set_time_between(int(input("Backup frequency [Hours]: "))):
                break

        while True:
            source = input("Folder to backup: ")
            if setting.set_backup_location(str(Path(source))):
                break

        while True:
            destination = input("Folder to save backup: ")
            if setting.set_save_location(str(Path(destination))):
                break

        setting.save_settings()

    backupThread = threading.Thread(target=thread_function, args=(setting,), daemon=True)
    backupThread.start()

    while True:
        userInput = input()
        userInput.lower()
        if userInput == 'stop':
            sys.exit()
        elif userInput == 'cd destination':
            setting.set_save_location(input("Folder to save backup: "))
            setting.save_settings()
        elif userInput == 'cd source':
            setting.set_save_location(input("Folder to backup: "))
            setting.save_settings()
        elif userInput == 'cd time':
            setting.set_save_location(input("Backup frequency [Hours]: "))
            setting.save_settings()
        else:
            print ('Invalid Command')
        

if __name__ == "__main__":
    main()