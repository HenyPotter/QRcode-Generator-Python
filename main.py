import pyqrcode
from pyqrcode import QRCode
import png

s = input("Vlož odkaz :")
url = pyqrcode.create(s)
url.png ('myqr.png', scale = 6)
