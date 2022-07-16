let Speed = 0
let Left_US = 0
let Right_US = 0
function Back () {
	
}
basic.forever(function () {
    basic.showLeds(`
        # . . . .
        . # . . .
        . . # . .
        . . . # .
        . . . . #
        `)
    Speed = 40
    kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor2, kitronik_motor_driver.MotorDirection.Forward, Speed)
    kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor1, kitronik_motor_driver.MotorDirection.Forward, Speed)
    Left_US = sonar.ping(
    DigitalPin.P3,
    DigitalPin.P6,
    PingUnit.Centimeters
    ) * 1.5
    basic.showLeds(`
        # . . . .
        # # . . .
        # # # . .
        # # # # .
        # # # # #
        `)
    basic.showNumber(Left_US)
    basic.pause(1000)
    Right_US = sonar.ping(
    DigitalPin.P9,
    DigitalPin.P13,
    PingUnit.Centimeters
    ) * 1.5
    basic.showLeds(`
        . . . . #
        . . . # #
        . . # # #
        . # # # #
        # # # # #
        `)
    basic.showNumber(Right_US)
    while (Left_US < 20 || Right_US < 20) {
        kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor2, kitronik_motor_driver.MotorDirection.Reverse, Speed)
        kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor1, kitronik_motor_driver.MotorDirection.Reverse, Speed)
        basic.showLeds(`
            # . . . #
            # . . # .
            # . # . .
            # # . . .
            # . . . .
            `)
        basic.showNumber(Left_US)
        basic.showLeds(`
            # . . . #
            . # . . #
            . . # . #
            . . . # #
            . . . . #
            `)
        basic.showNumber(Right_US)
    }
    basic.pause(1000)
})
