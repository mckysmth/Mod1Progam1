from pathlib import Path
import ast



class Settings:

    def __init__(self):
        if not Path("settings.txt").exists():
            self.data = {
                "save_location": "",
                "backup_location": "",
                "time_between": 0
            }
        else:
            self.data = ast.literal_eval(Path('settings.txt').read_text())
    
    def set_save_location(self, location):
        if len(location) > 0:
            self.data["save_location"] = location
            return True
        else:
            return False


    def set_backup_location(self, location):
        if len(location) > 0:
            self.data["backup_location"] = location
            return True
        else:
            return False

    def set_time_between(self, hours):
        if str(hours).isdigit() and int(hours) > 0:
            seconds = int(hours) * 60 * 60
            self.data["time_between"] = seconds
            return True
        else:
            return False

    def get_save_location(self):
        return self.data["save_location"]

    def get_backup_location(self):
        return self.data["backup_location"]

    def get_time_between(self):
        return self.data["time_between"]

    def save_settings(self):
        settingsFile = open('settings.txt', 'w')  

        settingsFile.write(str(self.data))

        settingsFile.close()

        


