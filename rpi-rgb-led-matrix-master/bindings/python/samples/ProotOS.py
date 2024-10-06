#!/usr/bin/env python
from samplebase import SampleBase


class OsProot(SampleBase):
    def __init__(self, *args, **kwargs):
        super(OsProot, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()

        #Define colours
        red =   RGBColour(red = 255, green=   0, blue=   0)
        green = RGBColour(red =   0, green= 255, blue=   0)
        blue =  RGBColour(red =   0, green=   0, blue= 255)
        off  =  RGBColour(red =   0, green=   0, blue=   0)

        #Define matrices
        #Normal Face
        faceNormal = [[red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red],
                      [off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off],
                      [red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red],
                      [off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off],
                      [red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red],
                      [off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off],
                      [red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red],
                      [off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off],
                      [red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red],
                      [off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off],
                      [red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red],
                      [off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off],
                      [red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red],
                      [off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off],
                      [red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red],
                      [off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off],
                      [red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red],
                      [off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off],
                      [red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red],
                      [off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off],
                      [red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red],
                      [off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off],
                      [red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red],
                      [off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off],
                      [red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red],
                      [off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off],
                      [red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red],
                      [off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off],
                      [red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red],
                      [off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off],
                      [red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red],
                      [off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off, off, red, off, off]]
        
        #Boop

        #Angy

        #Happy

        #Crash

        #Confused

        #Sleepy

        while True:
            offset_canvas.Clear()

            face = faceNormal

            for x in face:
                for i in (face[x]):
                    colour = face[x][i]
                    offset_canvas.SetPixel(x, i, colour.red, colour.green, colour.blue)
                    #offset_canvas.SetPixel(x, i, face[x][i][0], face[x][i][1], face[x][i][2])

            for x in range(0, self.matrix.width): #Was macht das??
                offset_canvas.SetPixel(x, x, 255, 255, 255)
            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)#Brauch ich das?


class RGBColour():
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue 

# Main function
if __name__ == "__main__":
    Proot_OS = OsProot()
    if (not Proot_OS.process()):
        Proot_OS.print_help()
