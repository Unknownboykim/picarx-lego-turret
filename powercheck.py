import spidev
spi = spidev.SpiDev()
spi.open(10, 0)
spi.max_speed_hz = 1350000
adc = spi.xfer2([1, (8+0) << 4, 0])
print("Raw:", adc)
spi.close()


