from PIL import Image as im
import numpy as np

mres = np.loadtxt("output/mres.txt")
mres = 512/(1+np.exp(-mres/40)) - 253

mresr = mres.copy()/3
mresg = mres.copy()/2
mresb = mres

imager = im.fromarray(mresr.astype("uint8"))
imageg = im.fromarray(mresg.astype("uint8"))
imageb = im.fromarray(mresb.astype("uint8"))
image = im.merge("RGB", (imager, imageg, imageb))
image.save("output/image.png")
