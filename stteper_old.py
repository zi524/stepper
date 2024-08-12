#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

class StepperMotor:
    def __init__(self, step_pins,direction_c):
        self.step_pins = step_pins
        self.step_count = 8
        self.step_sequence = [
            [1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1]
        ]
        self.step_direction()
        self.step_counter = 0
        self.setup_pins()
    
    def step_dirction(self):
        try:
            self.step_dir = self.direction_c 
        except:
            print("Error in set direction")     
        
    def setup_pins(self):
        GPIO.setmode(GPIO.BCM)
        try:
            for pin in self.step_pins:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, False)
        except:
            print("Error in setting up GPIO pins")

    def step(self, wait_time=10):
        for pin in range(4):
            xpin = self.step_pins[pin]
            GPIO.output(xpin,self.step_sequence[self.step_counter][pin])

        self.step_counter += self.step_dir
        if self.step_counter >= self.step_count:
            self.step_counter = 0
        elif self.step_counter < 0:
            self.step_counter = self.step_count - 1

        time.sleep(wait_time / 1000.0)

    def run(self, steps, wait_time):
        for _ in range(steps):
            self.step(wait_time)

    def cleanup(self):
        GPIO.cleanup()

if __name__ == "__main__":
    step_pins = [1,2,3,4]
    direction_c=1           # Clockwise direction and -1 for anti clock wise direction
    motor = StepperMotor(step_pins,direction_c)
    try:
        wait_time = 10
        steps = 512
        motor.run(steps, wait_time)
    except:
        print("Solve the error")
    finally:
        motor.cleanup()
        print("Program exited cleanly")
