import subprocess

def start_hotspot():
    subprocess.run([
        "nmcli", "device", "wifi", "hotspot",
        "ifname", "wlan0",
        "con-name", "ECLEANING-PI",
        "ssid", "ECLEANING-PI",
        "password", "eclean123"
    ], check=False)

    print("[WIFI] Hotspot started via NetworkManager")

start_hotspot()


#I have checked till step 7 and gave system a restart. after reboot tried to start wifi_ap.py and same error came. 
# when i manually connect the hotspot station as it is already created  then it is running and showing 
# {Device 'wlan0' successfully activated with 'c5ef0d17-1df4-47bb-8ad8-bd7ac0faa52c'.
# Hint: "nmcli dev wifi show-password" shows the Wi-Fi name and password.
# [WIFI] Hotspot started via NetworkManager}