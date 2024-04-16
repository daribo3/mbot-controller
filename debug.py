# from makeblock import MegaPi

import signal

# def run():
#     print("starting")
#     megapi = MegaPi.connect()


# if __name__ == "__main__":
#     print("hi")
#     run()

import megapi
import time

FRONT_LEFT = 10
FRONT_RIGHT = 1
REAR_LEFT = 2
REAR_RIGHT = 9

FRONT_LEFT_FORWARD = -1
FRONT_LEFT_BACKWARD = 1
FRONT_RIGHT_FORWARD = 1
FRONT_RIGHT_BACKWARD = -1
REAR_LEFT_FORWARD = -1
REAR_LEFT_BACKWARD = 1
REAR_RIGHT_FORWARD = 1
REAR_RIGHT_BACKWARD = -1

SPEED = 100


def stop_all(bot):
    bot.motorRun(FRONT_LEFT, 0)
    bot.motorRun(FRONT_RIGHT, 0)
    bot.motorRun(REAR_LEFT, 0)
    bot.motorRun(REAR_RIGHT, 0)


def forward(bot):
    bot.motorRun(FRONT_LEFT, SPEED * FRONT_LEFT_FORWARD)
    bot.motorRun(FRONT_RIGHT, SPEED * FRONT_RIGHT_FORWARD)
    bot.motorRun(REAR_LEFT, SPEED * REAR_LEFT_FORWARD)
    bot.motorRun(REAR_RIGHT, SPEED * REAR_RIGHT_FORWARD)


def reverse(bot):
    bot.motorRun(FRONT_LEFT, SPEED * FRONT_LEFT_BACKWARD)
    bot.motorRun(FRONT_RIGHT, SPEED * FRONT_RIGHT_BACKWARD)
    bot.motorRun(REAR_LEFT, SPEED * REAR_LEFT_BACKWARD)
    bot.motorRun(REAR_RIGHT, SPEED * REAR_RIGHT_BACKWARD)


def strafe_left(bot):
    bot.motorRun(FRONT_LEFT, SPEED * FRONT_LEFT_BACKWARD)
    bot.motorRun(FRONT_RIGHT, SPEED * FRONT_RIGHT_FORWARD)
    bot.motorRun(REAR_LEFT, SPEED * REAR_LEFT_FORWARD)
    bot.motorRun(REAR_RIGHT, SPEED * REAR_RIGHT_BACKWARD)


def strafe_right(bot):
    bot.motorRun(FRONT_LEFT, SPEED * FRONT_LEFT_FORWARD)
    bot.motorRun(FRONT_RIGHT, SPEED * FRONT_RIGHT_BACKWARD)
    bot.motorRun(REAR_LEFT, SPEED * REAR_LEFT_BACKWARD)
    bot.motorRun(REAR_RIGHT, SPEED * REAR_RIGHT_FORWARD)


def rotate_left(bot):
    bot.motorRun(FRONT_LEFT, SPEED * FRONT_LEFT_BACKWARD)
    bot.motorRun(FRONT_RIGHT, SPEED * FRONT_RIGHT_FORWARD)
    bot.motorRun(REAR_LEFT, SPEED * REAR_LEFT_BACKWARD)
    bot.motorRun(REAR_RIGHT, SPEED * REAR_RIGHT_FORWARD)


def rotate_right(bot):
    bot.motorRun(FRONT_LEFT, SPEED * FRONT_LEFT_FORWARD)
    bot.motorRun(FRONT_RIGHT, SPEED * FRONT_RIGHT_BACKWARD)
    bot.motorRun(REAR_LEFT, SPEED * REAR_LEFT_FORWARD)
    bot.motorRun(REAR_RIGHT, SPEED * REAR_RIGHT_BACKWARD)


if __name__ == "__main__":
    b = megapi.MegaPi()
    b.start("/dev/ttyUSB0")
    time.sleep(1)

    # stop_all(bot)
    # time.sleep(0.5)

    try:
        forward(b)
        time.sleep(0.5)
        reverse(b)
        time.sleep(0.5)
        strafe_left(b)
        time.sleep(0.5)
        strafe_right(b)
        time.sleep(0.5)
        rotate_left(b)
        time.sleep(0.5)
        rotate_right(b)
        time.sleep(0.5)
    finally:
        stop_all(b)
        b.close()
        b.exit(signal.SIGINT, None)

    print("Done")
