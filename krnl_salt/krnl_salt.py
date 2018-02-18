import salt.client.ssh.client as salt_ssh


class KernelSalt:
    def __init__(self):
        self.client = salt_ssh.SSHClient()

    def deploy_kernel(self):
        command = self.client.cmd('*', 'echo Hello from $(hostname)')
        print(command)
