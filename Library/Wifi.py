from math import log10
from wifi import Cell, Scheme
def retrieve():
    data = Cell.all('wlan0')
    return data
def dBm_meter(dBm,MHz):
    FSPL = 27.55
    MHz = int(MHz)
    m =  10 ** (( FSPL - (20 * log10(MHz)) + dBm ) / 20 )
    return m

if __name__ == '__main__':
    for i in retrieve():
        print (i.ssid,i.address,i.signal)
