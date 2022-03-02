from configparser import ConfigParser, ExtendedInterpolation
import os

def openConfig():
    pathConfig = os.path.join(os.getenv('appdata'), "overwatch_launcher/config.ini")
    
    if not existConfig(pathConfig):
        configBase()
        
    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read(pathConfig)
    
    return config

def existConfig(pathConfig):
    return os.path.isfile(pathConfig)

def configBase()->None:
    appdata_path = os.path.join(os.getenv('appdata'), "overwatch_launcher")
    if not existAppdata(appdata_path):
        os.mkdir(path=appdata_path)
    
    config = ConfigParser()

    config['commands'] = {
        'priority': '/High',
        'start_overwatch': 'start "" ${commands:priority} "${paths:overwatch}"',
    }

    config['paths'] = {
        'overwatch': 'C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe',
        'sample_img': '.\img\login.png',
        'appdata_path': appdata_path,
        'accs_json': "${paths:appdata_path}/accs.json",
        'config_ini': "${paths:appdata_path}/.config.ini"
    }
    
    saveConfig(config, appdata_path)
    
def saveConfig(config, appdata_path)->None:
    try:
        with open(os.path.join(appdata_path, 'config.ini'), 'w') as f:
            config.write(f)
    except:
        print("Can`t save config!")
        
def existAppdata(appdata_path):
    return os.path.isdir(appdata_path)