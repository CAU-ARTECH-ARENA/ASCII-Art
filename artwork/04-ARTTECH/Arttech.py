import cv2

CHARS = ["C", "A", "U", "a", "r", "t", "e", "c", "h", "&", "#", "$", "*", "+", "."]
wi = 50

img = 'AT.png'
img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

h, w = img.shape
ji = int(h / w * wi)

img = cv2.resize(img, (wi * 2, ji))

for row in img:
    for pixel in row: 
        index = int(pixel / 256 * len(CHARS))
        print(CHARS[index], end='')

    print()
