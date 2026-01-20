import qrcode

SSID = "ECLEANING-PI"
PASSWORD = "eclean123"


def generate_qr():
    wifi_string = f"WIFI:T:WPA;S:{SSID};P:{PASSWORD};;"
    img = qrcode.make(wifi_string)
    img.save("assets/qr.png")
    print("[QR] Wi‑Fi QR generated")