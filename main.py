import pyqrcode
from pyqrcode import QRCode
import png

link = input("Insert link:")
url = pyqrcode.create(link)
url.png ('myqr.png', scale = 6)
