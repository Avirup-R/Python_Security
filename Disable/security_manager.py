import subprocess

def run_registry_file(reg_file_path):
    try:
        # Use the 'regedit' command to import the registry file
        subprocess.run(['regedit', '/s', reg_file_path], check=True)
        print("Registry file imported successfully.")
    except subprocess.CalledProcessError:
        print("Error importing the registry file.")


def block_website_with_firewall(website):
    # PowerShell command to create a new outbound rule to block the website
    powershell_command = f"New-NetFirewallRule -DisplayName 'Block {website}' -Direction Outbound -Action Block -RemoteAddress {website} -Enabled True"

    # Run the PowerShell command using subprocess
    try:
        subprocess.run(["powershell", powershell_command], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Facebook blocked successfully.")
    except subprocess.CalledProcessError as e:
        print("Not able to block Facebook")

if __name__ == "__main__":
    try:
        run_registry_file("disable_usb.reg")
        print("USB Disabled Successfully")

    except:
        print("Not able to Disable USB")

    try:
        run_registry_file("disable_bluetooth.reg")
        print("Bluetooth Disabled Successfully")

    except:
        print("Not able to Disable Bluetooth")

    try:
        run_registry_file("disable_cmd.reg")
        print("Command Prompt Disabled Successfully")

    except:
        print("Not able to Disable Command Prompt")

    block_website_with_firewall("157.240.192.35")