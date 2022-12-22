
def camera_movement(str,report,ar):
    a = 0
    if report:
        a = report[ar]*0.70
        str.angle = 90 - a

def linear_movement(str,str1,str2,str3,report,ar):  #Without Speed Control
    a = 0
    if report:
        if report[ar]<75:
            str.on()
            str2.on()

        elif report[ar]>210:
            str1.on()
            str3.on()

def angular_movement(str,str1,str2,str3,report,ar):
    if report:
        if report[ar]<32:
            str.on()
            str3.on()

        if report[ar]>223:
            str1.on()
            str2.on()
