import socket

def android_connected():
    try:
        socket.gethostbyname("google.com")
        return True
    except:
        return False