import subprocess

SSID = "ECLEANING-PI"
PASSWORD = "eclean123"


def start_hotspot():
    subprocess.run(["sudo", "systemctl", "start", "hostapd"])
    subprocess.run(["sudo", "systemctl", "start", "dnsmasq"])
    print("[WIFI] Hotspot started")


def stop_hotspot():
    subprocess.run(["sudo", "systemctl", "stop", "hostapd"])
    subprocess.run(["sudo", "systemctl", "stop", "dnsmasq"])
    print("[WIFI] Hotspot stopped")