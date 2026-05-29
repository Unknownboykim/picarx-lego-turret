from robot_hat import ADC
import time

vrx = ADC("A2")
vry = ADC("A3")

print("Move joystick!")

while True:
    x = vrx.read()
    y = vry.read()
    print("VRX:", x, " VRY:", y)
    time.sleep(0.2)
