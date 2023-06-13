from flask import Flask, render_template, request
import serial
from Colors import *
from ColorMatrix import ColorMatrix
import json
import serial.tools.list_ports
from flask import session

app = Flask(__name__)

app.secret_key = b'penis'

SIZE = 12
PIXELCOUNT = SIZE*SIZE
MATRIX = ColorMatrix(SIZE)

@app.route('/serial_devices')
def get_serial_devices():
    ports = [port.device for port in serial.tools.list_ports.comports()]
    return json.dumps(ports)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clear', methods=['POST'])
def clear():
    serial_dev = serial.Serial(session.get('serial_device'), 230400, timeout= None)
    MATRIX.clear()
    MATRIX.printSerial(serial_dev)
    return ''

@app.route('/write_coordinates', methods=['POST'])
def write_coordinates():
    x = request.form['x']
    y = request.form['y']
    color = request.form['color']
    # log coords and colors
    print(f'{x},{y},{color}')
    with open('log.txt', 'a') as f:
        f.write(f'{x},{y},{color}\n')
    # send coords to serial
    MATRIX.setPixel(int(x),int(y),Color(hex2RGB(color)[0],hex2RGB(color)[1],hex2RGB(color)[2]))
    MATRIX.printSerial(serial_dev)
    return ''

def hex2RGB(color):
    #convert hex to separate RGB values
    RGB = [int(color[1:2], 16), int(color[3:4] , 16), int(color[5:6], 16)]
    return RGB

if __name__ == '__main__':
    app.run()
