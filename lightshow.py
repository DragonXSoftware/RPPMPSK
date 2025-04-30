from machine import Pin
from time import sleep

# Define LED pins
blue_led = Pin(0, Pin.OUT)  # GP0
red_led = Pin(1, Pin.OUT)   # GP1

def flash_led(led, times, delay=0.3):
    for _ in range(times):
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)

while True:
    flash_led(blue_led, 3)
    flash_led(red_led, 3)
    sleep(0.5)  # Pause between cycles