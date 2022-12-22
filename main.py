import hid
from gpiozero import AngularServo,LED
from gpiozero.pins.pigpio import PiGPIOFactory
from controller_input import camera_movement,linear_movement,angular_movement
import time
#Host's IP Address (In Our Case The Pi's Address)
factory = PiGPIOFactory(host='192.168.1.10')

#Controller Setup
gamepad = hid.device()
gamepad.open(0x045e,0x028e)
gamepad.set_nonblocking(True)

#Declaring The Servo Motors
hori_servo = AngularServo(15,min_pulse_width=0.0006, max_pulse_width=0.0023,pin_factory=factory)
vert_servo = AngularServo(3,min_pulse_width=0.0006, max_pulse_width=0.0023,pin_factory=factory)

#State Of The Motors(1 = In Motion , 0 = At Rest)
motor_state=0
servo_state=0

#Declaring The Motors
motor1_forward=LED(21,pin_factory=factory)
motor1_backward=LED(20,pin_factory=factory)
motor2_forward=LED(19,pin_factory=factory)
motor2_backward=LED(26,pin_factory=factory)

#Declaring The LED
led = LED(11,pin_factory=factory)
led_state = 0

while (True):
    report = gamepad.read(64)

    if report:

        if report[11]>11:
            if report[11]==28:
                motor1_forward.on()
                motor2_backward.on()
                time.sleep(0.0000000001)
                motor1_forward.off()
                motor2_backward.off()

            if report[11]==12:
                    motor1_backward.on()
                    motor2_forward.on()
                    time.sleep(0.0000000001)
                    motor1_backward.off()
                    motor2_forward.off()


        if report[5]<128 or report[5]>128:
            camera_movement(hori_servo,report,5)

        if report[7]<127 or report[7]>127:
            camera_movement(vert_servo,report,7)

        if report[9]<128 or report[9]>128:
            linear_movement(motor1_forward,motor1_backward,motor2_forward,motor2_backward,report,9)
            motor_state = 1
            continue

        if report[1]>128 or report[1]<128:
            angular_movement(motor1_forward,motor1_backward,motor2_forward,motor2_backward,report,1)
            motor_state = 1
            continue

        if motor_state==1:
            motor1_forward.off()
            motor1_backward.off()
            motor2_forward.off()
            motor2_backward.off()
            hori_servo.angle=0
            hori_servo.angle=0
            servo_state=0
            motor_state=0

        if report[10]==4:
            if led_state==0:
                led.on()
                led_state=1
            if led_state==1:
                led.off()
                led_state=0

        if motor_state==1:
            motor1_forward.off()
            motor1_backward.off()
            motor2_forward.off()
            motor2_backward.off()
            hori_servo.angle=0
            hori_servo.angle=0
            servo_state=0
            motor_state=0







