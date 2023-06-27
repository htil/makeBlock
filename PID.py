import cyberpi # Import the cyberpi library
from cyberpi import mbot2
from cyberpi import ultrasonic2
cyberpi.console.print("hello")
# mbot2.EM_set_power(100, "all")

DesiredState = 0
Kp = 0
Ki = 0
Kd = 0
KiTotal = 0
priorError = 0
Error = 0
Propotional = 0
Integral = 0
Derivative = 0
preError = 0
PID = 0
SensorDistance = 0

def on_start():
    global DesiredState, Kp, Ki, Kd, KiTotal, priorError, Error, Propotional, Integral, Derivative, preError, PID, SensorDistance
    DesiredState = 15
    Kp = 0.7
    Ki = 0
    Kd = 0
    priorError = 0
    KiTotal = 0
    while True:
        SensorDistance = cyberpi.ultrasonic2.get(1)
        if SensorDistance < 30:
            Error = (DesiredState - SensorDistance)
            Propotional = Kp * Error
            KiTotal = (KiTotal + Error)
            Integral = Ki * KiTotal
            Derivative = ((Error - preError)) * Kd
            preError = Error
            PID = ((Propotional + ((Integral + Derivative)))) * -1
            mbot2.EM_set_power((20 + PID),"EM1")
            mbot2.EM_set_power((-20 + PID),"EM2")

        else:
            mbot2.drive_power(30, -20)

on_start()
