#!/usr/bin/python
# coding: utf-8


from flask import Flask, render_template
import RPi.GPIO as GPIO
app=Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


pins = {
    24: {'name': u'machine à café', 'state': GPIO.LOW},
    25: {'name': 'lampe', 'state': GPIO.LOW},
    }

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


@app.route("/")
def main():
    
    for pin in pins:
        pins[pin]['state'] = GPIO.input(pin)

    templateData= {
        'pins': pins
        }
    return render_template('main_lamp.html', **templateData)

@app.route("/<changePin>/<action>")
def action(changePin,action):
    try:
        changePin = int(changePin)
        deviceName = pins[changePin]['name']

        if action == "on":
            GPIO.output(changePin, GPIO.HIGH)
            rep = deviceName + u" est allumée"
        if action == "off":
            GPIO.output(changePin, GPIO.LOW)
            rep = deviceName + u" est éteinte"
        if action == "toggle":
            GPIO.output(changePin, not GPIO.input(changePin))
            rep = deviceName + u" est basculée"
        for pin in pins:
            pins[pin]['state'] = GPIO.input(pin)


    except:
        rep = "Erreur !"


    templateData= {
        'message': rep,
        'pins': pins
        }
    return render_template('main_lamp.html', **templateData)



if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port=80, debug=True) 

