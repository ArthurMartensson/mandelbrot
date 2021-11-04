from PIL import Image as im
import numpy as np

mres = np.loadtxt("output/mres.txt", dtype = int)

image = im.fromarray(mres.astype("uint8"))
image.save("output/image.png")
