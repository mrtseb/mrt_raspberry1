{$mode objfpc}{$H+}
PROGRAM test;

USES crt, rpi;

VAR
  gpio: TGPIO;

BEGIN

clrscr();
gpio.init;

gpio.setup(24, OUTPUT);
gpio.setup(25, OUTPUT);

gpio.digitalWrite(25,HIGH);
delay(1500);
gpio.digitalWrite(25,LOW);
delay(1500);

gpio.destroy;

END.
