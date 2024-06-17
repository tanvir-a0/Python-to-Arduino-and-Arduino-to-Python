import serial.tools.list_ports


ports = serial.tools.list_ports.comports()

serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

print(portList)
val = input("Select port: COM")
print(val)


for x in range(0, len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])
    


ser = serial.Serial(portVar, 9600, timeout=1)
ser.flush()

def receive_data():
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            break
            return line

def send_data(data):
    ser.write(data.encode('utf-8'))
    receive_data()

receive_data()
try:
    while True:
        send_data(input("Enter data: "))
except KeyboardInterrupt:
    print("Keyboard Interrupt")

ser.close()