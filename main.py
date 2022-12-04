import hid
from gpiozero import AngularServo,PWMLED,LED
from gpiozero.pins.pigpio import PiGPIOFactory
from controller_input import camera_movement,linear_movement

#Host's IP Address (In Our Case The Pi's Address)
factory = PiGPIOFactory(host='192.168.137.176')

#Controller Setup
gamepad = hid.device()
gamepad.open(0x045e,0x028e)
gamepad.set_nonblocking(True)

#Declaring The Servo Motors
hori_servo = AngularServo(2,min_pulse_width=0.0006, max_pulse_width=0.0023,pin_factory=factory)
vert_servo = AngularServo(21,min_pulse_width=0.0006, max_pulse_width=0.0023,pin_factory=factory)


#Declaring The Motors
motor1_forward=LED(4,pin_factory=factory)
motor1_backward=LED(14,pin_factory=factory)
while (True):
    report = gamepad.read(64)
    if report:
        if report[5]<128 or report[5]>128:
            camera_movement(hori_servo,report,5)

        if report[7]<127 or report[7]>127:
            camera_movement(vert_servo,report,7)

        if report[9]<128 or report[9]>128:
            linear_movement(motor1_forward,motor1_backward,report,9)


