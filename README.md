# picarx-lego-turret
Raspberry Pi PiCar-X robot with Lego armor, joystick-controlled servo turret, and mobile app control

# PiCar-X Lego Turret

First documented build of a custom joystick turret
and Lego armor on the SunFounder PiCar-X robot car.

## What It Does
- Full Lego armor on the chassis
- 9G servo turret controlled by physical joystick
- Lego missile launcher
- Mobile app control via SunFounder Controller
- Live camera streaming over WiFi

## Hardware
- SunFounder PiCar-X
- Raspberry Pi
- Robot HAT V4
- Joystick module
- 9G servo
- Lego bricks
- Jumper wires

## Wiring
| Joystick Pin | HAT Pin |
|---|---|
| GND | A3 black pin |
| 5V | A3 yellow pin |
| VRY | A3 red pin |
| SW | D0 red pin |

| Servo Wire | HAT Pin |
|---|---|
| Brown | P3 GND |
| Red | P3 Signal |
| Yellow | P3 5V |

## How To Run
cd ~/picar-x/example
sudo python3 combined_app.py

## Files
- combined_app.py - Main program combining app and joystick control
- joystick_servo.py - Standalone joystick servo control

## Author
Ryan Kim
Computer Science and Business Administration
Northeastern University
github.com/Unknownboykim
