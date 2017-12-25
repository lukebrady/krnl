def generate_dockerfile(kernel_version):
    # Open Dockerfile to be written to. This will be used on the build server to
    # create an ephemeral build environment.

    dockerfile = open('./Dockerfile', 'w+')
    # dockerfile_string is the contents of the Dockerfile that will be generated at runtime.
    dockerfile_string  = 'FROM centos:latest\n'
    dockerfile_string += 'RUN yum install -y gcc make git ctags ncurses-devel openssl-devel\n'
    dockerfile_string += 'RUN mkdir ~/krnl_workspace/\n'
    dockerfile_string += 'COPY ./kernels/' + kernel_version  + ' ~/krnl_workspacen/\n'
    # Try to write to the Dockerfile and raise an exception if there is a failure.
    try:
        dockerfile.write(dockerfile_string)
    except IOError:
        raise print('ERROR: Could not write to Dockerfile')
        exit(code=1)
    exit(code=0)
    dockerfile.close()


if __name__ == '__main__':
    generate_dockerfile('linux-4.1.48.tar.xz')