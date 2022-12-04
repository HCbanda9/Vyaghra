import hid

gamepad = hid.device()
gamepad.open(0x045e,0x028e)
gamepad.set_nonblocking(True)
while True:
    report = gamepad.read(64)
    if report:
        print(report)