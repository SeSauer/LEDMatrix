from flask import Flask, render_template, request
import serial
from Colors import *
from ColorMatrix import ColorMatrix

app = Flask(__name__)


SERIAL = serial.Serial("/dev/ttyACM1", 230400, timeout= None)
SIZE = 12
PIXELCOUNT = SIZE*SIZE
MATRIX = ColorMatrix(SIZE)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/write_coordinates', methods=['POST'])
def write_coordinates():
    x = request.form['x']
    y = request.form['y']
    color = request.form['color']
    # log coords and color
    with open('log.txt', 'a') as f:
        f.write(f'{x},{y},{color}\n')
    # send coords to serial

    MATRIX.setPixel(int(x),int(y),Color(hex2RGB(color)[0],hex2RGB(color)[1],hex2RGB(color)[2]))
    MATRIX.printSerial(SERIAL)
    return ''

def hex2RGB(color):
    #convert hex to separate RGB values
    RGB = [int(color[1:2], 16), int(color[3:4] , 16), int(color[5:6], 16)]
    return RGB

if __name__ == '__main__':
    app.run()
