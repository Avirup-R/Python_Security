import subprocess

def run_registry_file(reg_file_path):
    try:
        # Use the 'regedit' command to import the registry file
        subprocess.run(['regedit', '/s', reg_file_path], check=True)
        print("Registry file imported successfully.")
    except subprocess.CalledProcessError:
        print("Error importing the registry file.")


def remove_website_rule(website):
    # PowerShell command to remove the outbound rule blocking the website
    powershell_command = f"Remove-NetFirewallRule -DisplayName 'Block {website}'"

    # Run the PowerShell command to remove the rule
    try:
        subprocess.run(["powershell", powershell_command], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Rule blocking {website} removed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)



if __name__ == "__main__":
    try:
        run_registry_file("enable_usb.reg")
        print("USB Enabled Successfully")

    except:
        print("Not able to Enable USB")

    try:
        run_registry_file("enable_bluetooth.reg")
        print("Bluetooth Enabled Successfully")

    except:
        print("Not able to Enable Bluetooth")

    try:
        run_registry_file("enable_cmd.reg")
        print("Command Prompt Enabled Successfully")

    except:
        print("Not able to Enable Command Prompt")

    remove_website_rule("157.240.192.35")