import configparser

class GlobalConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        
    @property
    def api_key(self):
        return self.config.get('openai', 'api_key')

    @property
    def model(self):
        return self.config.get('openai', 'model')

    @property
    def base_url(self):
        return self.config.get('openai', 'base_url')

global_config = GlobalConfig()