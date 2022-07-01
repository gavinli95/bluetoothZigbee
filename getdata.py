import serial
from playsound import playsound
import time
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import pandas as pd
import seaborn as sns

saveroot = "./7/"
root = "/dev/cu."
master_port = root + "usbmodem0011"
slave_ports = ["usbmodem2", "usbmodem3", "usbmodem4",
                      "usbmodem5", "usbmodem6", "usbmodem7",
                      "usbmodem8", "usbmodem9", "usbmodem10",
                      "usbmodem11", "usbmodem12", "usbmodem13",
                      "usbmodem14", "usbmodem15", "usbmodem16", "usbmodem17"]
slave_ports = [root + k for k in slave_ports]
print(slave_ports)
master = serial.Serial(master_port, 115200)
slaves = []
for port in slave_ports:
    slaves.append(serial.Serial(port, 115200, timeout=1))

i = 1
while i <= 199:
    datas = []
    if i % 2 == 0:
        master.write(b"start")
        time.sleep(1.6)
    else:
        playsound("./okgooglepred.wav", False)
        time.sleep(0.433)
        master.write(b"start")
        time.sleep(1.2)
    success = True
    for slave in slaves:
        data = []
        for j in range(0, 16):
            slave.write(b"send")
            tmp = []
            tmp += slave.read(100)

            if len(tmp) == 0:
                success = False
                break
            data += tmp
        slave.close()
        slave.open()
        if success:
            datas.append(data)
        else:
            break
    if success:
        datas = -np.array(datas)
        mdic = {"data": datas}
        if i % 2 == 0:
            sio.savemat(saveroot + "idle_" + str(i) + ".mat", mdic)
            time.sleep(15)
        else:
            sio.savemat(saveroot + "busy_" + str(i) + ".mat", mdic)
            time.sleep(15)
        print(i)
        i += 2
    else:
        time.sleep(15)
        continue

