import docker, krnl_redis
from configuration import Configuration


class BuildEnvironment():
    def __init__(self):
        configuration = Configuration('build').GetConfiguration()
        self.docker_client = docker.from_env()
        self.redis_server = configuration.get('redis_server')
        self.redis_port = configuration.get('redis_port')
        self.database = configuration.get('database')

    def deploy_redis(self):
        if self.redis_server == 'localhost':
            self.docker_client.containers.run(image='krnl_redis:latest',
                                              name='krnl_redis',
                                              ports={self.redis_port: self.redis_port},
                                              detach=True)
            print("INFO: Redis has been deployed to localhost")
            exit(code=0)
        else:
            print('ERROR: Cannot deploy krnl_redis to ' + self.redis_server)
            exit(code=1)