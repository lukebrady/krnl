import paramiko, redis, logging

from configuration import Configuration

def get_ssh_host_configuration():
    # Gets the host configuration that will be returned and used in later functions.
    host_configuration = Configuration('hosts').GetConfiguration()
    return host_configuration


def copy_ssh_id(user, password):
    logger = logging.getLogger('ssh-copy-id logger')
    host_config = Configuration('hosts')
    host_list = host_config.GetConfiguration()

    ssh_client = paramiko.SSHClient()

    for host in host_list.get('hosts'):
        print('INFO: Copying ID to ' + host)
        ssh_client.load_system_host_keys()
        ssh_client.connect(host, username=user, password=password)
        ssh_client.exec_command('mkdir ~/test')
        ssh_client.close()
    exit(code=0)


if __name__ == '__main__':
    copy_ssh_id('ltbrady','vagrant')
