# Image-Binarization-on-Pynq-Z2-using-VHDL-and-Python
This project implements image binarization, transforming grayscale images into binary (black-and-white) representations. Implemented on a SoC, it takes advantage of both the processor and fpga to increase the performance of the task executed.
The purpose of the project was to deepen my understanding of System on Chip concepts learned in class by applying them to solve a real-world problem.

## What does it do?
The embedded system I designed takes **an image in the .bmp format with a color depth of 24 bits, which is grayscale** and by using a threshold value, it converts the color of each pixel to be either white or black. <br><br>
<div align="center">
  <img src="pixels.bmp" alt="drawing" width="200"/> &emsp; &emsp;
  <img src="pixels_new.bmp" alt="drawing" width="200"/> <br>
</div>

## To run the project:
You will need to connect to the Pynq board. You can find more info about this [on this page](https://pynq.readthedocs.io/en/v2.2.1/getting_started/pynq_z2_setup.html). Once you have connected, access this link: [http://192.168.2.99:9090](http://192.168.2.99:9090) which will open Jupyter Notebook locally on the board. Here add in the same folder the following:
- PSpart.py
- pbi32_tested_prag_interr_v1.bit
- pbi32_tested_prag_interr_v1.hwh
- pixels.bmp <br>

After that you can run the code from the PSpart.py file and see the new generated image called pixels_new.bmp.

## To see the hardware implementation:
To see the hardware implementation, you need to install vivado. I used the 2020.1 version (I tried using the 2024.1 version and encountered problems); therefore, I do not guarantee it will work on other versions. Download **harware.zip** and extract all files. Create a new project in vivado, add the source: **prag_axi4stream32.vhd** and the folder of the block design: hardware/**dsg_tested_component32**. Now you can open dsg_tested_component32 to look at the design.


## Acknowledgments
I completed the project under the guidance of the teachers at the Technical University of Cluj-Napoca.
