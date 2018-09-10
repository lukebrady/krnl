import docker
from subprocess import call

# DestroyEnvironment removes a kernel environment from your machine. DestroyEnvironment will
# remove the redis database, all downloaded kernels, and all kernel metadata.
class DestroyEnvironment():
    def __init__(self):
        self.docker_client = docker.from_env()
    # This function will stop and remove the krnl redis docker container from the system.
    def destroy_redis(self):
        call(['docker', 'stop', 'redis'])
        try:
            call(['docker','rm','redis'])
            print("INFO: Redis has been removed from the system")
        except IOError:
            print('ERROR: Could not remove the redis container')
        exit(code=0)
