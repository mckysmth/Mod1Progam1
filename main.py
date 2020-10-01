from settings import Settings
import threading
import time
import os, shutil
from pathlib import Path
import datetime

def thread_function(setting):

    now = datetime.datetime.now()

    shutil.copytree(setting.get_backup_location(), Path(setting.get_save_location(),"File Backup [" + now.strftime("%Y-%m-%d %H%M") + "]"))
    
    print("DONE!")
    # time.sleep(setting.get_time_between())
    


def main():
    setting = Settings()
    if not Path("settings.txt").exists():
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

    backupThread = threading.Thread(target=thread_function, args=(setting,))

    backupThread.start()

if __name__ == "__main__":
    main()