from microbmp import MicroBMP
from pynq import Overlay
from pynq import allocate
from pynq.lib import AxiGPIO
import pynq.lib.dma
from pynq import Interrupt
import numpy as np
import time

print("Start")
alpha_value = 0

filepath = "./pixels.bmp"
new_bmp_file_name = "pixels_new.bmp"
prag = 128

###############################################################################
# Functions for working with .bmp file:

def pixel_info_bmp_to_buffer(image, buffer):
    index_aux = 0
    # Parcurgem bytearray-ul în grupuri de câte 3 bytes (R, G, B)
    for w in range(image.DIB_w):
        for h in range(image.DIB_h):
            # Extragem valorile R, G, B din bytearray
            b, g, r = image[w, h]

            # Combinăm în formatul (Alpha-R-G-B)
            pixel = (alpha_value << 24) | (r << 16) | (g << 8) | b
            buffer[index_aux] = pixel
            index_aux += 1

def pixel_info_buffer_to_bmp(buffer, image):
    for w in range(image.DIB_w):
        for h in range(image.DIB_h):
            pixel = buffer[w * image.DIB_h + h]
            # din pixelul returnat de PL, extrag componentele de culoare
            if pixel & np.uint64(0xff) == np.uint64(0):
                r = 0
                g = 0
                b = 0
            else:
                r = 0xff
                g = 0xff
                b = 0xff
            image[w, h] = r, g, b

# End functions for .bmp file
###############################################################################


overlay = Overlay("./pbi32_tested_prag_interr_v1.bit")

dma = overlay.axi_dma_0  # Initialize DMA for data transfer
print("Overlay - done")

######### PROCESARE IMAGINE
original_image = MicroBMP()
original_image.load(filepath)
print("Loaded file - done")

# alocare memorie buffere
buffer_length = (original_image.DIB_w * original_image.DIB_h)
input_buffer = allocate(shape=(buffer_length,), dtype=np.uint64)
output_buffer = allocate(shape=(buffer_length,), dtype=np.uint64)
print("Memory for buffers allocated - done")

pixel_info_bmp_to_buffer(original_image, input_buffer)
print("Pixels copyed to input_buffer - done")
# print(input_buffer)

dma.sendchannel.transfer(input_buffer)
dma.recvchannel.transfer(output_buffer)

dma.sendchannel.wait()
dma.recvchannel.wait()
print("PL processing - done")
# print(output_buffer)

new_image = MicroBMP(original_image.DIB_w, original_image.DIB_h, original_image.DIB_depth)
pixel_info_buffer_to_bmp(output_buffer, new_image)
new_image.save(new_bmp_file_name)

print("Binary Processing - done")