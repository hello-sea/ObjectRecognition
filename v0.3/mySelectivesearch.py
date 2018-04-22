# -*- coding: utf-8 -*-

'''

'''

from __future__ import (
    division,
    print_function,
)

import skimage.data
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import selectivesearch

import matplotlib.image as mpimg # mpimg 用于读取图片

def main():

    # loading astronaut image
    # img = skimage.data.astronaut()
    # print(type(img))
    img = mpimg.imread('../Data/train_LabelData/LabelData/500_0qEY_XcQi53Wo_EndAdYHN.jpg') # 读取和代码处于同一目录下的 lena.png
                                   # 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理

    # perform selective search
    ''' img_lbl, regions = selectivesearch.selective_search(
         img, scale=500, sigma=0.9, min_size=10)
        - img: 'numpy.ndarray'
        - scale: 
        - sigma:
        - min_size:
    '''
    img_lbl, regions = selectivesearch.selective_search(
        img, scale=500, sigma=0.9, min_size=10)
    

    candidates = set()
    for r in regions:
        # excluding same rectangle (with different segments)
        if r['rect'] in candidates:
            continue
        # # excluding regions smaller than 2000 pixels
        # if r['size'] < 2000:
        #     continue

        # if r['size'] > 200:
            # print(r['size'] )
            # continue

        if r['size'] < 30 or r['size']>2000:
            continue
        
        # print( r['size'], ":", r['rect'] ) 

        # distorted rects
        x, y, w, h = r['rect']

        if h == 0 or w == 0:
            continue
        if w / h > 2.5 or h / w > 2.5:
            continue
        candidates.add(r['rect'])

    # draw rectangles on the original image
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
    ax.imshow(img)
    for x, y, w, h in candidates:
        print(x, y, w, h)
        rect = mpatches.Rectangle(
            (x, y), w, h, fill=False, edgecolor='red', linewidth=1)
        ax.add_patch(rect)

    plt.show()

if __name__ == "__main__":
    main()

