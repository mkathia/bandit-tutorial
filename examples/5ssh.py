# Connecting to SSH without verifying host key
import paramiko

def insecure_ssh_login():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Insecure: skips host authenticity check
    ssh.connect("192.168.1.100", username="user", password="pass")
    stdin, stdout, stderr = ssh.exec_command("uptime")
    print(stdout.read().decode())
    ssh.close()

insecure_ssh_login()
