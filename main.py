Speed = 0
Left_US = 0
Right_US = 0
def Back():
    pass

def on_forever():
    global Speed, Left_US, Right_US
    basic.show_leds("""
        # . . . .
                . # . . .
                . . # . .
                . . . # .
                . . . . #
    """)
    Speed = 40
    kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2,
        kitronik_motor_driver.MotorDirection.FORWARD,
        Speed)
    kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
        kitronik_motor_driver.MotorDirection.FORWARD,
        Speed)
    Left_US = sonar.ping(DigitalPin.P3, DigitalPin.P6, PingUnit.CENTIMETERS) * 1.5
    basic.show_leds("""
        # . . . .
                # # . . .
                # # # . .
                # # # # .
                # # # # #
    """)
    basic.show_number(Left_US)
    basic.pause(1000)
    Right_US = sonar.ping(DigitalPin.P9, DigitalPin.P13, PingUnit.CENTIMETERS) * 1.5
    basic.show_leds("""
        . . . . #
                . . . # #
                . . # # #
                . # # # #
                # # # # #
    """)
    basic.show_number(Right_US)
    while Left_US < 20 or Right_US < 20:
        kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2,
            kitronik_motor_driver.MotorDirection.REVERSE,
            Speed)
        kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
            kitronik_motor_driver.MotorDirection.REVERSE,
            Speed)
        basic.show_leds("""
            # . . . #
                        # . . # .
                        # . # . .
                        # # . . .
                        # . . . .
        """)
        basic.show_number(Left_US)
        basic.show_leds("""
            # . . . #
                        . # . . #
                        . . # . #
                        . . . # #
                        . . . . #
        """)
        basic.show_number(Right_US)
    basic.pause(1000)
basic.forever(on_forever)
