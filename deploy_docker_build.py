import docker


# Pull latest CentOS image that will be used to create the kernel build container.
def pull_build_container():
    docker_client = docker.from_env()
    if docker_client.version() != None:
        print("INFO: Pulling latest centos docker image")
        docker_client.images.pull('centos:latest')
        print(docker_client.images.get('centos:latest'))
        exit(code=0)
    else:
        print('ERROR: Docker is not installed on the local machine.')
        print('ERROR: Exiting')
        exit(code=1)


if __name__ == '__main__':
    pull_build_container()
