import json

# Configuration is a factory class that can dynamically return a configuration
# based on the parameter when i
class Configuration:

    def __init__(self, configuration):
        self.configuration = configuration

    def GetConfiguration(self):
        if self.configuration == 'storage':
            storage_config = open("./config/storage_config.json").read()
            json_config = json.loads(storage_config)
            return json_config
        elif self.configuration == 'build':
            storage_config = open("./config/build_config.json").read()
            json_config = json.loads(storage_config)
            return json_config
        elif self.configuration == 'hosts':
            host_config = open('./config/hosts.json').read()
            json_config = json.loads(host_config)
            return json_config
        else:
            print('ERROR: Not a proper configuration')
            exit(code=1)
        exit(code=0)

if __name__ == '__main__':
    config = Configuration('storage')
    print(config.GetConfiguration())