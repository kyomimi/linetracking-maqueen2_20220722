#止まる
def maqStop():
    # maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 10)
    # maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 10)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)

#前に進む
def maqForward(kyori):
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
    if kyori > 0:
        basic.pause(6500*kyori)
        maqStop()
    else:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)

#後ろに下がる
def maqBackward(kyori):
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 253)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 180)
    if kyori > 0:
        basic.pause(6500*kyori)
        maqStop()
    else:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 253)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 180)

#右のLEDが点滅
def maqBlinkLedR():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_tone(Note.C,100)

    for i in range(3):
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
        basic.pause(100)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
        basic.pause(500)

#左のLEDが点滅
def maqBlinkLedL():
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(Note.E,100)

    for i in range(3):
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
        basic.pause(100)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
        basic.pause(100)
    pass


#右に曲がる
def maqTurnRight():
    maqBlinkLedR()
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 253)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
    basic.pause(750)
    maqStop()
    pass

#ハンドル操作で右に曲がる
def maqSteerRight():
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 170)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
    pass

#左に曲がる
def maqTurnLeft():
     maqBlinkLedL()
     maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
     maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 185)
     basic.pause(750)
     maqStop()
     pass

#ハンドル操作で左に曲がる
def maqSteerLeft():
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 170)
    pass

#右に曲がる(lineトレース用)
def maqSlightRight():
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 40)


#左に曲がる(lineトレース用)
def maqSlightLeft():
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)

#################################################################################################
def on_forever():
    
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0  and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        maqForward(0)
        # basic.show_string("S")

    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1  and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        maqSlightRight()
        # basic.show_string("R")

    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0  and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
        maqSlightLeft()
        # basic.show_string("L")
basic.forever(on_forever)





