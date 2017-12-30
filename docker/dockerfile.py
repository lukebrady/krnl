from subprocess import call
from paramiko import SSHClient, SSHException


# Dynamically generate a Dockerfile
def generate_dockerfile(kernel_version):
    # Open Dockerfile to be written to. This will be used on the build server to
    # create an ephemeral build environment.

    dockerfile = open('./Dockerfile', 'w+')
    # dockerfile_string is the contents of the Dockerfile that will be generated at runtime.
    dockerfile_string  = 'FROM centos:latest\n'
    dockerfile_string += 'RUN yum install -y gcc make git ctags ncurses-devel openssl-devel bc openssl\n'
    dockerfile_string += 'RUN mkdir ~/krnl_workspace/\n'
    dockerfile_string += 'COPY ./kernels/' + kernel_version  + ' /root/krnl_workspace/\n'
    dockerfile_string += 'RUN tar xzv /root/krnl_workspace/' + kernel_version + '\n'
    dockerfile_string += 'RUN cp ./config-3.10.0-693.11.1.el7.x86_64 ./' + kernel_version + '/.config'
    dockerfile_string += 'RUN cd ~/krnl_workspace/' + kernel_version + '; make\n'
    # Try to write to the Dockerfile and raise an exception if there is a failure.
    try:
        dockerfile.write(dockerfile_string)
    except IOError:
        raise print('ERROR: Could not write to Dockerfile')
        exit(code=1)
    exit(code=0)
    dockerfile.close()

# export_dockerfile sends your newly generated Dockerfile to the designated kernel build server.
def export_dockerfile(user, build_host):
    # Create a new SSH client that will be used to send the Dockerfile to the build server.
    # This server's key should already be in the known_hosts file.

    call(['scp', './Dockerfile', user + '@' + build_host + ':/etc/krnl/kernel-deploy'])


def build_docker_image(name, build_host):
    return




if __name__ == '__main__':
    # generate_dockerfile('linux-4.1.48.tar.xz')
    export_dockerfile('ltbrady', '192.168.33.14')