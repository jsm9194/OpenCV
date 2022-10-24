import cv2
import matplotlib.pyplot as plt

def img_show(title='image', img= None ,figsize=(8,5)):
    plt.figure(figsize=figsize)

    if type(img) == list:
        if type(title) == list:
            titles = title
        else:
            titles = []

            for i in range(len(img)):
                titles.append(title)

        for i in range(len(img)):
            if len(img[i].shape) <3:
                rgbImg = cv2.cvColor(img[i], cv2.COLOR_GRAY2RGB)
            else:
                rgbImg = cv2.cvtColor(img[i],cv2.COLOR_BGR2RGB)

            # plt.subplot(len(img), 1, i+1)
            plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])

        plt.show()
    else:
        if len(img.shape) < 3:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            rgbImg = cv2.cvtColor(img, cv2.CLOLOR_BGR2RGB)

        plt.imshow(rgbImg)
        plt.title(title)
        plt.xticks([]),plt.yticks([])
        plt.show()

src = cv2.imread("../images/cat.jpg", cv2.IMREAD_COLOR)
height, width, channel = src.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
img_show(["src","dst"], [src, dst], figsize = (8,4))
cv2.waitKey()
cv2.destroyAllWindows()