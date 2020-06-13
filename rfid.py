from pn532 import PN532_SPI
import time
import blinkt

def show_graph(v, r, g, b):
    import math
    v *= blinkt.NUM_PIXELS
    for x in range(blinkt.NUM_PIXELS):
        if v < 0:
            r, g, b = 0, 0, 0
        else:
            r, g, b = [int(min(v,1.0) * c) for c in [r, g, b]]
        blinkt.set_pixel(x, r, g, b)
        v -= 1
    blinkt.show()
    return

def lightsUp(times,brightness,name,r,g,b):
    print(name)
    blinkt.set_brightness(brightness)
    for _ in range(times):
       blinkt.set_all(r,g,b)
       blinkt.show()
       time.sleep(3)
       blinkt.clear()
    return

def printUID(uid):
    print('Found card with UID:', [hex(i) for i in uid])
    return
        
def main():
    try:
        blinkt.set_clear_on_exit()
        blinkt.clear()
        legitRFIDs = {}
        legitRFIDs['rfid1'] = ['0x1', '0x2', '0x3', '0x4']
        legitRFIDs['rfid2'] = ['0x5', '0x6', '0x7', '0x8']  
        rfid = PN532_SPI( debug=False, reset=20, cs=4 )
        ic, ver, rev, support = rfid.get_firmware_version()
        print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))
        print('ic: {0} and support: {1}'.format(ic,support))
        rfid.SAM_configuration()
        lightsUp(1,1,'Waiting for RFID/NFC card...',255,255,255)
        uid = rfid.read_passive_target()
        while uid != None:
            #v=(math.sin(time.time()) + 1) / 2
            #show_graph(v, 255, 0, 255)
            printUID(uid)
            if [hex(j) for j in uid] == legitRFIDs['rfid1']:
                lightsUp(3,0.5,'rfid1',128, 0, 128)
            elif [hex(j) for j in uid] == legitRFIDs['rfid2']:
                lightsUp(3,0.5,'rfid2',0,255,0)
            else:
                lightsUp(6,1,'This is an unrecognised RFID',255,0,0)
            time.sleep(0.1)
            uid = rfid.read_passive_target()
    except Exception as e:
        lightsUp(1,1,e,255,165,0)
    finally:
        blinkt.clear()
        lightsUp(2,1,'Bye.....',255,255,0)
        blinkt.clear()
        time.sleep(3)
    return    

if __name__ == '__main__':
    main()
