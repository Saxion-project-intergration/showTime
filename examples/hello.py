"""
hello.py

    Writes "Hello!" in random colors at random locations on the display

"""
import random
from machine import Pin, SPI
import gc9a01py as gc9a01
import time

# Choose a font

# from fonts import vga1_8x8 as font
# from fonts import vga2_8x8 as font
#from fonts.romfonts import vga1_8x16 as font
# from fonts import vga2_8x16 as font
# from fonts import vga1_16x16 as font
from fonts.romfonts import vga1_bold_16x16 as font
# from fonts import vga2_16x16 as font
# from fonts import vga2_bold_16x16 as font
# from fonts import vga1_16x32 as font
# from fonts import vga1_bold_16x32 as font
# from fonts import vga2_16x32 as font
#from fonts.romfonts import vga2_bold_16x32 as font

#=========================
TFT_BLK=26
TFT_CS=22
TFT_DC=21
TFT_RES=17
sck = Pin(27, Pin.OUT)
mosi = Pin(13, Pin.OUT)

print("BLK\t", TFT_BLK)
print("CD\t", TFT_CS)
print("DC\t", TFT_DC)
print("RES\t", TFT_RES)

spi = SPI(2, baudrate=10000000, sck=sck, mosi=mosi)
print(spi)
tft = gc9a01.GC9A01(
    spi,
    dc=Pin(TFT_DC, Pin.OUT),
    cs=Pin(TFT_CS, Pin.OUT),
    reset=Pin(TFT_RES, Pin.OUT),
    backlight=Pin(TFT_BLK, Pin.OUT),
    rotation=0)

background_color = gc9a01.color565(128, 128, 128)  # Grijs
text_color = gc9a01.color565(0, 0, 0)  # Zwart

#=========================

def main():
    """
    spi = SPI(2, baudrate=60000000, sck=Pin(18), mosi=Pin(23))
    tft = gc9a01.GC9A01(
        spi,
        dc=Pin(21, Pin.OUT),
        cs=Pin(13, Pin.OUT),
        reset=Pin(26, Pin.OUT),
        backlight=Pin(14, Pin.OUT),
        rotation=0)
    """

    while True:
        for rotation in range(8):
            
           # tft.rotation(rotation)
            tft.fill(0)
            col_max = tft.width 
            row_max = tft.height 
            for _ in range(1):
                tft.text(
                    font,
                    "Mooi werk",
                    50,
                    50,
                    text_color,
                    background_color
                )
                time.sleep(10)


main()
