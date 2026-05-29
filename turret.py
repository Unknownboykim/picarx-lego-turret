from robot_hat import ADC, Servo
import time

vry = ADC("A3")
servo = Servo("P3")

print("Turret ready! Move joystick left and right")
print("Press Ctrl+C to stop")

def map_value(value, in_min, in_max, out_min, out_max):
    value = max(in_min, min(in_max, value))
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

try:
    while True:
        vry_val = vry.read()
        angle = map_value(vry_val, 72, 3974, -90, 90)
        angle = int(angle)
        servo.angle(angle)
        print("VRY:", vry_val, " Angle:", angle)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopping")
    servo.angle(0)


