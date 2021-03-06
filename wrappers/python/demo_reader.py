import sys, zxing
from PIL import Image

img = Image.open(sys.argv[1])
result = zxing.read_barcode(img)
if result.valid:
	print("Found barcode:\n Text:    '{}'\n Format:   {}\n Position: {}"
		.format(result.text, result.format, result.position))
else:
	print("Could not read barcode")
