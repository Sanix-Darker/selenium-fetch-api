import configparser as ConfigParser

# Configs parameters
configParser = ConfigParser.RawConfigParser()   
configFilePath = r'config.txt'
configParser.read(configFilePath)

# Filling parameters
SECRET_KEY = configParser.get('config', 'SECRET_KEY')
