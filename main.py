"""
Use threading to poll the sensors concurrently and call update every time there's new sensor data.

Only change this file.
"""

import time
import threading
import localization
import sensors
data = [0,0,0]
def worker1():
    data[0] = sensors.get_accelerometer_data()
def worker2():
    data[1] = sensors.get_camera_data()
def worker3():
    data[2] = sensors.get_gps_data()

state = sensors.get_gps_data()
last_update = time.monotonic()

while True:
    thread1 = threading.Thread(target=worker1)
    thread2 = threading.Thread(target=worker2)
    thread3 = threading.Thread(target=worker3)
    thread1.start()
    thread2.start()
    thread3.start()
    state = localization.update(
        state=state,
        acc_data=data[0],
        cam_data=data[1],
        gps_data=data[2],
    )
    time.sleep(2)
    now = time.monotonic()
    thread1.join()
    thread2.join()
    thread3.join()
    duration = now - last_update
    update_freq = 1 / duration
    last_update = now
    print(f"update frequency: {update_freq:.2f}, state: {state:.2f}")
