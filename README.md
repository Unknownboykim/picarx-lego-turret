# PiCar-X Lego Turret 🤖

> **The first documented build of a custom joystick turret, 
> Lego armor, and breadboard integration on the 
> SunFounder PiCar-X robot car.**

No tutorial existed for this. I figured it out myself.

---

## 📹 Demo Video
[YouTube link here](https://www.youtube.com/watch?v=pMx2uCLGDFA)

---

## 🔥 What It Does

- ✅ Full Lego armor covering the chassis
- ✅ 9G servo turret controlled by physical joystick
- ✅ Lego missile launcher triggered by joystick button
- ✅ Mobile app control via SunFounder Controller
- ✅ Live camera streaming over WiFi
- ✅ Obstacle avoidance and line tracking still work
- ✅ Voice control through the app

---

## 🧰 Hardware Required

| Component | Purpose |
|---|---|
| SunFounder PiCar-X | Base robot car |
| Raspberry Pi 4/5 | Brain of the system |
| Robot HAT V4 | Controls servos and reads sensors |
| Joystick Module | Controls the turret servo |
| 9G Servo (SG90) | Turret pan and missile trigger |
| Lego bricks | Armor and turret structure |
| Female-to-Female jumper wires | Joystick to HAT connection |
| Zip ties | Mount turret to camera |

---

## 🔌 Wiring

### Joystick Module → Robot HAT

| Joystick Pin | Wire Color | HAT Pin |
|---|---|---|
| GND | Brown | A3 black pin (GND) |
| +5V | Red | A3 yellow pin (5V) |
| VRY | Yellow | A3 red pin (Signal) |
| SW Button | Green | D0 red pin (Signal) |

### 9G Servo → Robot HAT

| Servo Wire | HAT Pin |
|---|---|
| Brown (GND) | P3 black pin |
| Red (Signal) | P3 red pin |
| Yellow (5V) | P3 yellow pin |

### PiCar-X Factory Wiring (already connected)

| Pin | Connected To |
|---|---|
| P0 | Camera Pan servo |
| P1 | Camera Tilt servo |
| P2 | Steering servo |
| A0-A2 | Grayscale sensor |
| D2-D3 | Ultrasonic sensor |

---

## 💡 Key Problems I Solved

**Problem 1 — Connecting breadboard to Robot HAT:**
The HAT has no pass-through GPIO header. Solution: female-to-female jumper wires directly from the HAT's labeled ADC, Digital, and PWM pin rows.

**Problem 2 — Joystick analog input:**
I wasted few days trying to wire an MCP3008 SPI chip before discovering the Robot HAT already has a built-in 12-bit ADC. The joystick connects directly to ADC pin A3 with one wire.

**Problem 3 — Joystick center offset:**
The joystick resting position reads ~3976 out of 4113 instead of being centered at 2056. Fixed with a deadzone system in code.

**Problem 4 — Combining two Python programs:**
The SunFounder app control and joystick servo control were separate files. Merged into one loop in combined_app.py.

---

## 📁 Files

| File | Description |
|---|---|
| `combined_app.py` | Main program — app + joystick + servo all in one loop |
| `joystick_servo.py` | Standalone joystick servo control (no app) |
| `adctest.py` | Test joystick ADC readings |
| `joystick_test.py` | Test joystick values |
| `turret.py` | Servo turret test |
| `powercheck.py` | Check SPI/ADC power |

---

## ▶️ How To Run

**Full combined control (app + joystick + turret):**

---

## 📺 YouTube Channel

**[Unidentifiedboy1](https://www.youtube.com/@unidentifiedboygaming1747)**

Subscribe for more Raspberry Pi, robotics, and tech builds!

---

## 👤 Author

**Ryan Kim** (Unidentifiedboy1)
Computer Science and Business Administration
Northeastern University

- 🎥 YouTube: [Unidentifiedboy1](https://www.youtube.com/watch?v=pMx2uCLGDFA)
- 💻 GitHub: [Unknownboykim](https://github.com/Unknownboykim)

---

## ⭐ If this helped you build something cool, leave a star and subscribe to Azirath on YouTube!

# PiCar-X Lego Turret 🤖

> 📺 **Watch the full build video on YouTube: [Unidentifiedboy1](https://www.youtube.com/watch?v=pMx2uCLGDFA))**
