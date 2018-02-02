import numpy as np
import scipy.misc
import random
for i1 in range(1, 4):
    for i2 in range(1, 4):
        for i3 in range(1, 4):
            img = np.asarray([[[int(i1 * 256 / 4.0), int(i2 * 256 / 4.0), int(i3 * 256 / 4.0)]]], np.uint8)
            img = scipy.misc.imresize(img, 100.0)
            scipy.misc.imsave('./raw/%d%d%d.jpg' % (i1, i2, i3), img)
