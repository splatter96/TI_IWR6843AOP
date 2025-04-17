import numpy as np
from PIL import Image

import cv2

data = np.load("./data_image.npy")

data = np.nan_to_num(data, nan=0)
formatted = (data * 255 / np.max(data)).astype("uint8")

# img = Image.fromarray(formatted)
# img.show()

cv_img = cv2.cvtColor(formatted, cv2.COLOR_GRAY2BGR)

cv2.imshow("image", cv_img)
cv2.waitKey(0)
