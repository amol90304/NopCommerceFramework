import configparser

config = configparser.RawConfigParser()
config.read("C:/Users/amols/PycharmProjects/pythonProject/FacebookPOM/Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsermail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

