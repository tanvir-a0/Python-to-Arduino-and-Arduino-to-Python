import serial.tools.list_ports
import time


class Serial_Communication_Arduino:
    def __init__(self, port=None,speed=9600, timeout=1):
        if port is None:
            raise ValueError("Port is required")
        self.port = port
        self.ser = serial.Serial(self.port, speed, timeout=timeout)
        self.ser.flush()
        time.sleep(0.2)
        self.status = self.receive_data() # Check if the connection is established (In the arduino if i set it for my project)
        print(self.status)

        
    def receive_data(self):
        while True:
            if self.ser.in_waiting > 0:
                line = self.ser.readline().decode('utf-8').rstrip()
                #print(line)
                #break
                return line

    def send_data(self,data):
        self.ser.write(data.encode('utf-8'))
        return self.receive_data()

    def close(self):
        print("Closing the connection")
        self.ser.close()

# ser1 = Serial_Communication_Arduino(port='COM4')
# print(ser1.send_data("find"))
# ser1.close()
