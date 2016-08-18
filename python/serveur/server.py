# coding: utf-8

from flask import Flask, render_template
import RPi.GPIO as GPIO
import datetime
app=Flask(__name__)

GPIO.setmode(GPIO.BCM)

@app.route("/")
def hello():
    now=datetime.datetime.now()
    timeString=now.strftime("%d-%m-%Y %H:%M")
    templateData= {
        'title': 'HELLO!',
        'time': timeString
        }
    return render_template('main.html', **templateData)

@app.route("/readPin/<pin>")
def readPin(pin):
    try:
        GPIO.setup(int(pin),GPIO.IN)
        if GPIO.input(int(pin)) == True:
            rep = "La broche "+pin+u" est à l'état bas"
        else:
            rep = "La broche "+pin+u" est à l'état haut"
    except:
        rep = "Erreur lors de la lecture de la broche "+pin+ "."


    templateData= {
        'title': 'Etat de la broche '+pin,
        'reponse': rep
        }
    return render_template('pin.html', **templateData)



if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port=80, debug=True) 

