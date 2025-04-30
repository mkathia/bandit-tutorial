# Insecure creation of a credentials file with overly broad permissions
import os

def save_credentials_insecure():
    credentials = "username=admin\npassword=P@ssw0rd!\n"
    filepath = "credentials.txt"

    with open(filepath, "w") as f:
        f.write(credentials)

    # Insecure: Sets file to be readable, writable, and executable by anyone
    os.chmod(filepath, 0o777)

    print(f"Credentials saved to {filepath} with world-readable permissions.")

save_credentials_insecure()
