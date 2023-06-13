var selectedColor = '#FFFFFF'; // Default color is white

function populateSerialDevices(serialDevices) {
    var devicePicker = document.getElementById('device-picker');
    serialDevices.forEach(function(device) {
        var option = document.createElement('option');
        option.text = device;
        devicePicker.add(option);
    });
}

function loadSerialDevices() {
    fetch('/serial_devices')
        .then(response => response.json())
        .then(data => populateSerialDevices(data))
        .catch(error => console.error('Error:', error));
}

function writeCoordinates(x, y) {
    fetch('/write_coordinates', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `x=${x}&y=${y}&color=${selectedColor}`
    });

    var cell = document.getElementById(`cell-${x}-${y}`);
    cell.style.backgroundColor = selectedColor;
    }

function colorChanged() {
    var colorPicker = document.getElementById('color-picker');
    selectedColor = colorPicker.value;
}

function clearMatrix() {
    for (i = 0; i < 12; i++) {
        for (j = 0; j < 12; j++) {
            var cell = document.getElementById(`cell-${i}-${j}`);
            cell.style.backgroundColor = '#000000';
            fetch("/clear", {
                method: 'POST'
            });
        }
    }
}

function setSerialDevice() {
    var devicePicker = document.getElementById('device-picker');
    var selectedDevice = devicePicker.value;
    fetch('/set_serial_device', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ device: selectedDevice })
    })
        .then(response => {
            if (response.ok) {
                console.log('Serial device set successfully');
            } else {
                console.error('Error setting serial device');
            }
        })
        .catch(error => console.error('Error:', error));
}
