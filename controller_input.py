
def camera_movement(str,report,ar):
    a = 0
    if report:
        a = report[ar]*0.7058823529411765
        str.angle = a - 90

def linear_movement(str,str1,str2,str3,report,ar):  #Without Speed Control
    a = 0
    if report:
        if report[ar]>75:
            str.on()
            str2.on()
            str1.off()
            str3.off()


        if report[ar]>210:
            str1.on()
            str3.on()
            str.off()

