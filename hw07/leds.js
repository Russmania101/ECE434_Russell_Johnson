#!/usr/bin/env node
// Blinks various LEDs
const Blynk = require('/usr/lib/node_modules/blynk-library');
const b = require('bonescript');
const util = require('util');

const LED0 = 'USR3';
const LED1 = 'P9_14';
const button = 'P9_25';
b.pinMode(LED0, b.OUTPUT);
b.pinMode(LED1, b.OUTPUT);
b.pinMode(button, b.INPUT);

const AUTH = '0403f29876e84df397337d27bea55e18';


var blynk = new Blynk.Blynk(AUTH);

var v0 = new blynk.VirtualPin(0);
var v10 = new blynk.WidgetLED(10);
var v2 = new blynk.VirtualPin(2);

var slider_value;
v2.on('write', function(slider_value) {
    b.analogWrite(LED1, parseFloat(slider_value));
});

v0.on('write', function(param) {
    console.log('V0:', param[0]);
    b.digitalWrite(LED0, param[0]);
});

v10.setValue(0);    // Initiallly off

b.attachInterrupt(button, toggle, b.CHANGE);

function toggle(x) {
    console.log("V10: ", x.value);
    x.value ? v10.turnOff() : v10.turnOn();
}
