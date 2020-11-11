import bluetooth
import time

print ("Checking for bluetooth devices...")

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))

for addr, name in nearby_devices:
    print("  {} - {}".format(addr, name))
    if name == "Spark 40 Audio":
        server_addr = addr

print ("Connecting to {}...".format(server_addr))

SERVER_PORT = 2

try:
    client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    client_socket.connect((server_addr, SERVER_PORT))
    print ("Connected successfully")

    TONE_1 = "01fe000053fe1a000000000000000000f00124000138000000f779"
    TONE_2 = "01fe000053fe1a000000000000000000f00123010138000001f779"
    TONE_3 = "01fe000053fe1a000000000000000000f00125020138000002f779"
    TONE_4 = "01fe000053fe1a000000000000000000f00120030138000003f779"
    tones = [TONE_1,TONE_2,TONE_3,TONE_4]
    
    for count in range(20):
        msg = bytes.fromhex(tones[count % 4])
        client_socket.send(msg)
        time.sleep (1)

except OSError as e:
    print(e)

finally:
    if client_socket is not None:
        client_socket.close()

