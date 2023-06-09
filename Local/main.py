from flask import Flask, render_template, request

app = Flask(__name__)

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
    
    return ''

def hex2RGB(color):
    #convert hex to separate RGB values
    RGB = [int(color[1:2], 16), int(color[3:4] , 16), int(color[5:6], 16)]
    return RGB

if __name__ == '__main__':
    app.run()
