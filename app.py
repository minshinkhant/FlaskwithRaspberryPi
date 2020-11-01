'''
	Raspberry Pi GPIO Status and Control
'''
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# define actuators GPIOs
ledRed = 13

# initialize GPIO status variables
ledRedSts = 0

# Define led pins as output
GPIO.setup(ledRed, GPIO.OUT)

# turn leds OFF
GPIO.output(ledRed, GPIO.LOW)


@app.route("/")
def index():

    templateData = {
        'title': 'GPIO output Status!',
        'ledRed': "Turn Off"
    }
    return render_template('index.html', **templateData)


@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'ledRed':
        actuator = ledRed
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)

    # Read Sensors Status
    ledRedSts = GPIO.input(ledRed)
    if ledRedSts == 0:
        led_status = "Turn Off"
    else:
        led_status = "Turn On"

    templateData = {
        'ledRed': led_status
    }
    return render_template('index.html', **templateData)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
