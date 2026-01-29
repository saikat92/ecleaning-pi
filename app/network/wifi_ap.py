import subprocess


def start_hotspot():
    subprocess.run(["sudo", "systemctl", "stop", "NetworkManager"])
    subprocess.run(["sudo", "systemctl", "stop", "wpa_supplicant"])
    subprocess.run(["sudo", "ip", "link", "set", "wlan0", "down"])
    subprocess.run(["sudo", "iw", "dev", "wlan0", "set", "type", "__ap"])
    subprocess.run(["sudo", "ip", "link", "set", "wlan0", "up"])
    subprocess.run(["sudo", "systemctl", "start", "dnsmasq"])
    subprocess.run(["sudo", "systemctl", "start", "hostapd"])
    print("[WIFI] Hotspot started (AP mode forced)")




start_hotspot()

# SSID = "ECLEANING-PI"
# PASSWORD = "eclean123"


# def start_hotspot():
#     subprocess.run(["sudo", "systemctl", "start", "hostapd"])
#     subprocess.run(["sudo", "systemctl", "start", "dnsmasq"])
#     print("[WIFI] Hotspot started")


# def stop_hotspot():
#     subprocess.run(["sudo", "systemctl", "stop", "hostapd"])
#     subprocess.run(["sudo", "systemctl", "stop", "dnsmasq"])
#     print("[WIFI] Hotspot stopped")