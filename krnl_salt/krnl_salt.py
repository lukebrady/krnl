#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import salt.client.ssh.client as salt_ssh

client = salt_ssh.SSHClient()

command = client.cmd('*','echo Hello from $(hostname)')

print(command)




