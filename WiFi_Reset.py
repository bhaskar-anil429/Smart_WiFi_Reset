# Smart_WiFi_Reset
#use onion omega and relay controller to reset your router
# relay baord https://www.controleverything.com/content/Relay-Controller?sku=PCA9536_I2CR_R11
# onion omega i2c shield https://www.controleverything.com/content/I2C-Master?sku=OOI2C

from OmegaExpansion import onionI2C
import time

import socket
i2c = onionI2C.OnionI2C()
i2c.writeByte(0x41, 0x03, 0x00)
time.sleep(0.5)
i2c.writeByte(0x41,0x01,0x01)
while True :
        REMOTE_SERVER = "www.onion.io"

        def is_connected():
         try:

                host = socket.gethostbyname(REMOTE_SERVER)

                s = socket.create_connection((host, 80), 2)
                return True

         except:
                pass
         return False
        if is_connected() :
                print "Connected to the internet...."

                i2c.writeByte(0x41, 0x01, 0x01)
                time.sleep(1)
        else :
                print " No internet ...."
                i2c.writeByte(0x41, 0x01, 0x00)
                time.sleep(1)

                i2c.writeByte(0x41, 0x01, 0x01)

                time.sleep(60)


        time.sleep(100)
