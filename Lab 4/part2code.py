import time
import board
import busio
import adafruit_ssd1306
import adafruit_mpr121
import pygame
from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
pygame.mixer.init()
do = pygame.mixer.Sound('/home/pi/Interactive-Lab-Hub/Lab 4/sound/do.wav')
re = pygame.mixer.Sound('/home/pi/Interactive-Lab-Hub/Lab 4/sound/re.wav')
mi = pygame.mixer.Sound('/home/pi/Interactive-Lab-Hub/Lab 4/sound/mi.wav')
fa = pygame.mixer.Sound('/home/pi/Interactive-Lab-Hub/Lab 4/sound/fa.wav')
sol = pygame.mixer.Sound('/home/pi/Interactive-Lab-Hub/Lab 4/sound/sol.wav')
la = pygame.mixer.Sound('/home/pi/Interactive-Lab-Hub/Lab 4/sound/la.wav')
si = pygame.mixer.Sound('/home/pi/Interactive-Lab-Hub/Lab 4/sound/si.wav')

while True:
      if mpr121[5].value:
         do.play()
         oled.fill(0)
         oled.show()
         image = Image.new("1", (oled.width, oled.height))
         draw = ImageDraw.Draw(image)
         draw.text((50, 15), "do", fill=255)
         oled.image(image)
         oled.show()
      if mpr121[4].value:
         re.play()
         oled.fill(0)
         oled.show()
         image = Image.new("1", (oled.width, oled.height))
         draw = ImageDraw.Draw(image)
         draw.text((50, 15), "re", fill=255)
         oled.image(image)
         oled.show()
      if mpr121[3].value:
         mi.play()
         oled.fill(0)
         oled.show()
         image = Image.new("1", (oled.width, oled.height))
         draw = ImageDraw.Draw(image)
         draw.text((50, 15), "mi", fill=255)
         oled.image(image)
         oled.show()
      if mpr121[2].value:
         fa.play()
         oled.fill(0)
         oled.show()
         image = Image.new("1", (oled.width, oled.height))
         draw = ImageDraw.Draw(image)
         draw.text((50, 15), "fa", fill=255)
         oled.image(image)
         oled.show()
      if mpr121[1].value:
         sol.play()
         oled.fill(0)
         oled.show()
         image = Image.new("1", (oled.width, oled.height))
         draw = ImageDraw.Draw(image)
         draw.text((50, 15), "so", fill=255)
         oled.image(image)
         oled.show()
      if mpr121[0].value:
         la.play()
         oled.fill(0)
         oled.show()
         image = Image.new("1", (oled.width, oled.height))
         draw = ImageDraw.Draw(image)
         draw.text((50, 15), "la", fill=255)
         oled.image(image)
         oled.show()
      if mpr121[7].value:
         si.play()
         oled.fill(0)
         oled.show()
         image = Image.new("1", (oled.width, oled.height))
         draw = ImageDraw.Draw(image)
         draw.text((50, 15), "si", fill=255)
         oled.image(image)
         oled.show()
      time.sleep(0.1)

            
            #print(f"Twizzler {i} touched!")
    #time.sleep(0.2)  # Small delay to keep from spamming output messages.

#while True:
#    if mpr121[0].value:

