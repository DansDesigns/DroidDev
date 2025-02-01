#!/bin/bash
# From: https://gist.github.com/jadonk/0e4a190fc01dc5723d1f183737af1d83

# Connect the display before running this.
export LED=51         # P9_16


# This is for the Pocket SPI 0
export RESET=57     # RESET - P2.06
export DC=58        # D/C   - P2.04
export CS=5         # CS    - P1.06
export BUS=0        # SPI bus 0

echo SPI $BUS

sudo bash << EOF
    # Remove the framebuffer modules
    #if lsmod | grep -q 'fbtft_device ' ; then rmmod fbtft_device;  fi
    #if lsmod | grep -q 'fb_st7735 '   ; then rmmod --force fb_st7735;    fi
    #if lsmod | grep -q 'fbtft '        ; then rmmod --force fbtft;         fi

    # Set the pinmuxes for the display
    # Pocket SPI 0
    config-pin P2.04 gpio   # D/C 40
    config-pin P2.06 gpio   # RESET 46
    config-pin P1.12 spi    # spi 0_d1 MOSI
    config-pin P1.10 spi    # spi 0_d0 MISO
    config-pin P1.08 spi_sclk # spi 0_sclk
    config-pin P1.06 spi_cs # spi 0_cs0
    

    # LED pin, turn on
    #./LCD-backlight.py
    
    sleep 0.1
    
    # Insert the framebuffer modules
    # Change busnum to the SPI bus number
    #modprobe fbtft_device name=sainsmart18 busnum=0 rotate=0 gpios=reset:$RESET,dc:$DC cs=0
    modprobe fbtft_device name=fb_ili9488 busnum=0 debug=7 verbose=3 rotate=0 gpios=reset:$RESET,dc:$DC cs=0

    # Turn off cursor
    while [ ! -e /dev/fb0 ]
    do
      echo Waiting for /dev/fb0
      sleep 1
    done

     echo 0 > /sys/class/graphics/fbcon/cursor_blink 

EOF
