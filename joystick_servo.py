from robot_hat import ADC, Servo
from time import sleep

vry = ADC("A3")
servo = Servo("P3")
servo.angle(0)
sleep(1)

print("Move joystick left and right!")
print("Ctrl+C to stop")

try:
    while True:
        vry_val = vry.read()

        if vry_val > 3500:
            angle = -90
        elif vry_val < 500:
            angle = 90
        elif 2000 < vry_val < 3000:
            angle = 0
        else:
            angle = int((vry_val - 2500) / 2500 * 90)

        servo.angle(angle)
        print("VRY:", vry_val, "Angle:", angle)
        sleep(0.1)

except KeyboardInterrupt:
    print("Stopping")
    servo.angle(0)
