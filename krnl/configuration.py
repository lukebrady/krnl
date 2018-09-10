import json, logging


# Configuration is a factory class that can dynamically return a configuration
# based on the parameter when i
class Configuration:
    def __init__(self, configuration):
        self.configuration = configuration
        self.log = logging.getLogger('config-log')

    # Method that is used to retrieve the configuration defined within the factory method.
    # GetConfiguaration can be used as a simple abstration to access configurations throughout
    # the code. As of right now storage and build are basically the same and one will be used
    # over the other. I am thinking about just creating a krnl.json configuration file.
    def GetConfiguration(self):
        if self.configuration == 'storage':
            storage_config = open('./config/storage_config.json').read()
            json_config = json.loads(storage_config)
            self.log.info('INFO: Returning storage configuration')
            return json_config
        elif self.configuration == 'build':
            storage_config = open('./config/build_config.json').read()
            json_config = json.loads(storage_config)
            self.log.info('INFO: Returning build configuration')
            return json_config
        elif self.configuration == 'hosts':
            host_config = open('../config/hosts.json').read()
            json_config = json.loads(host_config)
            self.log.info('INFO: Returning host configuration')
            return json_config
        else:
            self.log.error('ERROR: Could not fetch the ' + self.configuration + ' configuration')
            exit(code=1)
        exit(code=0)


if __name__ == '__main__':
    config = Configuration('storage')
    print(config.GetConfiguration())
