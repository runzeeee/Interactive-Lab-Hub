import time
import subprocess
import digitalio
import board
from time import strftime, sleep
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from adafruit_rgb_display.rgb import color565

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True


cupsOfCoffee = 0
hoursOfSleep = 0

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    #draw.text((0,10), strftime("%m/%d/%Y %H:%M:%S"), font=font, fill="#FFFFFF")
    # part E
    # Leecode year
    buttonA = digitalio.DigitalInOut(board.D23)
    buttonB = digitalio.DigitalInOut(board.D24)
    buttonA.switch_to_input()
    buttonB.switch_to_input()


    Day = strftime("%d") + " Times of Sunrise"
    Month = strftime("%m") + " Times Rent Paid"
    Year = str(int(strftime("%Y"))-2000) + " Years Old"
    
    def checkDayNight():
        if int(strftime("%H")) >= 6 and int(strftime("%H")) <= 18:
            return str(18 - int(strftime("%H")))  + " Hours Daylight Remain"
        else:
            if int(strftime("%H")) > 18 and int(strftime("%H")) <= 24:
                return str(24 - int(strftime("%H")) + 6)  + " Hours Darkness Remain"
            else:
                return str(6 - int(strftime("%H")))  + " Hours Darkness Remaining"

    def checkDaysremain():
        thirtyone = [1,3,5,7,8,10,12]
        thirty = [4,6,9,11]
        if int(strftime("%d")) == 2:
            return str(28 - int(strftime("%d")))  + " days before pay rent"
        elif int(strftime("%d")) in thirty:
            return str(30 - int(strftime("%m")))  + " days before pay rent"
        elif int(strftime("%d")) in thirtyone:
            return str(31 - int(strftime("%d")))  + " days before pay rent"

    def checksectonextday():
        return str(86400 - int(strftime("%H")) * 60 * 60 - int(strftime("%M")) * 60 - int(strftime("%S")))  + "s remain today"


    Hour = checkDayNight()
    MinuteSecond = str(int(strftime("%M")) * 60 + int(strftime("%S"))) + " Times Love U(Hourly)"

    SleepHours = str(hoursOfSleep) + " hours of sleep this week"
    CoffeeNum = str(cupsOfCoffee) + " cups of coffee consumed"
    
    if buttonA.value and buttonB.value: # defalt diplay
        #draw.text((0,10), Time, font=font, fill="#FFFFFF")
        y = top
        draw.text((x, y), Year, font=font, fill="#D0C1C6")
        y += font.getsize(Year)[1]
        draw.text((x, y), Month, font=font, fill="#69647B")
        y += font.getsize(Month)[1]
        draw.text((x, y), Day, font=font, fill="#92ACD1")
        y += font.getsize(Day)[1]
        draw.text((x, y), Hour, font=font, fill="#9FD4BE")
        y += font.getsize(Hour)[1]
        draw.text((x, y), MinuteSecond, font=font, fill="#F5A997")
        y += font.getsize(CoffeeNum)[1]
        draw.text((x, y), CoffeeNum, font=font, fill="#F5A997")
        y += font.getsize(SleepHours)[1]
        draw.text((x, y), SleepHours, font=font, fill="#F5A997")

    if buttonB.value and not buttonA.value:  # just button A pressed
    #    draw.text((0,10), checkDaysremain(), font=font, fill="#FFFFFF")  # set the screen to white
    #    addCoffee()
        cupsOfCoffee += 1
    if buttonA.value and not buttonB.value:  # just button B pressed
    #    draw.text((0,10), checksectonextday(), font=font, fill="#FFFFFF")  # set the screen to white
        hoursOfSleep += 1
    if not buttonA.value and not buttonB.value:  # All pressed
        draw.text((0,10), strftime("%m/%d/%Y %H:%M:%S"), font=font, fill="#0000FF")
    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
