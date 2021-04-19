import pyqrcode
from pyqrcode import QRCode
import png

link = input("Vlož odkaz :")
url = pyqrcode.create(link)
url.png ('myqr.png', scale = 6)
